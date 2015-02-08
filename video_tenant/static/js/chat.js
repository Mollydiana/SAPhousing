$( document ).ready(function() {
    // App ID value from the dev portal. You can play
    // around with the supplied ID or replace it with
    // your own.
    var appid = "b71b5d08-8567-4c4c-a3dd-4fa935804f3a";
    var activeCall;
    var endpointId=$('.respoke-username').attr("id");

    console.log(endpointId);

    // Create the client object using the App ID
    var client = respoke.createClient({
        appId: appid,
        developmentMode: true
    });

    client.connect({
        endpointId: endpointId, // your username is the endpoint
        presence: 'available'
    });

    // "connect" event fired after successful connection to Respoke
    client.listen('connect', function() {
        $("#status").html("Connected to Respoke as \"" + endpointId + "\"");
    });

    // Listen for incoming calls
    client.listen('call', function(evt) {
        activeCall = evt.call;

        // We only want to answer if we didn't initiate the call
        if(activeCall.caller !== true) {
            activeCall.answer(callOptions);

            // The hangup event indicates the call is over
            activeCall.listen('hangup', function () {
                hangUp();
            });
        }
    });

    // The options for our video call including constraints and callbacks
    var callOptions = {
        constraints: {audio: true, video: true},

        // Your video
        onLocalMedia: function(evt) {
            setVideo('localVideoSource', evt.element)
        },

        // Their video
        onConnect: function(evt) {
            setVideo('remoteVideoSource', evt.element)
        }
    };

    // Adds the supplied video element as a child of the supplied element
    function setVideo(elementId, videoElement) {
      console.log("setVideo", videoElement  );
        var videoParent = document.getElementById(elementId);
        videoParent.innerHTML = "";
        videoParent.appendChild(videoElement);
    }

    // Call the recipient
    $("#doCall").click(function() {
//        var recipientId = $("#remoteId").val();
        var recipientId = "respoke-"+$("#ownerUsername").text();
        console.log(recipientId);
        var recipientEndpoint = client.getEndpoint({ id: recipientId });
        activeCall = recipientEndpoint.startVideoCall(callOptions);
        console.log("Trying to connect. ", activeCall);
        console.log(recipientEndpoint);
    });

    // Hangup the call
    $("#doHangUp").click(hangUp);

    // End the current call and clean up the DOM
    function hangUp() {
        activeCall.hangup();
        activeCall = null;

        // Remove the video elements
        $("#localVideoSource").html("");
        $("#remoteVideoSource").html("");
    }
});