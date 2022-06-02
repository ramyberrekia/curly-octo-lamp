from django.shortcuts import render, redirect, reverse, get_object_or_404 
from django.views.generic import CreateView, TemplateView
from .models import Organisation
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import IsStaffOrIsSuperUserRequiredMixin
from .forms import OrganisationPostForm, ApproveOrDeclineOrgForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

class OrganisationPostView(LoginRequiredMixin, CreateView):
    model = Organisation
    form_class = OrganisationPostForm

    def get_success_url(self):
        return reverse('organisations:organisations_list')
    def form_valid(self, form):
        organisation = form.save(commit=False)
        organisation.organisor = self.request.user
        organisation.save()
        messages.success(self.request, 'Your organisation has been posted, we\'ll contact you on your email after making a decision about it')
        return super(OrganisationPostView, self).form_valid(form)


    def form_invalid(self, form):

        return super(OrganisationPostView, self).form_invalid(form)


class OragnisationListView(IsStaffOrIsSuperUserRequiredMixin, TemplateView):
    model = Organisation
    context_object_name = 'organisations'
    template_name = 'organisations/organisation_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_oragnisations"] = Organisation.objects.pending_oragnisations() if Organisation.objects.pending_oragnisations().exists() else None
        context["approved_oragnisations"] = Organisation.objects.approved_oragnisations() if Organisation.objects.approved_oragnisations().exists() else None
        context["rejected_oragnisations"] = Organisation.objects.rejected_oragnisations() if Organisation.objects.rejected_oragnisations().exists() else None
        return context
    

def send_approval_or_declined_mail(request, user, choice):
    protocol = 'https' if request.is_secure() else 'http'
    domain = get_current_site(request)
    email_subject = 'Your orgnisation have been approved' if choice == 'A' else 'Unfortunally your organisation have been declided'
    context = {
        'user':user,
        'domain':domain,
        'protocol':protocol,
    }
    email_body = render_to_string('email/approval_email.html', context ) if choice == 'A' else render_to_string('email/declined_email.html', context)
    send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email,])


# @  decorator
# if organisation.is_approved
def organisation_detail_view(request, slug):
    organisation = get_object_or_404(Organisation, slug=slug)
    form = ApproveOrDeclineOrgForm()
    if request.method =='POST':
        form = ApproveOrDeclineOrgForm(request.POST)
        choice = request.POST.get('choice')
        if choice == 'A':
            organisation.is_approved = True
            organisation.is_rejected = False
            organisation.is_pending = False
            organisation.organisor.profile.is_organisor = True
            organisation.organisor.profile.save()
            organisation.save()
            send_approval_or_declined_mail(request, organisation.organisor, choice)
            return redirect(reverse('hotels:hotels_list'))
        if choice == 'D':
            organisation.is_declined = True
            organisation.is_approved = False
            organisation.is_pending = False
            organisation.save()
            send_approval_or_declined_mail(request, organisation.organisor, choice)
            return redirect(reverse('hotels:hotels_list'))



    context = {
        'organisation':organisation,
        'form':form,
    }

    return render(request, 'organisations/organisation_detail.html', context)