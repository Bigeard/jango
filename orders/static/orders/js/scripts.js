const input = document.getElementById('inputSearch');

const searchXML = () => {
    window.location = `/?url=${input.value}`;
}

const searchOrder = () => {
    window.location = `/orders/?search=${input.value}`;
}

input.addEventListener("keydown", (e) => {
    if (e.keyCode === 13) {
        if(window.location.pathname === '/') {
            searchXML();            
        } else {
            searchOrder();
        }
    }
});