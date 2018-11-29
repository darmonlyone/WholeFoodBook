var btnContainer = document.getElementById("category-button");
var btns = btnContainer.getElementsByClassName("btncat");
var filterbut = $('.check:checked');
var hidden = document.getElementsByClassName('unselected');
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("actived");
    current[0].className = current[0].className.replace(" actived", "");
    this.className += " actived";
    if (filterbut.length > 0 ) {
      for (var j =0 ; j < filterbut.length ; j ++ ) {
        filterbut[j].checked = false;
      }
    } 
    for (var i = 0; i < hidden.length; i++) {
        hidden[i].classList.remove("unselected");
    }
  });
}