
$("document").ready(function(){
    $("form").submit(function(){
        var select = $("#twtxt").val();
        $("form").attr("action",select);
        // alert(select);
        // alert($("form").attr("action"));
    });

});