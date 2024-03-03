document.addEventListener("DOMContentLoaded", function() {

  document.addEventListener("DOMContentLoaded", function() {
    const uploadForm = document.getElementById("upload-form"); // Assuming your form's ID
  
    uploadForm.addEventListener("submit", (event) => {
      event.preventDefault(); // Prevent default form submission
  
      const fileInput = document.getElementById("biodata-file"); // Assuming your file input ID
      const file = fileInput.files[0]; // Get the selected file
  
      if (!file) {
        alert("Please select a bioinformatics data file!");
        return; // Exit if no file is selected
      }
  
      // Prepare data for sending (adjust based on your backend API requirements)
      const formData = new FormData();
      formData.append("biodata", file); // Assuming "biodata" is the expected field name on the backend
  
      // Send data to the backend (replace with your actual logic)
      fetch("/api/process-biodata", {
        method: "POST",
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          console.log("Data sent successfully! Received response:", data);
          // Display the report using the received data (see below)
          displayReport(data);
        })
        .catch(error => {
          console.error("Error sending data:", error);
          // Handle errors during data processing or communication (e.g., user notification)
        });
    });
  
    // Function to display the report (replace with your specific logic)
    function displayReport(reportData) {
      const reportSection = document.getElementById('report-section');
      // ... (Process and display the report content based on reportData)
      reportSection.style.display = 'block'; // Make the report section visible
    }
  });
  

  const form1 = document.getElementById("form1");
const form2 = document.getElementById("form2");
const loginButton = document.querySelector(".login-section button"); // Assuming button within login-section

loginButton.addEventListener("click", () => {
  // Animate form visibility
  form1.classList.add("hidden"); // Hide form1 with animation
  form2.classList.remove("hidden"); // Show form2 with animation

  // Add animation class names to forms (replace with your animation class names)
  form1.classList.add("animate-out");
  form2.classList.add("animate-in");

  // Optionally implement animation completion handling based on your requirements (e.g., CSS transitions)
});

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const target = entry.target;
      // Add animation class to the target element (e.g., page)
      target.classList.add("animate-in");
      observer.unobserve(target);
    }
  });
});

const pages = document.querySelectorAll(".index-main"); // Assuming your page content is wrapped in a ".page" class

pages.forEach(page => {
  observer.observe(page);
});

  function validateLoginForm() {
  console.log("Validation triggered!");
  // Get references to username and password fields
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  // Check if username is empty
  if (usernameInput.value === "") {
    alert("Please enter your username.");
    usernameInput.focus(); // Set focus to username field
    usernameInput.classList.add("error"); // Add error class for styling
    return false;
  } else {
    usernameInput.classList.remove("error"); // Remove error class if previously added
  }

  // Check if password is empty
  if (passwordInput.value === "") {
    alert("Please enter your password.");
    passwordInput.focus();
    passwordInput.classList.add("error"); // Add error class for styling
    return false;
  } else {
    passwordInput.classList.remove("error"); // Remove error class if previously added
  }

  // If both fields are valid, allow form submission
  return true;

  
}

// Add event listener to the login form (check for null first)
(function() {
const loginForm = document.getElementById("login-form");
if (loginForm) {
  loginForm.addEventListener("submit", (event) => {
    if (!validateLoginForm()) {
      event.preventDefault(); // Prevent form submission if validation fails
      return; // Exit the function if validation fails
    }

    // Handle successful validation, e.g., submit data to backend server
    console.log("Form submitted successfully!");

    // Replace with your actual form submission logic (e.g., sending data to backend)
    // ...
  });
} else {
  console.error("Login form element not found!");
}
})();
});