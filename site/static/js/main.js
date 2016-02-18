function updateGameStateView(){
    $.ajax({
        url: "/game/state",
        method: "GET",
        success: function( data ) {
            $( "#gameState" ).html( "<ul id='gameList'></ul>" );
            $.each(data['state'], function(k,v){
                $("#gameList").append('<li>'+k+' - '+v+'</li>');
            });
            $( "#actionForm" ).html("");
            $.each(data['actions'], function(k,v){
                $( "#actionForm" ).html(
                    "<form class='form-inline actionForm' id='actionList"+k+"'>"+
                    "<div class='form-group'><label for='actionList"+k+"select'>"+k+"</label> "+
                    "<select id='actionList"+k+"select' name='"+k+"' class='form-control'></select>"+
                    "</div>"+
                    " <button type='submit' class='btn btn-success'><span class='glyphicon glyphicon-ok' aria-hidden='true'></span> Pick</button>"+
                    "</form>"
                );
                $.each(v, function(n,c){
                    $("#actionList"+k+"select").append(
                        '<option value='+c+'>'+c+'</option>'
                    );
                });
                $( "#actionList"+k+"" ).submit(function( event ) {
                    event.preventDefault();
                    post_form_action("#actionList"+k)

                });
            });


        }
    });
};

function post_form_action(id){
    console.log('posting');
    console.log(id);
    var form_data = $(id).serializeArray();
    console.log(form_data);
    $.ajax({
        type: "POST",
        url: 'game/action',
        datatype: 'json',
        data: form_data, // serializes the form's elements.
        contentType: 'application/json; charset=utf-8',
        success: function(data)
        {
           alert(data); // show response from the php script.
        }
    });
}

function updateGameState(){
    $.ajax({
        url: "/game/update",
        method: "POST"
    });
    updateGameStateView();
};
function reset(){
    $.ajax({
        url: "/reset",
        method: "POST"
    });
    updateGameStateView();
};
$(document).ready(function(){
    $( "#updateGameStateViewButton" ).click(function(){updateGameStateView()});
    $( "#updateGameStateButton" ).click(function(){updateGameState()});
    $( "#reset" ).click(function(){reset()});
    updateGameState();


});