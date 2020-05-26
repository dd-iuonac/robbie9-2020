$(document).ready(function () {

    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    console.log("READY");

    //receive details from server
    socket.on('take_picture', function () {
        $('#log').append("<li>Take picture</li>");
    });

    socket.on('image_uploaded', function () {
        $('#log').append("<li>Image uploaded</li>");
    });

    socket.on('uploading_image', function() {
        $('#log').append("<li>Uploading image</li>");
    });

    socket.on('traffic_detected', function () {
        $('#log').append("<li>Traffic detected</li>");
    });

    socket.on('traffic_not_detected', function () {
        $('#log').html("<p>Traffic not detected</p>");
    });

    socket.on('analyse_image', function() {
        $('#log').html("<p>Analyse image</p>");
    });

    socket.on('move_forward', function() {
        $('#log').html("<p>Moving forward</p>");
    });

    socket.on('running', function () {
        $('#log').html("<p>Running</p>");
    });
    socket.on('stopped', function () {
        $('#log').html("<p>Stopped</p>");
    });
});