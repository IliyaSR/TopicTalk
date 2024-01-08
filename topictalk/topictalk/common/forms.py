from django import forms


class SearchForm(forms.Form):
    community_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Search by community...'
            }
        ),
        label= ''
    )
