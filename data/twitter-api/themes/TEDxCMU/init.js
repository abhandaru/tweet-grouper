

$(document).ready(function() {
    var text = ['Updating live…','Get your tweet up here by tweeting @TEDxCMU or tagging with #TEDxCMU'];
    $('#logo-text').text(text[0]).fadeIn('slow');
    var index = 0;
    setInterval(function() {
        $('#logo-text').fadeOut('slow',function() {
            index = (1+index)%text.length;
            $('#logo-text').text(text[index]);
            $('#logo-text').fadeIn('slow')
        })
    },6000);
});
        
