# service_requests/views.py
from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.customer = request.user.userprofile
            request_obj.save()
            return redirect('request_detail', request_id=request_obj.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def request_detail(request, request_id):
    request_obj = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'service_requests/request_detail.html', {'request': request_obj})