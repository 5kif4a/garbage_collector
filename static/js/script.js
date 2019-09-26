var dump_state = true;
var event_state = true;
function dump_sidebar() {
    if (dump_state == false){
        document.getElementById("dump").style.width = "0px";
        dump_state = true;
    }
    else if(dump_state == true) {
        document.getElementById("dump").style.width = "350px";
        dump_state = false;
    }
}
function event_sidebar() {
    if (event_state == false){
        document.getElementById("event").style.width = "0px";
        event_state = true;
    }
    else if(event_state == true) {
        document.getElementById("event").style.width = "350px";
        event_state = false;
    }
}
