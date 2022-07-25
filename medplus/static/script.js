function search() {
    let input, filter, ul, li, a, textValue, inputValue;
    input = document.getElementById("search-input");
    filter = input.value.toUpperCase();
    ul = document.getElementById("elements");
    li = ul.getElementsByTagName("li");
    ul.style.display = 'block'; // Starts being hidden, show it now
    inputValue = input.value;

    if (!inputValue.match(/\S/)) { // If input empty again, hide all search results again
        ul.style.display = 'none';
    }

    for (let i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        textValue = a.textContent || a.innerText;
        if (textValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}