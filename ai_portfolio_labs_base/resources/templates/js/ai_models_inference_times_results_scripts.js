function showFileName() {
    const fileInput = document.getElementById("imageInput");
    const fileNameDisplay = document.getElementById("fileNameDisplay");

    fileNameDisplay.textContent = fileInput.files.length > 0
        ? fileInput.files[0].name
        : "No file chosen yet...";
}

function uploadImage() {
    const imageInput = document.getElementById("imageInput").files[0];
    const resultDiv = document.getElementById("result");
    const loadingText = document.getElementById("loading");

    if (!imageInput) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("image", imageInput);

    loadingText.style.display = "block";
    resultDiv.style.display = "none";

    fetch("/api/ai_models_inference_times_comparison/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loadingText.style.display = "none";
        resultDiv.style.display = "block";
        resultDiv.innerHTML = `
            <strong>TensorFlow:</strong> ${data.tensorflow_time} ms <br>
            <strong>PyTorch:</strong> ${data.pytorch_time} ms <br>
            <h3>🏆 Winner: ${data.winner}!</h3>
        `;
    })
    .catch(error => {
        loadingText.style.display = "none";
        console.error("Error:", error);
        alert("Error processing image. Please try again.");
    });
}
