// When the user clicks on <span> (x), close the modal
document.querySelectorAll('.close').forEach(function(closeButton) {
  closeButton.addEventListener('click', function(event) {
    event.stopPropagation();
    this.parentElement.parentElement.style.display = "none";
  });
});

// When the user clicks anywhere outside of the modal content, close the modal
document.querySelectorAll('.modal').forEach(function(modal) {
  modal.addEventListener('click', function(event) {
    if (event.target === this) {
      this.style.display = "none";
    }
  });
});

// When the user clicks on the modal content, stop the event propagation
document.querySelectorAll('.modal-content').forEach(function(modalContent) {
  modalContent.addEventListener('click', function(event) {
    event.stopPropagation();
  });
});

function closeModal(modalId) {
  var modal = document.getElementById(modalId);
  modal.style.display = "none";
}

function openModal(modalId, imageUrl, title, event) {
  // Stop event propagation
  if (event) {
    event.stopPropagation();
  }

  // Close all other modals
  document.querySelectorAll('.modal').forEach(function(modal) {
    modal.style.display = "none";
  });

  // Now open the requested modal
  var modal = document.getElementById(modalId);
  var modalImage = modal.querySelector("#modalImage" + modalId.replace('myModal', ''));
  var modalTitle = modal.querySelector("#modalTitle" + modalId.replace('myModal', ''));
  modal.style.display = "block";
  modalImage.src = imageUrl;
  modalTitle.innerHTML = title;
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (!event.target.closest('.modal-content')) {
    document.querySelectorAll('.modal').forEach(function(modal) {
      if (modal.style.display === "block") {
        modal.style.display = "none";
      }
    });
  }
}

const btn = document.querySelector(".btn-toggle");
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
  document.body.classList.toggle("dark-theme");
} else if (currentTheme == "light") {
  document.body.classList.toggle("light-theme");
}

btn.addEventListener("click", function () {
  if (prefersDarkScheme.matches) {
    document.body.classList.toggle("light-theme");
    var theme = document.body.classList.contains("light-theme")
      ? "light"
      : "dark";
  } else {
    document.body.classList.toggle("dark-theme");
    var theme = document.body.classList.contains("dark-theme")
      ? "dark"
      : "light";
  }
  localStorage.setItem("theme", theme);
});
