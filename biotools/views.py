from django.shortcuts import render

from .forms import SeqContentForm
from .forms import RevCompForm
from .forms import RandomDNAForm
from . import utils

def seqcontent_view(request):
    if request.method == 'POST':
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            word_size = form.cleaned_data['word_size']
            d = utils.count_words(seq, word_size)
            return render(
                request, 
                'biotools/seqcontent.html', 
                {'results':d,
                 'sequence_length': len(seq),
                }
            )
    else:
        form = SeqContentForm()
    return render(request, 'biotools/seqcontent.html', {'form':form})

def revcomp_view(request):
    if request.method == 'POST':
        form = RevCompForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            choice = form.cleaned_data['choice']
            return render(
                request, 
                'biotools/revcomp.html', 
                {'results':utils.chooseMethod(seq,choice),
                }
            )
    else:
        form = RevCompForm()
    return render(request, 'biotools/revcomp.html', {'form':form})

def randomdna_view(request):
    if request.method == 'POST':
        form = RandomDNAForm(request.POST)
        if form.is_valid():
            propabilities = (
                form.cleaned_data["a_freq"],
                form.cleaned_data["c_freq"],
                form.cleaned_data["g_freq"],
                form.cleaned_data["t_freq"]
                )
            length = form.cleaned_data["generated_Sequence_Length"]
            return render(request,
                'biotools/randomdna.html',
                {'results': utils.generateRandomDNA(length,propabilities)})
    else:
        form = RandomDNAForm()
    return render(request, 'biotools/randomdna.html', {'form':form})