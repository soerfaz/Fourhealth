$("#check").click(function(){
    if($("#symptomps").val().length > 0){
        axios.post("/check", {
            symptoms: $("#symptomps").val(),
            fever: $("#fever").val()
        })
        .then(function (response) {
            console.log(typeof(response.data.precaution));      
                  
            $("#symptomps").val(null).trigger('change')
            $("#fever").val("35")
            console.log(response.data)
            $("#result").html(`<article-card
                                _name="${response.data.name}"
                                description="${response.data.description}"
                                precaution="${response.data.precaution}"
                                ></article-card>`)
        })
        .catch(function (error) {
            console.log(error);
            $("#result").html("<p>Error</p> ")
        });
    }else{
        $('#alertMessage').fadeIn();
        setTimeout(function() {
            $('#alertMessage').fadeOut();
        }, 3000);
    }
})
$('#alertMessage .close').click(function() {
    $('#alertMessage').fadeOut();
})

