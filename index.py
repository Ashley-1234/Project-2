<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MITS Landing Page</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="font-sans bg-gray-50">
  <!-- Sticky Internship Banner -->
  <div class="sticky top-0 left-0 z-50 bg-gradient-to-r from-blue-600 to-blue-800 text-white p-2 text-sm w-full text-center shadow-md">
    <a href="#apply" class="hover:underline font-bold">🚀 Apply for Internship</a>
  </div>

  <!-- Sidebar and Hamburger -->
  <div class="flex">
    <!-- Sidebar -->
    <div id="sidebar" class="fixed top-0 left-0 h-full w-64 bg-gray-900 text-white p-4 transform -translate-x-full transition-transform duration-300 ease-in-out z-40">
      <h2 class="text-2xl font-bold mb-6 border-b pb-2">📚 Menu</h2>
      <ul class="space-y-4">
        <li><a href="#apply" class="hover:underline">Internship Application</a></li>
        <li><a href="#offer" class="hover:underline">Offer Letter Generation</a></li>
        <li><a href="#verify" class="hover:underline">Certificate Verification</a></li>
        <li><a href="#team" class="hover:underline">Join Team Form</a></li>
        <li><a href="#contact" class="hover:underline">Contact Info</a></li>
      </ul>
    </div>

    <!-- Hamburger -->
    <button id="hamburger" class="fixed top-2 left-2 z-50 bg-blue-700 text-white p-2 rounded-md focus:outline-none shadow-md">
      &#9776;
    </button>

    <!-- Main Content -->
    <div class="ml-4 mt-16 px-6">
      <!-- Hero Section -->
      <section class="text-center mb-12">
        <h1 class="text-4xl font-extrabold text-blue-800">Micro Information Technology Services (MITS)</h1>
        <p class="text-gray-700 mt-4 max-w-2xl mx-auto text-lg">
          Empowering students with real-world tech experiences, MITS bridges the academic-industry gap through high-quality internships and tech training programs.
        </p>
      </section>

      <!-- University Names -->
      <section class="mb-12">
        <h2 class="text-2xl font-semibold mb-4 text-gray-800">🎓 Affiliated Universities</h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4 text-center text-sm text-gray-700">
          <div>IIT Madras</div>
          <div>Anna University</div>
          <div>VIT University</div>
          <div>SRM Institute</div>
          <div>Amrita University</div>
          <div>NIT Trichy</div>
          <div>SASTRA University</div>
          <div>PSG Tech</div>
          <div>Loyola College</div>
          <div>Christ University</div>
        </div>
      </section>

      <!-- Social Media Stats -->
      <section class="mb-12">
        <h2 class="text-2xl font-semibold mb-4 text-gray-800">📊 Social Media Presence</h2>
        <ul class="space-y-2 text-gray-700 text-base">
          <li>🌐 <strong>LinkedIn</strong>: 15,000+ followers</li>
          <li>📘 <strong>Facebook</strong>: 10,000+ followers</li>
          <li>📱 <strong>Instagram</strong>: 8,000+ followers</li>
          <li>🌍 <strong>Global Network</strong>: Connected to 100+ universities & colleges</li>
        </ul>
      </section>
    </div>
  </div>

  <!-- JavaScript for Sidebar Toggle -->
  <script>
    const sidebar = document.getElementById("sidebar");
    const hamburger = document.getElementById("hamburger");
    
    hamburger.addEventListener("click", () => {
      sidebar.classList.toggle("-translate-x-full");
    });
  </script>
</body>
</html>
