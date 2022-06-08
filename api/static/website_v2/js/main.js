jQuery(document).ready(function() {
    if ($(".cd-stretchy-nav").length > 0) {
        var a = $(".cd-stretchy-nav");
        a.each(function() {
            var b = $(this),
            c = b.find(".cd-nav-trigger");
            c.on("click",
            function(d) {
                d.preventDefault();
                b.toggleClass("nav-is-visible")
            })
        });
        $(document).on("click",
        function(b) { (!$(b.target).is(".cd-nav-trigger") && !$(b.target).is(".cd-nav-trigger span")) && a.removeClass("nav-is-visible")
        })
    }
});