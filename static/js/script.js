// When the user clicks on <span> (x), close the modal
document.querySelectorAll('.close').forEach(function(closeButton) {
  closeButton.addEventListener('click', function() {
    this.parentElement.parentElement.style.display = "none";
  });
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target.classList.contains('modal')) {
    event.target.style.display = "none";
  }
}



function closeModal(modalId) {
  var modal = document.getElementById(modalId);
  modal.style.display = "none";
}


function openModal(modalId, imageUrl, title) {
  var modal = document.getElementById(modalId);
  var modalImage = modal.querySelector("#modalImage" + modalId.replace('myModal', ''));
  var modalTitle = modal.querySelector("#modalTitle" + modalId.replace('myModal', ''));
  modal.style.display = "block";
  modalImage.src = imageUrl;
  modalTitle.innerHTML = title;
}

legacyShowCookieBar({
  content: '<div class="cookie-bar"> <p>We use cookies to improve your browsing experience. By continuing to use our site, you agree to our use of cookies.</p> <a href="/accept_cookies" class="cc-cookie-accept">Accept</a> <a href="/decline_cookies" class="cc-cookie-decline">Decline</a> </div>',
  cookie_groups: ['analytics'],
  cookie_decline: '{% get_decline_cookie_groups_cookie_string request analytics %}',
  beforeDeclined: function () {
    console.log('User is about to decline cookies');
  },
});