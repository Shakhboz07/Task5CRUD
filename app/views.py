from django.shortcuts import render, redirect, get_object_or_404

from app.models import Candidate
from app.forms import CandidateModelForm, CandidateUpdateForm


# Read

def index_page(request):
    candidate = Candidate.objects.all()
    context = {
        "candidates": candidate
    }
    return render(request, 'app/index.html', context)


# Create

def candidateCreate(request):
    if request.method == "POST":
        form = CandidateModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index_page')
    return render(request, 'app/create.html')


# Read update

def form_page(request, pk):
    candidate = get_object_or_404(Candidate, id=pk)
    context = {
        'candidate': candidate
    }
    if request.method == "POST":
        form = CandidateUpdateForm(request.POST, request.FILES)
        form.save(pk)
        return redirect('index_page')
    return render(request, 'app/form.html', context)


# delete
def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, id=pk)
    candidate.delete()
    return redirect('index_page')
