let swiper = new Swiper('.swiper1', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

});
let swiper2 = new Swiper('.swiper2', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next2',
    prevEl: '.swiper-button-prev2',
  },

});

let swiper3 = new Swiper('.swiper3', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,
  slidesPerView: 1,
  spaceBetween: 15,

  breakpoints: {
    // When window width is less than 576px (mobile)
    386: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    390: {
      slidesPerView: 2,
      spaceBetween: 0,
    },

    // When window width is between 576px and 768px (tablet)
    724: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    // When window width is greater than 768px (desktop)
    992: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1312: {
      slidesPerView: 5,
      spaceBetween: 20,
    },
  },
});


let swiper4 = new Swiper('.swiper4', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next4',
    prevEl: '.swiper-button-prev4',
  },

});

const swiperSection = document.querySelector('.swiper3');
const circleCursor = document.querySelector('.circle-cursor');
const cursorSize = 122; // Size of the circle cursor element

swiperSection.addEventListener('mousemove', (e) => {
  const x = e.clientX - cursorSize / 2 + 'px';
  const y = e.clientY - cursorSize / 2 + 'px';
  circleCursor.style.top = y;
  circleCursor.style.left = x;
  circleCursor.style.opacity = 1;
});

swiperSection.addEventListener('mouseleave', () => {
  circleCursor.style.opacity = 0;
});

swiperSection.addEventListener('mouseenter', () => {
  document.body.style.cursor = 'none'; // Hide default cursor
});

document.addEventListener('mousemove', (e) => {
  if (swiperSection.contains(e.target)) {
    document.body.style.cursor = 'none'; // Hide default cursor within swiper section
  } else {
    document.body.style.cursor = 'auto'; // Show default cursor outside swiper section
  }
});


// JavaScript
document.addEventListener('DOMContentLoaded', function() {
  var navLinks = document.querySelectorAll('nav a');
  console.log(navLinks);
  navLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      var targetId = this.getAttribute('data-id');

      var targetElement = document.getElementById(targetId);
      console.log(targetElement);
      if (targetElement) {
        // Scroll smoothly to the target section
        console.log(targetElement.offsetTop);

        window.scrollTo({
          top: targetElement.offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
});


// Get the header element
var header = document.querySelector('.subnavbar');

// Get the initial offset of the header
var headerOffsetTop = header.offsetTop;

// Function to handle scroll event
function handleScroll() {
  // Get the current scroll position
  var scrollY = window.scrollY || window.pageYOffset;

  // Check if the scroll position is greater than or equal to the initial offset of the header
  if (scrollY > headerOffsetTop) {
    // Add "fixed" class to the header
    header.classList.add('fixed');
  } else {
    header.classList.remove('fixed');
  }
}

// Add scroll event listener
window.addEventListener('scroll', handleScroll);
