from django.shortcuts import render, redirect
from .forms import TimeEntryForm

def create_time_entry(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page or display success message
            return redirect('/')

    else:
        form = TimeEntryForm()
    return render(request, 'create_time_entry.html', {'form': form})
