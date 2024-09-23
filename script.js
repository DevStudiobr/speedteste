document.getElementById('start-test').addEventListener('click', function() {
    fetch('/speedtest')
        .then(response => response.json())
        .then(data => {
            document.getElementById('download').innerText = `Download: ${data.download.toFixed(2)} Mbps`;
            document.getElementById('upload').innerText = `Upload: ${data.upload.toFixed(2)} Mbps`;
            document.getElementById('results').classList.remove('hidden');
        });
});
