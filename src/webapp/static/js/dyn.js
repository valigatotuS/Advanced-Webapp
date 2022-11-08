$(document).ready(function(){
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
    });  
});

