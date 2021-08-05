// show review form

$(document).ready(function () {
    $(".review_form_row").hide();
});

$(".showReviewForm").click(function (e) {
    $(".review_form_row").show();
    $(".write_review_text").hide();
    e.preventDefault();
});

$(".hideReviewForm").click(function (e) {
    $(".review_form_row").hide();
    $(".write_review_text").show();
    e.preventDefault();
});

