$(function() {
    $('#savebtn').click(function () {
        console.log("click save button");
        var newAlias = document.getElementById("editedAlias");
        $('#alias').html(newAlias.value);
        newAlias.value = " ";
    });
 });