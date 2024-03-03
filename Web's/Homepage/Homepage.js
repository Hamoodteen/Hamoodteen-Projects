let box = document.querySelector(".plus");
let addE = document.querySelector(".add");
let closeBox = document.querySelector(".close");

addE.addEventListener("click", () => {
    box.style.display = "block";
});

closeBox.addEventListener("click", () => {
    box.style.display = "none";
});

function template(url, name, title, urlclass) {
    let crd = document.createElement('a');
    crd.href = url;
    crd.target = "_blank";
    crd.title = title;

    let img = document.createElement('img');
    img.src = `${url}/favicon.ico`;
    img.alt = name;
    crd.appendChild(img);

    crd.style.margin = "9.875px";
    
    let nameNode = document.createTextNode(name);
    crd.appendChild(nameNode);

    let target = document.querySelector(`.url${urlclass}`);
    target.appendChild(crd);
}

let urlInput = document.querySelector('input[type="url"]');
let nameInput = document.querySelectorAll('input[type="text"]')[0];
let titleInput = document.querySelectorAll('input[type="text"]')[1];
let btn = document.querySelector("button");

function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
}

btn.addEventListener("click", () => {
    if (isValidURL(urlInput.value)) {
        let selection = document.querySelectorAll("option");
        let correct = undefined;

        for (let i = 0; i < selection.length; i++) {
            if (selection[i].selected === true) {
                correct = i + 1;
                break;
            }
        }

        template(urlInput.value, nameInput.value, titleInput.value, correct);

        let stored = JSON.parse(localStorage.getItem("Websites")) || {};
        stored[`url${correct}`] = stored[`url${correct}`] || [];
        stored[`url${correct}`].push({ name: nameInput.value, url: urlInput.value, title: titleInput.value });
        localStorage.setItem("Websites", JSON.stringify(stored));

        alert("تمت الإضافة بنجاح");
        box.style.display = "none";
    } else {
        alert("رجاء أدخل موقع ويب صحيح");
    }
});

document.addEventListener("DOMContentLoaded", () => {
    let retrieve = JSON.parse(localStorage.getItem("Websites")) || {};

    for (let i = 0; i < 7; i++) {
        let urlNow = retrieve[`url${i + 1}`] || [];
        
        for (const urlData of urlNow) {
            template(urlData.url, urlData.name, urlData.title, i + 1);
        }
    }
});
