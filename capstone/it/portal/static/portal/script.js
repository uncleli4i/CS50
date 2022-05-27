document.addEventListener('DOMContentLoaded', function() {


// Show/hide Add New Computer block
add_comp = document.querySelector('.add_comp');
add_comp.addEventListener("click", () => {
    show_form = document.querySelector('.add_comp_form');
    if(show_form.style.display == 'block') show_form.style.display = 'none'
    else show_form.style.display = 'block';
})


// Live Search Computers

search_button = document.querySelector('#comp_search');
search_button.addEventListener('keyup', () =>{
    comp_row = document.querySelectorAll('#comp_row');
    
    comp_row.forEach(element => {
        let search_str = new Array();
        comp_item = Array.from(element.children);
        comp_item.forEach(element => {
            
            search_str.push(element.innerText.toLowerCase());
           
        });
        
        res = find(search_str,search_button.value.toLowerCase());
        if(res.length >0) element.style.display = "flex"
        else element.style.display = "none";
     }); 
});
});


// Function find str in array
function find(arr, find) {
    return arr.filter(function (value) {
        return (value + "").indexOf(find) != -1;
    });
}
