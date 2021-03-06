(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
        if ($('#spinner').length > 0) {
            $('#spinner').removeClass('show');
        }
    }, 1);
  };
  spinner();
  
  
  // Initiate the wowjs
  new WOW().init();


  // Sticky Navbar
  $(window).scroll(function () {
      if ($(this).scrollTop() > 45) {
          $('.navbar').addClass('sticky-top shadow-sm');
      } else {
          $('.navbar').removeClass('sticky-top shadow-sm');
      }
  });
  
  
  // Dropdown on mouse hover
  const $dropdown = $(".dropdown");
  const $dropdownToggle = $(".dropdown-toggle");
  const $dropdownMenu = $(".dropdown-menu");
  const showClass = "show";
  
  $(window).on("load resize", function() {
      if (this.matchMedia("(min-width: 992px)").matches) {
          $dropdown.hover(
          function() {
              const $this = $(this);
              $this.addClass(showClass);
              $this.find($dropdownToggle).attr("aria-expanded", "true");
              $this.find($dropdownMenu).addClass(showClass);
          },
          function() {
              const $this = $(this);
              $this.removeClass(showClass);
              $this.find($dropdownToggle).attr("aria-expanded", "false");
              $this.find($dropdownMenu).removeClass(showClass);
          }
          );
      } else {
          $dropdown.off("mouseenter mouseleave");
      }
  });
  
  
  // Back to top button
  $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
          $('.back-to-top').fadeIn('slow');
      } else {
          $('.back-to-top').fadeOut('slow');
      }
  });

  $('.back-to-top').click(function () {
    $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
    return false;
});

$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
      $('.back-to-top2').fadeIn('slow');
  } else {
      $('.back-to-top2').fadeOut('slow');
  }
});

$('.back-to-top2').click(function () {
  window.location.href = "https://lin.ee/7K12Ixj";
});

// Screenshot carousel
$(".screenshot-carousel").owlCarousel({
  autoplay: true,
  smartSpeed: 1000,
  loop: true,
  dots: true,
  items: 1
});

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    loop: true,
    center: true,
    dots: false,
    nav: true,
    navText : [
        '<i class="bi bi-chevron-left"></i>',
        '<i class="bi bi-chevron-right"></i>'
    ],
    responsive: {
        0:{
            items:1
        },
        768:{
            items:2
        },
        992:{
            items:3
        }
    }
});

// Navbar on mobile
let elements = document.querySelectorAll(".nav-link:not(.navbar-toggle)");

for (let i = 0; i < elements.length; i++) {
	elements[i].addEventListener("click", () => {
		document.querySelector(".navbar-toggler").classList.toggle("collapsed");
    // document.querySelector(".navbar-collapse").classList.removeClass('show');
    $('.navbar-collapse').removeClass('show');
	});
}


})(jQuery);

