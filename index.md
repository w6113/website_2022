---
layout: index
---


#### Overview

Data management systems are the corner-stone of modern applications, businesses, and science (including data).  If you were excited by the topics in 4111,  this graduate level course in database systems research will be a deep dive into classic and modern database systems research.  Topics will range from classic database system design, modern optimizations in single-machine and multi-machine settings, data cleaning and quality, and application-oriented databases.   This semester's theme will look at how learning has affected many classic data management systems challenges, and also how data management systems support and extends ML needs.

See [FAQ](./syllabus#faq) for difference between 6113 and the other database courses. 

<!--<small style="color: grey">Course capped at 25. </small>-->


#### Information 

* Class: Th 2-4PM in 829 Mudd
* Instructor: [Eugene Wu](http://www.eugenewu.net), OH: Thurs 12-1PM 421 Mudd
* [Syllabus & FAQ](./syllabus), 
[Slack](https://w6113-s23.slack.com),
[Project](./projects),
[Papers](./papers)
* Prereqs: W4111 Intro to DB (required), W4112 DB Implementations (recommended).  Ugrads OK; see Prof Wu

#### Grading 

* Discussion Prep 30%
* Class participation 30%
* [Project](./projects) 40%:
   Final Presentation <small>10%</small>,
   Paper <small>30%</small>

<!--
* [Paper Reviews](./papers) <small>10%</small>
* [Assignments](./assignments) <small>15%</small>
-->


#### Recent Announcements


#### Tentative Schedule

<style>
.presenter { }
</style>

<table class="table table-striped schedule">
  <thead>
  <tr>
    <!--<th class="idx" style="width: 3em; max-width:3em;"></th>-->
    <th class="date" style="width: 15em; max-width: 15em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 15%;"> <p> <span>Topic </span> </p> </th>
    <th style="width: 10%"> <p> <span>Notes </span> </p> </th>
    <!--<th style="width: 15%;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 15%;"> <p> <span>Due</span> </p> </th>-->
  </tr>
  </thead>
{% assign idx = 0 %}

{% for r in site.data.schedule %}
  {% assign idx = idx | plus: 1  %}

  <tr style="background-color: {{r.color}}; ">
    <td class="date">C{{idx}}: {{r.date}}</td>
    <td class="slug">
      {% if r.link %}
        <a href="./papers#{{r.link}}"><b>{{r.slug}}</b></a>
      {% else %}
        <b>{{r.slug}}</b>
      {% endif %}

      {% if r.papers %}
      <ul>
      {% for p in r.papers %}
        <li><a href="{{p.url}}">{{p.title}}</a></li> 
      {% endfor %}
      </ul>
      {% endif %}

      {% if r.presenter %}
        <br/>
        <span class='presenter'>Presenter: {{r.presenter}}</span>
      {% endif %}

      {% if r.misc %}
      <div> {{r.misc|raw}}</div>
      {% endif %}

    </td>
    <td class="notes">
      {% if r.notes %}
        {{r.notes|raw}}
      {% endif %}
    </td>
    <!--
    <td>{{r.assigned | safe}}</td>
    <td>{{r.due | safe}}</td>
    -->
  </tr>
{% endfor %}

</table>


Course design inspired by

* [Cal's CS286](https://cs286berkeley.net/)
* [Waterloo's CS848](https://cs.uwaterloo.ca/~kmsalem/courses/cs848S19/schedule.shtml)
* Colin Raffel's [Role playing seminar](https://colinraffel.com/blog/role-playing-seminar.html)
* Carl Vondrick's self supervision graduate seminar
