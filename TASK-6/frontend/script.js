// ---------- THEME SWITCH ----------
function setTheme(theme) {
    document.body.className = "theme-" + theme;
}

// ---------- DRAG & DROP ----------
const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("imageInput");

dropArea.addEventListener("click", () => fileInput.click());

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("dragover");
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("dragover");

    fileInput.files = e.dataTransfer.files;
    showPreview();
});

fileInput.addEventListener("change", showPreview);

function showPreview() {
    const preview = document.getElementById("preview");
    let file = fileInput.files[0];
    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
}

// ---------- API CALL ----------
function classifyImage() {
    const model = document.getElementById("modelSelect").value;
    const resultBox = document.getElementById("result");
    const preview = document.getElementById("preview");

    if (!fileInput.files.length) {
        alert("Please upload an image!");
        return;
    }

    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append("file", file);
    formData.append("model", model);

    resultBox.innerHTML = "⏳ Predicting...";

    fetch("http://localhost:8000/classify", {
        method: "POST",
        body: formData
    })
        .then((response) => response.json())
        .then((data) => {
            resultBox.innerHTML = "Prediction: 🐾 <b>" + data.prediction + "</b>";
        })
        .catch((error) => {
            resultBox.innerHTML = "❌ Error: " + error;
        });
}
