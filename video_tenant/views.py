from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Registration stuff
from geoposition.forms import GeopositionField
from video_tenant.forms import AccountForm, AccountCreationForm
from video_tenant.models import Rental

"""
All rentals
"""

@login_required
def my_rental(request):
    all_rentals = Rental.objects.filter(owner=request.user)
    return render(request, 'rental/all_rentals.html', {'all_rentals': all_rentals})

"""
All rentals
"""


def rental(request):
    all_rentals = Rental.objects.all()
    return render(request, 'rental/all_rentals.html', {'all_rentals': all_rentals})
                                                       # 'form': GeopositionField().widget})
"""
shows detail rental page
"""

def view_rental(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id)

    return render(request, 'rental/view_rental.html', {'rental': rental})

"""
Shows the account page
"""


def account(request):
    account_form = AccountForm()
    return render(request,'registration/account.html', {
        'account_form': account_form
    })

"""
Shows the registration form page!
"""


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.send_email("welcome {}".format(user.username), "Thank you for signing up")
            return redirect("login")
    else:
        form = AccountCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
