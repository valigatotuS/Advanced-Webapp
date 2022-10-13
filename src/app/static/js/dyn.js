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

    $.ajax({
        method : 'GET',
        url : 'api/lamp/lamp1a',
        success : function(e){
            console.log(e.result);
        }
    })

    $(".mijnsliders").change(function() {
        console.log("Slider " + this.id + 'aangepast naar ' + $(this).val());
        $('#' + this.id + 'waarde').text($(this).val());
        // api call 
        $.ajax({
            data : {
              lamp_id : $(this).closest("div").parent().attr("id"),
              dimming : $(this).val()
            },
            method : 'POST',
            url : 'api/lamp/'
        })
    });     

    // $("#mijn1eslider").change(function() {
    //   alert("slider 1 aangepast");
    //   console.log("slider 1 aangepast");
    //   $("#mijn1ewaarde").text($("#mijn1eslider").val())
    // });         
    
  });

// my functions

function refreshSlider(){
    $("#mijn1eslider").val(99);
    console.log('Get lamp status');
}