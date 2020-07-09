// JavaScript Document
function prepareMenuForDesktop() {
			"use strict";

            var navbarHeight = 0;
            
            // For screens greater than 767
            if($(window).width() > 767) {

                // target at which the menu bar changes to sticky
                var target = $("#tm-section-1").offset().top - 100;

                // window scroll
				$(document).ready(function() {
                $(window).scroll(function(){

                    if($(this).scrollTop() > target) {                            
						$(".tm-navbar-row").addClass("sticky");
						$(".dropdown-content a").addClass("sticky");
						$(".dropdown-content a:hover").addClass("sticky");
                    }
                    else {
                        $(".tm-navbar-row").removeClass("sticky");
						$(".dropdown-content a").removeClass("sticky");
						$(".dropdown-content a:hover").removeClass("sticky");
                    }     

                }); 
			});
                navbarHeight = 56;
            }

            // Single Page Nav
/*            $('#tmNavbar').singlePageNav({
               'currentClass' : "active",
                offset : navbarHeight,
                'filter': ':not(.external)'
            });  *//*链接失效*/
        }  
   
        $(document).ready(function(){
			"use strict";

            prepareMenuForDesktop();

            // On window resize, prepare menu
            $(window).resize(function(){
                prepareMenuForDesktop();                 
                                  
            });       
        });
