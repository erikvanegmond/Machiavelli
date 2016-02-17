function updateGameStateView(){
            $.ajax({
                url: "/game/state",
                method: "GET",
                success: function( data ) {
                    $( "#gameState" ).html( "<ul id='gameList'></ul>" );
                    $.each(data['state'], function(k,v){
                        $("#gameList").append('<li>'+k+' - '+v+'</li>');
                    });
                    $( "#actionForm" ).html( "<ul id='actionList'></ul>" );
                    $.each(data['actions'], function(k,v){
                        $("#actionForm").append('<li>'+k+' - '+v+'</li>');
                    });
                }
            });
        };
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