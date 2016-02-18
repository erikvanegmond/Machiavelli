function updateGameStateView(){
            $.ajax({
                url: "/game/state",
                method: "GET",
                success: function( data ) {
                    $( "#gameState" ).html( "<ul id='gameList'></ul>" );
                    $.each(data['state'], function(k,v){
                        $("#gameList").append('<li>'+k+' - '+v+'</li>');
                    });
                    $.each(data['actions'], function(k,v){
                        $( "#actionForm" ).html( "<form id='actionList"+k+"'></form>" );
                        $.each(v, function(n,c){
                            $("#actionList"+k).append('<input type="radio" name="'+k+'" value="'+c+'">'+c+'</input>');
                        })
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