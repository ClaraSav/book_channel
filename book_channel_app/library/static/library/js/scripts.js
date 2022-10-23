// Render the first element
const formats = document.querySelectorAll('.links_download li');
formats[0].classList.add('select');

var link_info = document.getElementsByClassName(formats[0].id);
link_info[0].classList.remove('deactive');

// cahnge width click
formats.forEach((li) => {
    li.addEventListener('click', ()=> {
        formats.forEach((li) => {
            var info = document.getElementsByClassName(li.id);
            info[0].classList.add('deactive');
            li.classList.remove('select');
        })
        li.classList.add('select');
        link_info = document.getElementsByClassName(li.id);
        link_info[0].classList.remove('deactive');
    })
})