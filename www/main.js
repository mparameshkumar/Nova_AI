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
});