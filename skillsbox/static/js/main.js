setTimeout(() => {
  $("#message").fadeOut("slow");
}, 3000);

var input = document.getElementById("profileImage");
var infoArea = document.getElementById("background-image-name");

input.addEventListener("change", showFileName);

function showFileName(event) {
  var input = event.srcElement;
  var fileName = input.file[0].name;
  infoArea.textContent = "File name: " + fileName;
}
