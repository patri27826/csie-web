from django.shortcuts import  render
from django.views import generic

from .models import Member, Office_Member
from django.db.models import Q
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_member = Member.objects.all().count()
    num_office_member = Office_Member.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_member' : num_member,
        'num_office_member' : num_office_member,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'members/index.html', context=context)

from django.views import generic

class MemberListView(generic.ListView):
    model = Member

class MemberListView_csie(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(department__name__contains="資訊系") & Q(classification__name__contains='專任'))

class MemberListView_csieg(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(department__name__contains="資訊所") & Q(classification__name__contains='專任'))
class MemberListView_ai(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(department__name__contains="AI學程") & Q(classification__name__contains='專任'))

class MemberListView_med(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(department__name__contains="醫資所") & Q(classification__name__contains='專任'))

class MemberListView_imis(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(department__name__contains="製造所") & Q(classification__name__contains='專任'))

class MemberListView_adjunct(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(classification__name__contains='兼任'))

class MemberListView_joint(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(classification__name__contains='合聘'))

class MemberListView_visiting(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(classification__name__contains='客座'))

class MemberListView_retire(generic.ListView):
    model = Member
    def get_queryset(self, **kwargs):
        return Member.objects.filter(Q(classification__name__contains='退休'))

# class MemberListView_retired(generic.ListView):
#     model = Member
#     def get_queryset(self, **kwargs):
#         return Member.objects.filter(classification__name__contains='Retired')

class MemberDetailView(generic.DetailView):
    model = Member

class OfficeMemberListView(generic.ListView):
    model = Office_Member

class OfficeMemberDetailView(generic.DetailView):
    model = Office_Member