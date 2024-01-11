// Toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header:

$('#toggle_header').click(function () {
    const header = $('header');
    header.toggleClass('red green');
});
