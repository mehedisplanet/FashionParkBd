from django import forms
from .models import Product, UserReviews,Purchase

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReviews
        fields = ['name','email','body']
        
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user_purchased = Purchase.objects.filter(user=self.user, product=self.product).exists()
        if not user_purchased:
            raise forms.ValidationError("You must purchase  the product to leave a review.")
        return cleaned_data