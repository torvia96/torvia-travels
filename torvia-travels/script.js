/* =========================================================
   TORVIA TRAVELS
   CINEMATIC WEBSITE JAVASCRIPT
========================================================= */


/* =========================================================
   CONTACT SETTINGS
========================================================= */

const WHATSAPP = "919008522092";

const PHONE = "tel:+919008522092";

const BASE_MESSAGE =
    "Hello Torvia Travels, I would like to enquire about a cab/travel booking.";



/* =========================================================
   PAGE LOADER
========================================================= */

window.addEventListener("load", () => {

    const loader = document.getElementById("loader");

    setTimeout(() => {

        loader.classList.add("hidden");

        document.body.classList.remove("loading");

    }, 1400);

});


document.body.classList.add("loading");



/* =========================================================
   WHATSAPP LINKS
========================================================= */

document.querySelectorAll("[data-whatsapp]").forEach(link => {

    link.href =
        `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(BASE_MESSAGE)}`;

    link.target = "_blank";

    link.rel = "noopener noreferrer";

});



/* =========================================================
   CALL LINKS
========================================================= */

document.querySelectorAll("[data-call]").forEach(link => {

    link.href = PHONE;

});



/* =========================================================
   CURRENT YEAR
========================================================= */

const yearElement = document.getElementById("year");

if (yearElement) {

    yearElement.textContent =
        new Date().getFullYear();

}



/* =========================================================
   NAVBAR SCROLL EFFECT
========================================================= */

const navbar = document.getElementById("navbar");

function updateNavbar() {

    if (window.scrollY > 40) {

        navbar.classList.add("scrolled");

    } else {

        navbar.classList.remove("scrolled");

    }

}

window.addEventListener("scroll", updateNavbar);

updateNavbar();



/* =========================================================
   MOBILE MENU
========================================================= */

const menuToggle =
    document.getElementById("menuToggle");

const nav =
    document.getElementById("nav");


function setMenu(open) {

    nav.classList.toggle("open", open);

    menuToggle.setAttribute(
        "aria-expanded",
        String(open)
    );

}


menuToggle.addEventListener("click", () => {

    const isOpen =
        nav.classList.contains("open");

    setMenu(!isOpen);

});


nav.querySelectorAll("a").forEach(link => {

    link.addEventListener("click", () => {

        setMenu(false);

    });

});



/* =========================================================
   CINEMATIC SCROLL REVEALS
========================================================= */

const revealElements =
    document.querySelectorAll(".reveal");


const revealObserver =
    new IntersectionObserver(

        entries => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("visible");

                    revealObserver.unobserve(
                        entry.target
                    );

                }

            });

        },

        {
            threshold: 0.12
        }

    );


revealElements.forEach(element => {

    revealObserver.observe(element);

});



/* =========================================================
   HERO PARALLAX
========================================================= */

const heroPhoto =
    document.querySelector(".hero-photo");


window.addEventListener("scroll", () => {

    if (!heroPhoto) return;

    const scroll =
        window.scrollY;

    if (scroll < window.innerHeight) {

        heroPhoto.style.transform =
            `scale(1) translateY(${scroll * 0.12}px)`;

    }

});



/* =========================================================
   TRAVEL DATE
========================================================= */

const dateInput =
    document.querySelector('input[name="date"]');


if (dateInput) {

    const today =
        new Date();

    const year =
        today.getFullYear();

    const month =
        String(today.getMonth() + 1)
        .padStart(2, "0");

    const day =
        String(today.getDate())
        .padStart(2, "0");

    dateInput.min =
        `${year}-${month}-${day}`;

}



/* =========================================================
   CAB SELECTION
========================================================= */

const cabRadios =
    document.querySelectorAll(
        'input[name="fleetChoice"]'
    );


const vehicleSelect =
    document.getElementById(
        "vehicleSelect"
    );


const fleetNote =
    document.getElementById(
        "fleetNote"
    );


function showCabChoice(value) {

    document
        .querySelectorAll(".fleet-card")
        .forEach(card => {

            const radio =
                card.querySelector(
                    'input[name="fleetChoice"]'
                );

            card.classList.toggle(
                "is-selected",
                radio && radio.checked
            );

        });


    if (value) {

        fleetNote.textContent =
            `Selected: ${value}. It is filled into the booking form below.`;

        fleetNote.classList.add("chosen");

    } else {

        fleetNote.textContent =
            "No vehicle selected yet. Your choice will appear in the booking form below.";

        fleetNote.classList.remove("chosen");

    }

}


cabRadios.forEach(radio => {

    radio.addEventListener(
        "change",
        () => {

            vehicleSelect.value =
                radio.value;

            showCabChoice(
                radio.value
            );

            document
                .getElementById("booking")
                .scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

        }
    );

});



/* =========================================================
   CAB SELECT FROM FORM
========================================================= */

vehicleSelect.addEventListener(
    "change",
    () => {

        cabRadios.forEach(radio => {

            radio.checked =
                radio.value ===
                vehicleSelect.value;

        });


        showCabChoice(
            vehicleSelect.value
        );

    }
);



/* =========================================================
   COORG PLACES
========================================================= */

const placeCards =
    document.querySelectorAll(
        ".place-card"
    );


const stopsList =
    document.getElementById(
        "stopsList"
    );


const stopsInput =
    document.getElementById(
        "stopsInput"
    );


const clearStops =
    document.getElementById(
        "clearStops"
    );


const stops =
    new Set();



/* =========================================================
   RENDER STOPS
========================================================= */

function renderStops() {

    stopsInput.value =
        [...stops].join(", ");


    clearStops.hidden =
        stops.size === 0;


    stopsList.innerHTML = "";


    if (stops.size === 0) {

        const empty =
            document.createElement(
                "span"
            );

        empty.className =
            "stops-empty";

        empty.textContent =
            "None yet. Tap places in the Coorg Places section above.";

        stopsList.appendChild(
            empty
        );

        return;

    }


    stops.forEach(name => {

        const chip =
            document.createElement(
                "span"
            );

        chip.className =
            "chip";

        chip.appendChild(
            document.createTextNode(
                name
            )
        );


        const remove =
            document.createElement(
                "button"
            );

        remove.type =
            "button";

        remove.textContent =
            "×";

        remove.setAttribute(
            "aria-label",
            `Remove ${name}`
        );


        remove.addEventListener(
            "click",
            event => {

                event.stopPropagation();

                toggleStop(
                    name,
                    false
                );

            }
        );


        chip.appendChild(
            remove
        );


        stopsList.appendChild(
            chip
        );

    });

}



/* =========================================================
   TOGGLE STOP
========================================================= */

function toggleStop(name, add) {

    if (add) {

        stops.add(name);

    } else {

        stops.delete(name);

    }


    placeCards.forEach(card => {

        if (
            card.dataset.place === name
        ) {

            card.setAttribute(
                "aria-pressed",
                String(add)
            );


            const label =
                card.querySelector(
                    ".add-label"
                );


            if (label) {

                label.textContent =
                    add
                        ? "Added to trip"
                        : "Add to trip";

            }

        }

    });


    renderStops();

}



/* =========================================================
   PLACE CLICK
========================================================= */

placeCards.forEach(card => {

    card.addEventListener(
        "click",
        () => {

            const name =
                card.dataset.place;

            const currentlySelected =
                card.getAttribute(
                    "aria-pressed"
                ) === "true";


            toggleStop(
                name,
                !currentlySelected
            );

        }
    );

});



/* =========================================================
   CLEAR ALL STOPS
========================================================= */

clearStops.addEventListener(
    "click",
    () => {

        [...stops].forEach(
            name => toggleStop(
                name,
                false
            )
        );

    }
);


renderStops();



/* =========================================================
   BOOKING FORM
========================================================= */

const bookingForm =
    document.getElementById(
        "bookingForm"
    );


bookingForm.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();


        const data =
            new FormData(this);


        const name =
            data.get("name");


        const phone =
            data.get("phone");


        const pickup =
            data.get("pickup");


        const drop =
            data.get("drop");


        const date =
            data.get("date");


        const passengers =
            data.get("passengers");


        const trip =
            data.get("trip");


        const vehicle =
            data.get("vehicle");


        const selectedStops =
            data.get("stops");


        const notes =
            data.get("notes");



        const message = [

            "Hello Torvia Travels, I would like to book/enquire about a trip.",

            "",

            `Name: ${name}`,

            `WhatsApp Number: ${phone}`,

            `Pickup: ${pickup}`,

            `Drop: ${drop}`,

            `Travel Date: ${date}`,

            `Passengers: ${passengers}`,

            `Trip Type: ${trip}`,

            `Cab Type: ${
                vehicle ||
                "Not decided, please suggest"
            }`,

            `Sightseeing Stops: ${
                selectedStops ||
                "Not decided yet"
            }`,

            `Additional Requirements: ${
                notes ||
                "None"
            }`,

            "",

            "Please share availability and pricing. Thank you."

        ].join("\n");



        const whatsappURL =
            `https://wa.me/${WHATSAPP}?text=${
                encodeURIComponent(message)
            }`;



        const status =
            document.getElementById(
                "formStatus"
            );


        status.textContent =
            "Opening WhatsApp with your booking details...";



        window.open(
            whatsappURL,
            "_blank",
            "noopener,noreferrer"
        );

    }
);



/* =========================================================
   BACK TO TOP
========================================================= */

const backTop =
    document.getElementById(
        "backTop"
    );


window.addEventListener(
    "scroll",
    () => {

        if (window.scrollY > 700) {

            backTop.classList.add(
                "show"
            );

        } else {

            backTop.classList.remove(
                "show"
            );

        }

    }
);


backTop.addEventListener(
    "click",
    () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    }
);



/* =========================================================
   IMAGE ERROR HANDLING
========================================================= */

document
    .querySelectorAll("img")
    .forEach(image => {

        image.addEventListener(
            "error",
            () => {

                image.classList.add(
                    "image-missing"
                );

            }
        );

    });



/* =========================================================
   MOUSE PARALLAX ON DESKTOP
========================================================= */

if (
    window.matchMedia(
        "(pointer:fine)"
    ).matches
) {

    const hero =
        document.querySelector(
            ".hero"
        );


    hero.addEventListener(
        "mousemove",
        event => {

            const x =
                (event.clientX /
                    window.innerWidth -
                    .5) * 10;


            const y =
                (event.clientY /
                    window.innerHeight -
                    .5) * 6;


            if (heroPhoto) {

                heroPhoto.style.transform =
                    `scale(1.03) translate(${x}px, ${y}px)`;

            }

        }
    );


    hero.addEventListener(
        "mouseleave",
        () => {

            if (heroPhoto) {

                heroPhoto.style.transform =
                    "scale(1.03)";

            }

        }
    );

}