$(document).ready(function() {
	var navsHeight = $(".header-navbar").height() + $(".footer-nav").height();
	$(".main-container").css("min-height", $(window).height() - navsHeight);
});

