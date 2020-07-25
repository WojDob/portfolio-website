from django import forms


class SeqContentForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(attrs=
            {'placeholder': 'Plain sequence',
             'rows': 4,}
        ), 
        min_length=10, 
        required=True)
    word_size = forms.IntegerField(initial=1, required=True)

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        return sequence.upper()

    def clean(self):
        sequence = self.cleaned_data["sequence"]
        word_size = self.cleaned_data["word_size"]
        if sequence and word_size:
            if len(sequence) < word_size:
                raise forms.ValidationError(
                    "Sequence cannot be shorter than word size."
                )

class RevCompForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(attrs=
            {'placeholder': "Paste sequence here in plain or FASTA", 
            'rows': 10,'cols':90}
        ),
        min_length=5,
        required=True)
    CHOICES = (('reverseComplement', 'Reverse complement'),('reverse', 'Reverse'),('complement', 'Complement'),)
    choice = forms.ChoiceField(label='Method', widget=forms.Select,choices=CHOICES)

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        return sequence.upper()

class RandomDNAForm(forms.Form):
    generated_Sequence_Length = forms.IntegerField(min_value = 20, max_value=10000,required=True)
    a_freq = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    c_freq = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    g_freq = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    t_freq = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)

    def clean(self):
        if self.cleaned_data["a_freq"] + self.cleaned_data["c_freq"] + self.cleaned_data["g_freq"] + self.cleaned_data["a_freq"] != 1:
            raise forms.ValidationError(
                    "Frequencies must sum up to 1"
                ) 