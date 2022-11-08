from django.forms import ModelForm, ImageField, CharField, Form
from app.models import Candidate


class CandidateModelForm(ModelForm):
    image = ImageField(required=False)

    class Meta:
        model = Candidate
        exclude = []


class CandidateUpdateForm(Form):
    image = ImageField(required=False)
    name = CharField(max_length=255)
    field = CharField(max_length=255)
    address = CharField(max_length=255)

    def save(self, pk):
        candidate = Candidate.objects.filter(pk=pk).first()

        image = self.data.get('image')
        name = self.data.get('name')
        field = self.data.get('field')
        address = self.data.get('address')

        candidate.image = image
        candidate.name = name
        candidate.field = field
        candidate.address = address

        candidate.save()
