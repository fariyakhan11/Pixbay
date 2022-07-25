


//========= typing animation ========

var typed = new Typed(".typing", {
    strings: ["Sharpen", "Contrast", "Bright", "Saturate", "Blur","Sketch","Dull", "GreyScale","Colorize","Transpose", "Scale", "Mirror", "Contrast","ShearX","ShearY"],
    typeSpeed: 100,
    BackSpeed: 60,
    loop: true
})

const navTogglerBtn = document.querySelector(".nav-toggler"),
    aside = document.querySelector(".aside");
navTogglerBtn.addEventListener("click", () => {
    asideSectionTogglerBtn();

})
function asideSectionTogglerBtn() {
    aside.classList.toggle("open");
    navTogglerBtn.classList.toggle("open");
    // for (let i=0; i<totalSection; i++) {
    //     allSection[i].classList.toggle("open")
    // }
}

// if (window.innerWidth< 1200)
//     {
//         asideSectionTogglerBtn();
//     }

let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo-header');
let logoSpan = document.querySelectorAll('.logo');

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.add('active');
            }, (idx + 1) * 400)
        });
        setTimeout(() => {
            logoSpan.forEach((span, idx) => {
                setTimeout(() => {
                    span.classList.remove('active');
                    span.classList.add('active');
                }, (idx + 1) * 50)
            })
        }, 2000);
        setTimeout(() => {
            intro.style.top = '-100vh';
        }, 2300)
    })
})

