document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("greetBtn");
    if(btn){
        btn.addEventListener("click", function() {
            alert("Hello! Thanks for visiting my page.");
        });
    }
});
