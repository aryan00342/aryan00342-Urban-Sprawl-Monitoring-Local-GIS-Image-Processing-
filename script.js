document.getElementById('uploadForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const file = document.getElementById('imageInput').files[0];
  if (!file) {
    alert("Please upload an image first!");
    return;
  }

  const formData = new FormData();
  formData.append('image', file);

  // Show loading animation
  const resultDiv = document.getElementById('result');
  resultDiv.classList.remove('hidden');
  resultDiv.innerHTML = `
    <div class="loading">
      <div class="spinner"></div>
      <p>🛰️ Analyzing satellite image... Please wait</p>
    </div>
  `;

  try {
    const response = await fetch('/process', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();

    // Display the processed image and analysis report
    resultDiv.innerHTML = `
      <h2>🖼️ Processed Output</h2>
      <img id="processedImage" src="${data.image_url}" alt="Processed Output"/>

      <div id="analysis">
        <h3>🧠 Analysis Report</h3>
        <ul>
          <li><strong>Urban Area:</strong> ${data.urban_area} sq km</li>
          <li><strong>Green Cover Loss:</strong> ${data.green_loss}%</li>
          <li><strong>Growth Rate:</strong> ${data.growth_rate}%</li>
          <li><strong>Detected Zones:</strong> ${data.zones.join(', ')}</li>
          <li><strong>Analysis Time:</strong> ${data.timestamp}</li>
        </ul>
        <p>📊 The analysis shows that urban growth is progressing steadily. Consider green initiatives to balance expansion with sustainability.</p>
      </div>
    `;
  } catch (error) {
    resultDiv.innerHTML = `<p style="color:red;">❌ Error processing image. Please try again.</p>`;
  }
});
