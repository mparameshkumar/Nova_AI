$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn'
        },
        out: {
            effect: 'bounceOut'
        }
    });

    //Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 1000,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
      });
      //siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeIn',
            sync: true,
        },
        out: {
            effect: 'fadeOutUp',
            sync: true,
        }
    });
    //MIC BUTTON ACTION
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
    });
});