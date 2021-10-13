function myFunction() {
    var x = document.getElementById("navbar");
    if (x.className === "right_nav") {
      x.className += " responsive";
    } else {
      x.className = "right_nav";
    }
  }