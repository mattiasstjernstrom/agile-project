const newsletterBox = document.getElementById("newsletter");
const form = document.getElementById("newsletter-form");
const newsletterEmail = document.getElementById("newsletter_email");
const btn = form.querySelector("button");
const errorMsg = document.getElementById("error-msg");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const newsletterForm = new FormData(form);

  fetch("/newsletter", {
    method: "POST",
    body: newsletterForm,
  })
    .then(async response => {
      btn.disabled = true;
      btn.innerHTML = `<i class="fa fa-envelope"></i> Signing up...`;

      if (response.status === 400) {
        errorMsg.innerHTML = "Incorrect email-format!";
        newsletterEmail.style.border = "1px solid red";
        throw new Error("Incorrect input!");
        console.log("Incorrect input!");
      } else if (response.status === 409) {
        errorMsg.innerHTML =
          newsletterEmail.value + "  is already subscribed to our newsletter!";
        newsletterEmail.style.border = "1px solid red";
        throw new Error("Email already exists!");
        console.log("Email already exists!");
      } else if (response.status === 405) {
        throw new Error("Method Not Allowed!");
        console.log("Method Not Allowed!");
      } else if (!response.ok) {
        throw new Error("Network response was not ok!");
      } else if (response.status === 200) {
        console.log("You have successfully subscribed to our newsletter!");
      }
      return response.json();
    })
    .then(data => {
      btn.innerHTML = `<i class="fa fa-envelope"></i> Subscribe`;
      btn.disabled = false;
      newsletterModal();
    })
    .catch(error => {
      console.error("Error:", error);
      btn.innerHTML = `<i class="fa fa-envelope"></i> Subscribe`;
      btn.disabled = false;
    });
});

function newsletterModal() {
  $("#newsletterModalPopup").modal({ show: true });
  const modalText = document.getElementById("newsletterModalPopupText");
  modalText.innerHTML = `Your email <strong>${newsletterEmail.value}</strong> has been successfully subscribed to our newsletter!`;
  newsletterBox.style.display = "none";
}
