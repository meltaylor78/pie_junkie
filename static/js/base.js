/*jshint esversion: 6 */
/*globals $:false */

$(document).ready(function () {
    $("#product-search-large").submit(function (e) {
        e.preventDefault();
        let search = $("#custom-search-group-large").val();
        window.location = `/products/?search=${search}`;
    });

    $("#product-search-small").submit(function (e) {
        e.preventDefault();
        let search = $("#custom-search-group-small").val();
        window.location = `/products/?search=${search}`;
    });

    $(".close-message-container").click(function() {
        $(".message-container").hide();
    });

    setTimeout(function() {
        $(".message-container").hide();
    }, 4000);
});
