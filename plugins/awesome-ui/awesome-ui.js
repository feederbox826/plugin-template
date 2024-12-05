function awesomeui() {
    console.log('awesomeui loaded');
    // awesomeui code here
    alert("nice plugin repository!");
}

awesomeui()
PluginApi.Event.addEventListener("stash:location", (evt) => console.log("Location changed to: " + evt.location));