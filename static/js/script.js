$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    $(window).scroll(function () {     
        if (this.scrollY > 500) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: -200,
        loop: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            }, 
            600:{
                items: 2,
                nav: false
            }, 
            1000:{
                items: 3,
                nav: false
            } 
        }

    }); 

    // scroll up btn function 
    $('.scroll-up-btn').click(function () {
        $('html').animate({
            scrollTop: 0
        });
    });

    // Add smooth scrolling to all links
    $("a").on('click', function (event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });

    // form input validation 
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on(
            "focusin", function () {
            $(this).parent(".select-wrapper").on(
                "change", function () {
                if ($(this).children("ul").children(
                    "li.selected:not(.disabled)").on(
                        "click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children(
                "li.selected:not(.disabled)").css(
                    "background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children(
                    "input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on(
                    "focusout", function () {
                    if ($(this).parent(".select-wrapper").children(
                        "select").prop("required")) {
                        if ($(this).css(
                            "border-bottom") !== "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children(
                                "input").css(classInvalid);
                        }
                    }
                });
            }  
        });
    }
});

 // sticky header 
 window.onscroll = function () {
    myFunction();
};

let header = document.getElementById("myHeader");
let sticky = header.offsetTop;

function myFunction() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

// read more function from w3school.com 
function toggleText() {
    let dots = document.getElementById("dots");
    let moreText = document.getElementById("more");
    let btnText = document.getElementById("toggleBtn");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}
