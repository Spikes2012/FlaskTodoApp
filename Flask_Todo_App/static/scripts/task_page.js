/*
* Author: Yichen Song
* Target: task_page.html
*/

"use strict";


function openTasks(evt, tabName) { 
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function openDetails(evt, taskID) {
    document.getElementById("default").style.display = "none";
    var i, manage, details, tasklinks;

    manage = document.getElementsByClassName("manage");
    for (i = 0; i < manage.length; i++) {
        manage[i].style.display = "none";
    }

    details = document.getElementsByClassName("details");
    for (i = 0; i < details.length; i++) {
        details[i].style.display = "none";
    }

    tasklinks = document.getElementsByClassName("tasklinks");
    for (i = 0; i < tasklinks.length; i++) {
        tasklinks[i].className = tasklinks[i].className.replace(" active", "");
    }
    document.getElementById(taskID).style.display = "block";
    evt.currentTarget.className += " active";
}

function manageTask(id) {
    var mID = "m" + id;
    document.getElementById(mID).style.display = "block";
    document.getElementById(id).style.display = "none";
}

function back(id) {
    var mID = "m" + id;
    document.getElementById(mID).style.display = "none";
    document.getElementById(id).style.display = "block";
}

function init() {
    document.getElementById("defaultOpen").click();
}

window.onload = init;