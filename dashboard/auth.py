from django.shortcuts import redirect


# For visitor as unauthenticated user
def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashbaord')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function

# check if the user is admin
def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/homepage')

    return wrapper_function



# check if the user is travellers
def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admins')
        else:
            return view_function(request, *args, **kwargs)

    return