console.log("Mini Amazon loaded!"); 

function filterByCategory(cat) {
    if (cat) {
        window.location.href = `/?category=${cat}`;
    } else {
        window.location.href = '/'; 
    }
}