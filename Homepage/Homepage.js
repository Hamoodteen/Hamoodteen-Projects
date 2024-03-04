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
    img.style.height = "85px";

    function correctURL(curl) {
        const inputString = curl;
        const letterToSplit = '/';
        const splitArray = inputString.split(letterToSplit);
        const splittedString = splitArray.slice(0, 3).join(letterToSplit);
        return splittedString;
    }
    if (url.split('').filter(char => char === '/').length >= 3) {
        img.src = `${correctURL(url)}/favicon.ico`;
    } else {
        img.src = `${url}/favicon.ico`;
    }

    img.alt = name;
    crd.appendChild(img);

    crd.style.margin = "0px 12px";

    let nameNode = document.createTextNode(name);
    crd.appendChild(nameNode);

    let target = document.querySelector(`.url${urlclass}`);
    target.appendChild(crd);
}

let urlInput = document.querySelector('input[type="url"]');
let nameInput = document.querySelectorAll('input[type="text"]')[0];
let titleInput = document.querySelectorAll('input[type="text"]')[1];
let btnSave = document.querySelector(".save");
let btnRemove = document.querySelector(".remove");

function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
}

function correctOption() {
    let selection = document.querySelectorAll("option");
    let correctVal = undefined;

    for (let i = 0; i < selection.length; i++) {
        if (selection[i].selected === true) {
            correctVal = i + 1;
            break;
        }
    }
    return correctVal
}

let initials = [
    "google", "bing", "wikipedia", "ask",
    "facebook", "twitter", "skype", "whatsapp",
    "youtube", "msn", "accuweather",
    "google play", "app store", "microsoft store",
    "icloud", "google drive", "one drive",
    "chatgpt", "gemini", "copilot"
];

btnSave.addEventListener("click", () => {
    if (isValidURL(urlInput.value) && nameInput.value !== "") {
        let correctsave = correctOption();
        if (initials.includes(nameInput.value.toLowerCase())) {
            alert("لا يمكن تكرار إضافة أسماء المواقع الموجودة مسبقا في البداية , غير الإسم");
        } else {
            template(urlInput.value, nameInput.value, titleInput.value, correctsave);

            let stored = JSON.parse(localStorage.getItem("Websites")) || {};
            stored[`url${correctsave}`] = stored[`url${correctsave}`] || [];
            stored[`url${correctsave}`].push({ name: nameInput.value, url: urlInput.value, title: titleInput.value });
            localStorage.setItem("Websites", JSON.stringify(stored));

            alert("تمت الإضافة بنجاح");
            box.style.display = "none";
        }
    } else {
        alert("رجاء أدخل اسم و موقع ويب صحيح");
    }
});

btnRemove.addEventListener("click", () => {
    let correctremove = correctOption();
    let removeElement = document.querySelectorAll(`.url${correctremove} a`)
    if (nameInput.value === "") {
        alert("رجاء اكتب اسم الموقع");
    } else {
        let found = false;
        if (initials.includes(nameInput.value.toLowerCase())) {
            alert("المواقع الموجودة مسبقا في البداية لا يمكن إزالتها , فقط يمكنك إزالة المواقع الي أضقتها بنفسك");
        } else {
            for (let i = 0; i < removeElement.length; i++) {
                if (removeElement[i].textContent.trim().toLowerCase() === nameInput.value.toLowerCase()) {
                    removeElement[i].remove();
                    alert("تمت الإزالة بنجاح");
                    found = true;
                    break;
                }
            }
            if (found) {
                let stored = JSON.parse(localStorage.getItem("Websites")) || {};
                stored[`url${correctremove}`] = stored[`url${correctremove}`].filter(item => item.name.toLowerCase() !== nameInput.value.toLowerCase());
                localStorage.setItem("Websites", JSON.stringify(stored));
                box.style.display = "none";
            } else {
                alert("اسم الموقع خاطئ أو غير موجود , أو تم اختيار الفئة الخطأ , تأكد و حاول مرة أخرى");
            }
        }
    }
});

let video = document.querySelector(".more");
video.addEventListener("click", () => {
    let newWindow = window.open("", "_blank", "width=660, height=500");
    if (newWindow) {
        newWindow.document.write(`
        <video controls autoplay muted>
            <source src="Homepage.mp4" type="video/mp4">
        </video>
        `);
        newWindow.document.body.style.overflow = "hidden";
        newWindow.document.close();
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
