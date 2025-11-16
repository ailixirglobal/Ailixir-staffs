from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Experiment, LabNote


@login_required
@permission_required("research.view_experiments", raise_exception=True)
def experiment_list(request):
    experiments = Experiment.objects.all()
    return render(request, "research/experiment_list.html", {"experiments": experiments})


@login_required
@permission_required("research.add_experiments", raise_exception=True)
def experiment_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("description")
        start_date = request.POST.get("start_date")

        Experiment.objects.create(
            title=title,
            description=desc,
            start_date=start_date,
            status="ongoing",
            lead_researcher=request.user
        )

        return redirect("research:experiment_list")

    return render(request, "research/experiment_add.html")


@login_required
@permission_required("research.view_experiments", raise_exception=True)
def experiment_detail(request, exp_id):
    exp = get_object_or_404(Experiment, id=exp_id)
    notes = exp.notes.all()
    return render(request, "research/experiment_detail.html", {
        "exp": exp,
        "notes": notes
    })


@login_required
@permission_required("research.add_labnote", raise_exception=True)
def labnote_add(request, exp_id):
    exp = get_object_or_404(Experiment, id=exp_id)

    if request.method == "POST":
        LabNote.objects.create(
            experiment=exp,
            author=request.user,
            title=request.POST.get("title"),
            note=request.POST.get("note"),
            attachment=request.FILES.get("attachment")
        )
        return redirect("research:experiment_detail", exp_id=exp.id)

    return render(request, "research/labnote_add.html", {"exp": exp})
    
@login_required
@permission_required("research.view_labnote", raise_exception=True)
def labnote_list(request):
    notes = LabNote.objects.select_related("experiment", "author").order_by("-created_at")
    return render(request, "research/labnote_list.html", {"notes": notes})