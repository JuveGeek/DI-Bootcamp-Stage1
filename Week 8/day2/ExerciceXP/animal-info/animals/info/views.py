from django.shortcuts import render

animals= [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 4,
            "name": "Snake",
            "legs": 0,
            "weight": 5.67,
            "height": 0.2,
            "speed": 30,
            "family": 4 
        }
    ]


families= [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammal"
        },
        {
            "id":4,
            "name": "reptile"
        }
    ]

def family(request,id):
    
    context = {
        'families' : families,
        'animals': animals,
        'id': id,
        'page_title' : "Family",
    }
    return render(request,'posts/family.html', context)

def animal(request,id):
    
    context = {
        
        'animals': animals,
        'id': id,
        'page_title' : "Animal",
    }
    return render(request,'posts/animal.html', context)