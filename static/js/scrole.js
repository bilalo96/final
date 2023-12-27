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

// Initially adjust the button position
adjustButtonPosition();

// Listen for window resize events and adjust the button position
window.addEventListener('resize', adjustButtonPosition);