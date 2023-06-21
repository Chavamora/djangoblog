document.getElementById("filter-favoritos").addEventListener("click", function () {
    // Realiza la solicitud AJAX para obtener los elementos favoritos
    
    
    filterActive = this.classList.contains("filter_active");
    var item = document.querySelector(".item")
    var hasFavorite = item.querySelector(".favorite");

    if(filterActive) {
        //desactivar filtro
        this.classList.remove("filter_active");
        if(!hasFavorite)
            item.style.visibility = "visible";

    } else {
        //activar filtro
        this.classList.add("filter_active");
        if(!hasFavorite)
            item.style.visibility = "hidden";
        

    }


   
});
