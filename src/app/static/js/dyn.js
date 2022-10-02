$(document).ready(function(){


    $(".mijnsliders").val(50);  //Initialiseer alle ranges (sliders) op 50

    $(".mijnsliders").change(function() {
        console.log("Slider " + this.id + 'aangepast naar ' + $(this).val());
        $('#' + this.id + 'waarde').text($(this).val())
    });     

    // $("#mijn1eslider").change(function() {
    //   alert("slider 1 aangepast");
    //   console.log("slider 1 aangepast");
    //   $("#mijn1ewaarde").text($("#mijn1eslider").val())
    // });         
    
  });