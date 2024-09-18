let startTime, endTime;

window.onload = function(){
    startTime = new Date();
};

window.onbeforeunload = function(){
    endTime = new Date();
    let timeSpent = Math.round((endTime - startTime) / 1000);

    navigator.sendBeacon('/track-time', JSON.stringify({
        page:window.location.pathname,
        timeSpent: timeSpent
    }));
};