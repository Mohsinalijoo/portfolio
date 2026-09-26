/* =========================================
   CUSTOM DELAYED CURSOR
========================================= */

const cursor = document.getElementById("cursor");
const cursorDot = document.getElementById("cursor-dot");

let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;

let cursorX = mouseX;
let cursorY = mouseY;


// Track actual mouse
document.addEventListener("mousemove", (event) => {
    mouseX = event.clientX;
    mouseY = event.clientY;

    // Small dot follows instantly
    cursorDot.style.left = `${mouseX}px`;
    cursorDot.style.top = `${mouseY}px`;
});


// Large circle follows with delay
function animateCursor() {

    cursorX += (mouseX - cursorX) * 0.11;
    cursorY += (mouseY - cursorY) * 0.11;

    cursor.style.left = `${cursorX}px`;
    cursor.style.top = `${cursorY}px`;

    requestAnimationFrame(animateCursor);
}

animateCursor();


// Make cursor larger over interactive items
const interactiveItems =
    document.querySelectorAll(".interactive");

interactiveItems.forEach((item) => {

    item.addEventListener("mouseenter", () => {
        document.body.classList.add("cursor-hover");
    });

    item.addEventListener("mouseleave", () => {
        document.body.classList.remove("cursor-hover");
    });

});


/* =========================================
   PANELS
========================================= */

const panelButtons =
    document.querySelectorAll("[data-panel]");

panelButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const panelId =
            button.getAttribute("data-panel");

        const selectedPanel =
            document.getElementById(panelId);

        // Close other panels
        document
            .querySelectorAll(".panel")
            .forEach((panel) => {

                if (panel !== selectedPanel) {
                    panel.classList.remove("active");
                }

            });


        selectedPanel.classList.toggle("active");


        if (selectedPanel.classList.contains("active")) {
            setTimeout(() => {

                selectedPanel.scrollIntoView({
                    behavior: "smooth",
                    block: "nearest"
                });

            }, 100);
        }

    });

});


/* =========================================
   CLOSE PANEL
========================================= */

const closeButtons =
    document.querySelectorAll("[data-close]");

closeButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const panelId =
            button.getAttribute("data-close");

        document
            .getElementById(panelId)
            .classList.remove("active");

    });

});


/* =========================================
   CLOCK
========================================= */

function updateClock() {

    const now = new Date();

    const time = now.toLocaleTimeString(
        "en-US",
        {
            hour12: false
        }
    );

    document.getElementById("clock").textContent = time;
}

updateClock();

setInterval(updateClock, 1000);


/* =========================================
   YEAR
========================================= */

document.getElementById("year").textContent =
    new Date().getFullYear();


/* =========================================
   KEYBOARD SHORTCUTS
========================================= */

document.addEventListener("keydown", (event) => {

    // ESC closes panels
    if (event.key === "Escape") {

        document
            .querySelectorAll(".panel")
            .forEach((panel) => {
                panel.classList.remove("active");
            });
    }

});