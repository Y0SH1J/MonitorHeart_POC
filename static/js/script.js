function fetchData() {
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    console.log("Fetched data:", data); // For debugging on console
                    
                    let bpmDisplay = document.getElementById('bpm-data'); // Get html element with id 'bpm-data'
                    
                    if (count == 0) {
                        bpmDisplay.innerText = " ";
                    } // Erase "Loading..." text in element

                    // Append only the new data
                    for (let i = count; i < data.length; i++) {               
                        // document.getElementById('bpm-data').innerText = data.join(', ');
                        if (count == 0) {
                            bpmDisplay.innerText += 'ID: ' + data[i] + '\n Live BPM Data:'; // Display ID on first line and bpm feed on next line
                        }
                        else {
                            bpmDisplay.innerText += ' ' + data[i] + ','; // Display bpm list data
                        }
                    }

                    count = data.length; // Ensure new data is appended
                })
                .catch(error => console.error('Error fetching data:', error));
        }

let count = 0;
setInterval(fetchData, 1000);  // Fetch every 1 second
fetchData();  // Run immediately, otherwise we would have to wait 1 second before first data fetch happens
