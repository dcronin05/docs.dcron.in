document$.subscribe(function() {
  let button = document.getElementsByClassName("md-button-copy-template-content")[0]
  let text = document.getElementById('emailSubject').firstElementChild.childNodes[0].textContent;

  if(button) {
    button.addEventListener("click", function(event) {
        navigator.clipboard.writeText(text);
        console.log(text);
        event.preventDefault()
    })
  }
})
