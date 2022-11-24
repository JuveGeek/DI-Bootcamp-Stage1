from django.shortcuts import render

peopledata = [{
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
}, {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
}, {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
}, {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
}]


# Create your views here.
def people(request):

    context = {
        'peopledata': peopledata,
        'page_title': "People",
    }
    return render(request, 'posts/people.html', context)


def peoplebyid(request,id):
    
    context = {
        'id': id,
        'peopledata': peopledata,
        'page_title': "People ",
    }
    return render(request, 'posts/peoplebyid.html', context)
