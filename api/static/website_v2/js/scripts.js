/* Description: Custom JS file */

/* Navigation*/
// Collapse the navbar by adding the top-nav-collapse class

window.onscroll = function () {
	scrollFunction();
	// scrollFunctionBTT(); // back to top button
};

window.onload = function () {
	scrollFunction();
};

function scrollFunction() {
	if (document.documentElement.scrollTop > 30) {
		document.getElementById("navbar").classList.add("top-nav-collapse");
	} else if ( document.documentElement.scrollTop < 30 ) {
		document.getElementById("navbar").classList.remove("top-nav-collapse");
	}
}

// Navbar on mobile
let elements = document.querySelectorAll(".nav-link:not(.dropdown-toggle)");

for (let i = 0; i < elements.length; i++) {
	elements[i].addEventListener("click", () => {
		document.querySelector(".offcanvas-collapse").classList.toggle("open");
	});
}

document.querySelector(".navbar-toggler").addEventListener("click", () => {
  console.log("test")
  	document.querySelector(".offcanvas-collapse").classList.toggle("open");
});

// Hover on desktop
function toggleDropdown(e) {
	const _d = e.target.closest(".dropdown");
	let _m = document.querySelector(".dropdown-menu", _d);

	setTimeout(
		function () {
		const shouldOpen = _d.matches(":hover");
		_m.classList.toggle("show", shouldOpen);
		_d.classList.toggle("show", shouldOpen);

		_d.setAttribute("aria-expanded", shouldOpen);
		},
		e.type === "mouseleave" ? 300 : 0
	);
}

// On hover
const dropdownCheck = document.querySelector('.dropdown');

if (dropdownCheck !== null) { 
	document.querySelector(".dropdown").addEventListener("mouseleave", toggleDropdown);
	document.querySelector(".dropdown").addEventListener("mouseover", toggleDropdown);

	// On click
	document.querySelector(".dropdown").addEventListener("click", (e) => {
		const _d = e.target.closest(".dropdown");
		let _m = document.querySelector(".dropdown-menu", _d);
		if (_d.classList.contains("show")) {
			_m.classList.remove("show");
			_d.classList.remove("show");
		} else {
			_m.classList.add("show");
			_d.classList.add("show");
		}
	});
}
  

/* Card Slider - Swiper */
// var cardSlider = new Swiper('.card-slider', {
// 	autoplay: {
// 		delay: 4000,
// 		disableOnInteraction: false
// 	},
// 	loop: true,
// 	navigation: {
// 		nextEl: '.swiper-button-next',
// 		prevEl: '.swiper-button-prev'
// 	}
// });


/* Back To Top Button */
// Get the button
// myButton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
// function scrollFunctionBTT() {
// 	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
// 		myButton.style.display = "block";
// 	} else {
// 		myButton.style.display = "none";
// 	}
// }

// When the user clicks on the button, scroll to the top of the document
// function topFunction() {
// 	document.body.scrollTop = 0; // for Safari
// 	document.documentElement.scrollTop = 0; // for Chrome, Firefox, IE and Opera
// }

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
  if ($(this).scrollTop() > 40) {
      $('.navbar').addClass('fixed-top');
  } else {
      $('.navbar').removeClass('fixed-top');
  }
});

// Screenshot carousel
$(".screenshot-carousel").owlCarousel({
  autoplay: true,
  smartSpeed: 1000,
  loop: true,
  dots: true,
  items: 1
});

$('.owl-service-item').owlCarousel({
  items:2,
  loop:true,
  dots: true,
  nav: false,
  autoplay: false,
  margin:15,
    responsive:{
      0:{
        items:1
      },
      600:{
        items:2
      },
      1000:{
        items:2
      }
    }
  })

  $('.owl-banner').owlCarousel({
		items:1,
		loop:true,
		dots: true,
		nav: false,
		autoplay: true,
		margin:0,
		  responsive:{
			  0:{
				  items:1
			  },
			  600:{
				  items:1
			  },
			  1000:{
				  items:1
			  },
			  1600:{
				  items:1
			  }
		  }
	})

  $('.colorful').click(function(){
    $('.colorful').removeClass('active');
    $(this).addClass('active');
    var value = this.getAttribute("value");
     ajaxRequest(1,1000,value);
  })
  
  var ajaxRequest = function (pageNo, pageSize, color) {
    $.ajax({
        url: "/api/v1/admin/templates/getList?pageNo="+pageNo+"&pageSize="+pageSize+"&color=" +color,
        type: "GET",
        // data: data,
        error: function () {
          var html = '<div class="swiper-slide"><div data-wow-delay="0.3s" style="text-align: center;">Error</div></div>'
          document.getElementById('template_swiper').innerHTML = html;
        },
        async:false,
        success: function (data) {
          var arr = data.data.items
          var html = ""
          for (let i = 0; i < arr.length; i++) {
            var item= '<div class="swiper-slide">' +
            '<div class=" wow fadeInUp iframe-center" data-wow-delay="0.3s" style="visibility: visible; animation-delay: 0.3s; animation-name: fadeInUp;">'+
              '<div class="room-item shadow rounded overflow-hidden" style="background-color:#fff;">'+
                '<div class="position-relative" style="min-height:200px;">'+
                  '<a href="https://www.uniecard.com/viewer/template/'+arr[i]['key']+'" target=" _blank">'+
                    '<img class="img-fluid-template swiper-lazy" data-src="' + arr[i]['coverUrl']+ '">'+
                    '<div class="swiper-lazy-preloader"></div>'+
                  '</a>'+
                '</div>'+
                '<h6 class="template-title">'+arr[i]['name']+'</h6>'+
                // '<a class="template-button" style="font-family: \'Mitr\', sans-serif;" href="https://www.uniecard.com/viewer/template/'+arr[i]['key']+'" target=" _blank">เพิ่มเติม</a>'+
                '<a type="button" class="template-button" style="font-family: \'Mitr\', sans-serif;" onclick=showModal("'+arr[i]['key'].toString()+'","'+arr[i]['name'].toString()+'")>เพิ่มเติม</a>'+
              '</div></div>' + '</div>'
            // var item = '<div class="swiper-slide"><div><img data-src="'+arr[i]['coverUrl']+'" class="swiper-lazy"> <div class="swiper-lazy-preloader"></div></div></div>'
              html = html + item
          }
          if (html == "") {
            html = '<div class="swiper-slide"><div data-wow-delay="0.3s" style="text-align: center;">No Data</div></div>'
          }
          document.getElementById('template_swiper').innerHTML = html;
          var swiper = new Swiper(".mySwiper", {
//             lazyLoading : true,  //启动延迟加载
// 　　lazyLoadingInPrevNext : true,      //延迟加载应用到最接近的slide的图片
// 　　lazyLoadingInPrevNextAmount : 1,   //加载下一个slide
// 　　lazyLoadingOnTransitionStart : true,  //过渡到slide一开始就加载，设置为true
            lazy: {
              loadPrevNext: true,
              loadPrevNextAmount: 10000,
              loadOnTransitionStart: true,
              loadingClass: 'my-lazy-loading',
            },
            slidesPerView: 2,
            centeredSlides: false,
            grid: {
              fill: 'column',
              rows: 2,
            },
            slidesPerGroup: 2,
            spaceBetween: 20,
            grabCursor: true,
            keyboard: {
              enabled: true,
            },
            breakpoints: {
              // '@0.75': { //当屏幕宽高比大于等于0.75
              //   grid: {
              //     // fill: 'column',
              //     rows: 1,
              //   },
              //   },
              //   '@2.00': { //当屏幕宽高比大于等于1
              //     grid: {
              //       // fill: 'column',
              //       rows: 3,
              //     },
              //   },
              // 769
              693: {
                slidesPerView: 4,
                slidesPerGroup: 4,
                spaceBetween: 30,
              },
              // 993
              1011: {
                slidesPerView: 6,
                slidesPerGroup: 6,
                spaceBetween: 30,
              }
            },
            scrollbar: {
              el: ".swiper-scrollbar",
            },
            pagination: {
              el: ".swiper-pagination",
              type: "fraction",
            },
            navigation: {
              nextEl: ".swiper-button-next",
              prevEl: ".swiper-button-prev",
            },
            //点击事件
            //   onTap: function(swiper){
            //     alert('你tap了Swiper');
            // },//在移动端，click会有 200~300 ms延迟，所以请用tap代替click作为点击事件
          });
        }
    });
  }

  function doMobileActions() {
    ajaxRequest(1,1000,"all")
     // Price carousel
   $(".price1-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    loop: true,
    center: true,
    dots: false,
    nav: true,
    navText : [
        '<i class="fa-solid fa-chevron-left"></i>',
        '<i class="fa-solid fa-chevron-right"></i>'
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
  }
  function doPCActions() {
    ajaxRequest(1,1000,"all")
    // Price carousel
  $(".price1-carousel").owlCarousel({
   autoplay: false,
   smartSpeed: 1000,
   loop: true,
   center: true,
   dots: false,
   nav: true,
   navText : [
       '<i class="fa-solid fa-chevron-left"></i>',
       '<i class="fa-solid fa-chevron-right"></i>'
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
 }
  function isMobile() {
    var mobileDeviceReg = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobi/i
    return mobileDeviceReg.test(navigator.userAgent) || window.innerWidth < 500
  }
  isMobile() ? doMobileActions() : doPCActions();
  

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
      autoplay: true,
      smartSpeed: 1000,
      loop: true,
      center: true,
      dots: false,
      nav: true,
      navText : [
          '<i class="fa-solid fa-chevron-left"></i>',
          '<i class="fa-solid fa-chevron-right"></i>'
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
  
  $('.owl-service-item').owlCarousel({
		items:4,
		loop:true,
		dots: true,
		nav: false,
		autoplay: true,
		margin:15,
		  responsive:{
			  0:{
				  items:1
			  },
			  600:{
				  items:2
			  },
			  1000:{
				  items:2
			  }
		  }
	  })

    // Price carousel
    $(".price-carousel").owlCarousel({
      autoplay: true,
      smartSpeed: 1500,
      margin: 45,
      dots: false,
      loop: true,
      nav : true,
      navText : [
          '<i class="fa-solid fa-arrow-left"></i>',
          '<i class="fa-solid fa-arrow-right"></i>'
      ],
      responsive: {
          0:{
              items:1
          },
          768:{
              items:2
          },
          1000:{
            items:3
          }
      }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 20) {
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
    if ($(this).scrollTop() > 20) {
        $('.back-to-top2').fadeIn('slow');
    } else {
        $('.back-to-top2').fadeOut('slow');
    }
  });

  $('.back-to-top2').click(function () {
    window.location.href = "https://lin.ee/7K12Ixj";
  });

})(jQuery);
