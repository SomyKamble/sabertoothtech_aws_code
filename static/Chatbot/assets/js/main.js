// Navbar Active
$('#navbarNav .navbar-nav a').on('click', function () {
    $('#navbarNav .navbar-nav').find('li.active').removeClass('active');
    $(this).parent('li').addClass('active');
});

function myScrolling() {
    window.scrollBy({ top: 900, left: 0, behavior: 'smooth' });
}

(function (d, m) {
    var kommunicateSettings = { "appId": "284a3f9a87d25b57664794489a18965cb", "popupWidget": true, "automaticChatOpenOnNavigation": true };
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
    var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
    window.kommunicate = m; m._globals = kommunicateSettings;
})(document, window.kommunicate || {});
