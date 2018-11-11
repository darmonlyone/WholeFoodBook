$(function() {
    $('#fb-login').click(function () {
        console.log("click");
        $("#start-login").hide();
        $("#hamburger").show();
    });

    $('#gg-login').click(function () {
        console.log("click");
        $("#start-login").hide();
        $("#hamburger").show();
    });

    $('#SignOut').click(function () {
        console.log("user has signed out.");
        $("#start-login").show();
        $("#hamburger").hide();
    });
 });