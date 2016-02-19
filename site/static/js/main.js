function updateGameStateView(){
    $.ajax({
        url: "/game/state",
        method: "GET",
        success: function( data ) {
            update_screen(data);
        }
    });
};

function update_screen(data) {
    $( "#gameStateBody" ).html( "" );
    $( "#playerStateBody" ).html( "" );
    var gameorder = ['game_name', 'n_players', 'open_cards', 'n_open_cards', 'closed_cards', 'game_state', 'players', 'player_order'];
    var playerorder = ['current_player',
    'current_player_status', 'king_player']
    $.each(gameorder, function(i, o){
        $("#gameStateBody").append('<tr><th scope="row">'+o+'</th><td>'+data['state'][o]+'</td></tr>');
    });
    $.each(playerorder, function(i, o){
        $("#playerStateBody").append('<tr><th scope="row">'+o+'</th><td>'+data['state'][o]+'</td></tr>');
    });
    $( "#actionForm" ).html("");
    $.each(data['actions'], function(k,v){
        $( "#actionForm" ).append(
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
            post_form_action("#actionList"+k+"select")
        });
    });

    if(data['message'].length > 0){
        $('#messageModalBody').html(data['message']);
        $('#messageModal').modal('show');
    }
    console.log(data['message'].length);
}

function post_form_action(id){
    var sendData = {};
    sendData[$(id).attr('name')] = $(id).val();
    $.ajax({
        type: "POST",
        url: 'game/action',
        datatype: 'json',
        data: JSON.stringify(sendData), // serializes the form's elements.
        contentType: 'application/json; charset=utf-8',
        success: function(data)
        {
           update_screen(data); // show response from the php script.
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
    updateGameStateView();


});