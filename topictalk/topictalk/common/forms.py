from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Search by community...'
            }
        ),
        label=''
    )
    section = forms.CharField(max_length=100, required=False)
