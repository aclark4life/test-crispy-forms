from django.shortcuts import render, redirect
from .forms import TimeEntryForm
from .models import TimeEntry


def index(request):
    time_entries = TimeEntry.objects.all()
    context = {'time_entries': time_entries}
    return render(request, 'index.html', context)


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
