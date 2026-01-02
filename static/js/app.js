window.addEventListener('load', (event) => {
    const all_projects_dropdown_button = document.getElementsByClassName("nav-link dropdown-toggle");

    for (let i = 0; i < all_projects_dropdown_button.length; i++) {
        all_projects_dropdown_button[i].addEventListener('click', ()=>{
            (all_projects_dropdown_button[i].previousSibling.checked == true) ? all_projects_dropdown_button[i].previousSibling.checked = false : all_projects_dropdown_button[i].previousSibling.previousSibling.checked = true;
        });
    };
});


