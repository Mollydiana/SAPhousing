from django.shortcuts import render, redirect

# Registration stuff
from video_tenant.forms import AccountForm, AccountCreationForm

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
            user.send_email("welcome {}".format(user.username), "Thank you for signing up")
            return redirect("login")
    else:
        form = AccountCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
