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
                            "<form class='form-inline' id='actionList"+k+"'>"+
                            "<div class='form-group'><label for='actionList"+k+"select'>"+k+"</label> "+
                            "<select id='actionList"+k+"select' class='form-control'></select>"+
                            "</div>"+
                            " <button type='submit' class='btn btn-success'><span class='glyphicon glyphicon-ok' aria-hidden='true'></span> Pick</button>"+
                            "</form>"
                        );
                        $.each(v, function(n,c){
                            $("#actionList"+k+"select").append(
                                '<option value='+c+'>'+c+'</option>'
                            );
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