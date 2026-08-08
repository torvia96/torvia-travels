const WHATSAPP = "919008522092";
const PHONE = "tel:+919008522092";

const baseMessage = "Hello Torvia Travels, I would like to enquire about a cab/travel booking.";

document.querySelectorAll("[data-whatsapp]").forEach(link => {
  link.href = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(baseMessage)}`;
});

document.querySelectorAll("[data-call]").forEach(link => {
  link.href = PHONE;
});

document.getElementById("year").textContent = new Date().getFullYear();

const menuToggle = document.querySelector(".menu-toggle");
const nav = document.getElementById("nav");
menuToggle.addEventListener("click", () => nav.classList.toggle("open"));
nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => nav.classList.remove("open")));

const dateInput = document.querySelector('input[name="date"]');
dateInput.min = new Date().toISOString().split("T")[0];

document.getElementById("bookingForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const data = new FormData(this);
  const message = [
    "Hello Torvia Travels, I would like to book/enquire about a trip.",
    "",
    `Name: ${data.get("name")}`,
    `WhatsApp Number: ${data.get("phone")}`,
    `Pickup: ${data.get("pickup")}`,
    `Drop: ${data.get("drop")}`,
    `Travel Date: ${data.get("date")}`,
    `Passengers: ${data.get("passengers")}`,
    `Trip Type: ${data.get("trip")}`,
    `Additional Requirements: ${data.get("notes") || "None"}`,
    "",
    "Please share availability and pricing. Thank you."
  ].join("\n");

  const url = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(message)}`;
  const status = document.getElementById("formStatus");
  status.textContent = "Opening WhatsApp with your booking details...";
  window.open(url, "_blank", "noopener,noreferrer");
});
