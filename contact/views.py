from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = 'contact/tags/form.html'

    def form_valid(self, contact_form):
        contact_form.save()
        send(contact_form.instance.email)
        return super().form_valid(contact_form)