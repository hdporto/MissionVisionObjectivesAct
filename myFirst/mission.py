from django.shortcuts import render
from django.http import HttpResponse

def mission(request):
    mission = "<h1>The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.</h1>"
    return HttpResponse(mission);

def vision(request):
    vision = "<h1>The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.</h1>"
    return HttpResponse(vision);

def goals(request):
    goals = """<ol>
        <li>
            Increase faculty performance by obtaining a minimum rating of 4.00 in the semestral faculty evaluation of each faculty for the next fiveyears.
        </li>
        <li>
            Maintain competent faculty line-up by sending all permanent fulltime faculty to at least one (1) IT related training, conference, orseminar annually for the next five years.
        </li>
        <li>
            Conduct a minimum of two (2) researches, IT projects or production of instructional materials annually for the next five years.Achieve a minimum of 50% student passing percentage in the IT certification annually for the next five years.
        </li>
        <li>
            Maintain state-of-the-art information technology learning environment through annual procurement or upgrading of hardwareor software licenses for at least one computer laboratory for the next five years.
        </li>
        <li>
            Set up minimum of two (2) academe-industry partnership projects and commercialization initiatives or research publication andpresentation annually in preparation for the next CHED COD/COE application. 
        </li>
        <li>
            Strengthen promotion program to increase freshman enrollees to a minimum of three (3) class sections annually for the next five years.
        </li>
    </ol>"""
    return HttpResponse(goals);