/* ------------------------------------------------------------------
   Torvia Travels - booking, cab selection and Coorg stop picker
   Change the two numbers below if the contact number ever changes.
------------------------------------------------------------------- */
const WHATSAPP = "919008522092";          // country code + number, no plus sign
const PHONE = "tel:+919008522092";

const baseMessage = "Hello Torvia Travels, I would like to enquire about a cab/travel booking.";

/* ---------------------------------------------- contact links + year */
document.querySelectorAll("[data-whatsapp]").forEach(link => {
  link.href = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(baseMessage)}`;
  link.target = "_blank";
  link.rel = "noopener";
});

document.querySelectorAll("[data-call]").forEach(link => {
  link.href = PHONE;
});

document.getElementById("year").textContent = new Date().getFullYear();

/* ------------------------------------------------------ mobile menu */
const menuToggle = document.querySelector(".menu-toggle");
const nav = document.getElementById("nav");

function setMenu(open) {
  nav.classList.toggle("open", open);
  menuToggle.setAttribute("aria-expanded", String(open));
}

menuToggle.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => setMenu(false)));

/* --------------------------------------------------- travel date min */
const dateInput = document.querySelector('input[name="date"]');
dateInput.min = new Date().toISOString().split("T")[0];

/* ------------------------------------------- cab (vehicle) selection */
const cabRadios = document.querySelectorAll('input[name="fleetChoice"]');
const vehicleSelect = document.getElementById("vehicleSelect");
const fleetNote = document.getElementById("fleetNote");

function showCabChoice(value) {
  document.querySelectorAll(".cab-card").forEach(card => {
    card.classList.toggle("is-selected", card.querySelector("input").checked);
  });
  if (value) {
    fleetNote.textContent = `Selected: ${value}. It is filled into the booking form below.`;
    fleetNote.classList.add("chosen");
  } else {
    fleetNote.textContent = "No vehicle selected yet. Your choice will appear in the booking form below.";
    fleetNote.classList.remove("chosen");
  }
}

cabRadios.forEach(radio => {
  radio.addEventListener("change", () => {
    vehicleSelect.value = radio.value;
    showCabChoice(radio.value);
  });
});

// picking the cab inside the form keeps the cards in sync
vehicleSelect.addEventListener("change", () => {
  cabRadios.forEach(radio => { radio.checked = radio.value === vehicleSelect.value; });
  showCabChoice(vehicleSelect.value);
});

/* -------------------------------------------- Coorg stops selection */
const placeCards = document.querySelectorAll(".place-card");
const stopsList = document.getElementById("stopsList");
const stopsInput = document.getElementById("stopsInput");
const clearStops = document.getElementById("clearStops");
const stops = new Set();

function renderStops() {
  stopsInput.value = [...stops].join(", ");
  clearStops.hidden = stops.size === 0;
  stopsList.textContent = "";

  if (stops.size === 0) {
    const empty = document.createElement("span");
    empty.className = "stops-empty";
    empty.textContent = "None yet. Tap places in the Coorg Places section above.";
    stopsList.appendChild(empty);
    return;
  }

  stops.forEach(name => {
    const chip = document.createElement("span");
    chip.className = "chip";
    chip.textContent = name;

    const remove = document.createElement("button");
    remove.type = "button";
    remove.setAttribute("aria-label", `Remove ${name}`);
    remove.textContent = "\u00d7";
    remove.addEventListener("click", () => toggleStop(name, false));

    chip.appendChild(remove);
    stopsList.appendChild(chip);
  });
}

function toggleStop(name, add) {
  if (add) stops.add(name); else stops.delete(name);

  placeCards.forEach(card => {
    if (card.dataset.place === name) {
      card.setAttribute("aria-pressed", String(add));
      card.querySelector(".add-label").textContent = add ? "Added to trip" : "Add to trip";
    }
  });
  renderStops();
}

placeCards.forEach(card => {
  card.addEventListener("click", () => {
    const name = card.dataset.place;
    toggleStop(name, card.getAttribute("aria-pressed") !== "true");
  });
});

clearStops.addEventListener("click", () => {
  [...stops].forEach(name => toggleStop(name, false));
});

renderStops();

/* ------------------------------------------------ booking form send */
document.getElementById("bookingForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const data = new FormData(this);

  const lines = [
    "Hello Torvia Travels, I would like to book/enquire about a trip.",
    "",
    `Name: ${data.get("name")}`,
    `WhatsApp Number: ${data.get("phone")}`,
    `Pickup: ${data.get("pickup")}`,
    `Drop: ${data.get("drop")}`,
    `Travel Date: ${data.get("date")}`,
    `Passengers: ${data.get("passengers")}`,
    `Trip Type: ${data.get("trip")}`,
    `Cab Type: ${data.get("vehicle") || "Not decided, please suggest"}`,
    `Sightseeing Stops: ${data.get("stops") || "Not decided yet"}`,
    `Additional Requirements: ${data.get("notes") || "None"}`,
    "",
    "Please share availability and pricing. Thank you."
  ];

  const url = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(lines.join("\n"))}`;
  const status = document.getElementById("formStatus");
  status.textContent = "Opening WhatsApp with your booking details...";
  window.open(url, "_blank", "noopener,noreferrer");
});
