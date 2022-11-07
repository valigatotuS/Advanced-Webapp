$(document).ready(function(){

    // $(".mijnsliders").val(50);  //Initialiseer alle ranges (sliders) op 50

    // $("#mijn1eslider").val(
    //     $.ajax({
    //         data : {
    //           lamp_id : $(this).closest("div").parent().attr("id")
    //         },
    //         method : 'GET',
    //         url : 'api/lamp/'
    //     })
    // );
    
    // $.ajax({
    //     method : 'GET',
    //     url : 'api/lamp/lamp1a',
    //     success : function(e){
    //         console.log(e.result);
    //     }
    // })



    $(".mijnsliders").change(function() {
        console.log("Slider " + this.id + 'aangepast naar ' + $(this).val());
        $('#' + this.id + 'waarde').text($(this).val() + " %");
        // api call 
        $.ajax({
            data : {
              lamp_id : $(this).closest("div").parent().attr("id"),
              dimming : $(this).val()
            },
            method : 'POST',
            url : 'api/lamp/' + $(this).closest("div").parent().attr("id")
        })
        // window.alert("sometext");
    });     

    //  web-socket implementation
    
    
    //   var socket = io();
    
    //   var messages = document.getElementById('messages');
    //   var form = document.getElementById('form');
    //   var input = document.getElementById('input');
    
    //   form.addEventListener('submit', function(e) {
    //     e.preventDefault();
    //     if (input.value) {
    //       socket.emit('addToChat', input.value);
    //       input.value = '';
    //     }
    //   });
    
    //   socket.on('ReceiveFromChatServer', function(msg) {
    //     var item = document.createElement('li');
    //     item.textContent = msg;
    //     messages.appendChild(item);
    //     window.scrollTo(0, document.body.scrollHeight);
    //     console.log(msg)
    //   });
    
    
});


  
// my functions

function refreshSlider(){
    $("#mijn1eslider").val(99);
    console.log('Get lamp status');
}

