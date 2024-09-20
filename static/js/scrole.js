function adjustButtonPosition() {
    const fixedButtons = document.querySelector('.fixed-booking-buttons');
    if (window.innerWidth <= 768) {
        // Adjust the button position for smaller screens
        fixedButtons.style.left = '10px';
        fixedButtons.style.transform = 'none';
    } else {
        // Reset the button position for larger screens
        fixedButtons.style.left = '50%';
        fixedButtons.style.transform = 'translateX(-50%)';
    }
}

function enableScrollWithinDiv() {
    document.querySelector('.custom-scroll').addEventListener('wheel', function(e) {
        const delta = e.deltaY || e.detail || e.wheelDelta;

        // Check if scrolling reaches the top or bottom of the div
        const isAtTop = this.scrollTop === 0;
        const isAtBottom = this.scrollHeight - this.clientHeight <= this.scrollTop;

        // Prevent the page scroll if scrolling inside the div
        if ((delta < 0 && !isAtTop) || (delta > 0 && !isAtBottom)) {
            e.preventDefault();
            this.scrollTop += delta * 2; // Adjust the scroll speed
        }
    });
}

// Initially adjust the button position and enable scroll within the div
adjustButtonPosition();
enableScrollWithinDiv();

// Listen for window resize events and adjust the button position
window.addEventListener('resize', () => {
    adjustButtonPosition();
    // Additionally, you might need to re-enable scroll within the div based on your layout
    enableScrollWithinDiv();
});
function enableScrollWithinDiv() {
    const scrollableDiv = document.querySelector('.custom-scroll');

    scrollableDiv.addEventListener('wheel', function(e) {
        const delta = e.deltaY || e.detail || e.wheelDelta;

        const isAtTop = this.scrollTop === 0;
        const isAtBottom = this.scrollHeight - this.clientHeight <= this.scrollTop;

        // Allow vertical scrolling only if not at the top or bottom of the div
        if ((delta < 0 && !isAtTop) || (delta > 0 && !isAtBottom)) {
            e.preventDefault();
            this.scrollTop += delta * 2; // Adjust the scroll speed
        }
    });
}
function initializeSlickSlider() {
    $('.slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: false,
        variableWidth: true,
        centerMode: true,
        arrows: false,
        swipeToSlide: true
    });
}

$(document).ready(function(){
    enableScrollWithinDiv();
    initializeSlickSlider();
});