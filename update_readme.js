const axios = require('axios');
const fs = require('fs');
const path = require('path');
const username = 'sailwalpranjal';
const maxRepos = 6;

async function fetchRepos() {
  try {
    const response = await axios.get(`https://api.github.com/users/${username}/repos?sort=updated&per_page=100`);
    const repos = response.data;
    repos.sort((a, b) => b.stargazers_count - a.stargazers_count);
    return repos.slice(0, maxRepos);
  } catch (error) {
    console.error('Error fetching repositories:', error.message);
    return []; // Return an empty array if there's an error
  }
}

async function updateReadme(repos) {
  const readmeContent = `
<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Architects+Daughter&color=FF69B4&size=40&center=true&vCenter=true&width=800&height=60&lines=Hi+there!+I'm+Pranjal+Sailwal+👋;Computer+Science+Student+💻;Passionate+Programmer+👨‍💻;Tech+Enthusiast+🚀" alt="Typing SVG" />
</div>

<div align="center">
  <!-- Profile Banner with Animation -->
  <img src="https://github.com/sailwalpranjal/sailwalpranjal/raw/main/Components/Name.gif" alt="Name GIF" width="300"/>
  <br>
  <img src="https://github.com/sailwalpranjal/sailwalpranjal/raw/main/Components/Greetings.gif" alt="Greetings GIF" width="300"/>
  <br><br>
  
  <!-- Colorful Divider -->
  <img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
  
  <!-- Animated Social Media Badges -->
  <p align="center">
    <a href="https://www.linkedin.com/in/pranjal-sailwal/">
      <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&color=071A2C" alt="LinkedIn"/>
    </a>
    <a href="https://twitter.com/sailwalpranjal">
      <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white&color=071A2C" alt="Twitter"/>
    </a>
    <a href="https://dev.to/sailwalpranjal">
      <img src="https://img.shields.io/badge/Dev.to-%2312100E.svg?&style=for-the-badge&logo=dev.to&logoColor=white&color=071A2C" alt="Dev.to"/>
    </a>
    <a href="https://medium.com/@pranjalsailwal09">
      <img src="https://img.shields.io/badge/Medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white&color=071A2C" alt="Medium"/>
    </a>
    <a href="https://www.instagram.com/pranjal_sailwal/">
      <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white&color=071A2C" alt="Instagram"/>
    </a>
    <a href="mailto:pranjalsailwal09@gmail.com">
      <img src="https://img.shields.io/badge/Email-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white&color=071A2C" alt="Email"/>
    </a>
  </p>

<!-- Animated wave separator -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=header"/>

## <div align="center">🌟 About Me 🌟</div>

<table>
  <tr>
    <td width="60%">
      <div style="text-align: left; padding: 15px; background-color: #0d1117; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
        <h3>👨‍💻 I'm <b>Pranjal Sailwal</b></h3>
        <p><i>Turning coffee into code and dreams into reality ✨</i></p>
        <p>A passionate Computer Science student at Graphic Era Hill University, Dehradun, with a keen interest in software development, algorithms, and cutting-edge technologies.</p>
        <ul>
          <li>🔭 Currently working on building a robust portfolio of projects</li>
          <li>🌱 Mastering data structures, algorithms, and full-stack development</li>
          <li>💡 Exploring the realms of cloud computing and DevOps</li>
          <li>🤝 Open to collaborating on innovative open-source projects</li>
          <li>💬 Ask me about programming, tech trends, or problem-solving approaches</li>
          <li>📚 Continuously learning and adapting to new technologies</li>
          <li>📫 Reach out at: <a href="mailto:pranjalsailwal09@gmail.com">pranjalsailwal09@gmail.com</a></li>
          <li>😄 Pronouns: He/Him</li>
          <li>⚡ Fun fact: I can debug code faster with lofi music in the background!</li>
        </ul>
      </div>
    </td>
    <td width="40%" align="center">
      <!-- Replace with a more visually appealing programmer image -->
      <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100%" alt="Coding Animation"/>
      <br><br>
      <!-- Daily Dev Quote -->
      <img src="https://quotes-github-readme.vercel.app/api?type=vertical&theme=radical" width="100%" alt="Quote Card"/>
    </td>
  </tr>
</table>

<div align="center">
  <!-- Spotify Now Playing -->
  <img src="https://novatorem-nu-seven.vercel.app/api/spotify" alt="Spotify Now Playing" width="350"/>
</div>

<!-- Colorful Divider -->
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">


<!-- INTERACTIVE RESUME WITH COLLAPSIBLE SECTIONS -->
<div align="center">
  <h1>
    Resume
  </h1>
</div>

<p align="center">
  <img src="https://github.com/sailwalpranjal/sailwalpranjal/raw/main/assets/resume_preview.png" alt="Resume Preview" width="60%" style="border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
</p>

<p align="center">
  <a href="https://github.com/sailwalpranjal/sailwalpranjal/blob/main/assets/Pranjal_Resume.pdf?raw=true" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/View%20Full%20Resume-8C52FF?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="View Resume">
  </a>
  <a href="https://github.com/sailwalpranjal/sailwalpranjal/raw/main/assets/Pranjal_Resume.pdf" download>
    <img src="https://img.shields.io/badge/Download%20Resume-FF5722?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Download Resume">
  </a>
</p>



  <h3>💼 Work Experience</h3>
  
  <table>
    <tr>
      <td><strong>Freelancer Software Developer</strong></td>
      <td>Self-Employed</td>
      <td>Jan 2023 – Present</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Developed a React full-stack website for a property dealing business, enhancing user engagement and streamlining property management.</li>
          <li>Increased traffic by 50% and improved client interaction through responsive design and optimized features.</li>
          <li>Utilized Node.js and Express for backend development, ensuring smooth data integration and functionality.</li>
        </ul>
      </td>
    </tr>
  </table>

  <h3>🖥️ Projects</h3>

  <table>
    <tr>
      <td><strong>NO2-Sentinel</strong></td>
      <td>Project Lead</td>
      <td>Nov 2024 – Present</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Developing satellite-based NO2 monitoring system with advanced air quality analysis and reporting features.</li>
          <li>Implemented data visualization and predictive analytics for improved decision-making.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>Pranjal's Vantage</strong></td>
      <td>Lead Developer</td>
      <td>Oct 2024 – Present</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Built a responsive 3D portfolio using React and Three.js with GPU-accelerated rendering for enhanced performance.</li>
          <li>Showcases technical expertise through interactive and dynamic design elements.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>GitPulse</strong></td>
      <td>Lead Developer</td>
      <td>Aug 2024 – Present</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Automated GitHub operations, including live commit monitoring, issue management, and pull request tracking.</li>
          <li>Enhanced repository productivity by 40% through intuitive analytics and automation workflows.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>PrediStock</strong></td>
      <td>Golang Enthusiast</td>
      <td>Aug 2024</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Optimized data processing workflows using Go, improving predictive accuracy by 30%.</li>
          <li>Integrated machine learning models to forecast stock trends effectively.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>ByteBuddies</strong></td>
      <td>Python Developer</td>
      <td>Aug 2024</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Created an animated, interactive feature that reacts to user interaction, increasing engagement by 25%.</li>
          <li>Improved user interface through responsive design and smooth animations.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>CipherLab</strong></td>
      <td>Python Developer</td>
      <td>Jul 2024</td>
    </tr>
    <tr>
      <td colspan="3">
        <ul>
          <li>Integrated advanced cryptographic techniques and secure communication standards.</li>
          <li>Ensured 99.9% data integrity through comprehensive security evaluations.</li>
        </ul>
      </td>
    </tr>
  </table>

  <h3>🎓 Education</h3>
  
  <table>
    <tr>
      <td><strong>B.Tech in Computer Science and Engineering</strong></td>
      <td>Graphic Era Hill University</td>
      <td>2022 – 2026</td>
    </tr>
    <tr>
      <td><strong>Senior Secondary (CBSE)</strong></td>
      <td>Kendriya Vidyalaya OLF, Dehradun</td>
      <td>2022</td>
    </tr>
    <tr>
      <td><strong>Secondary (CBSE)</strong></td>
      <td>Kendriya Vidyalaya OLF, Dehradun</td>
      <td>2020</td>
    </tr>
  </table>

  <h3>🌍 Languages</h3>
  <table>
  <tr>
    <td>English – B2 Level</td>
    <td>Hindi – Native Proficiency</td>
  </tr>
  </table>


## Technologies I've Engaged With

<div align="center">
  
<!-- Programming Languages -->
[![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white&label=&labelColor=3776AB&color=3776AB&logoWidth=60&logoHeight=60&shape=square)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript&logoColor=white&label=&labelColor=F7DF1E&color=F7DF1E&logoWidth=60&logoHeight=60&shape=circle)](https://www.javascript.com/)
[![Java](https://img.shields.io/badge/Java-red?style=for-the-badge&logo=java&logoColor=white&label=&labelColor=007396&color=007396&logoWidth=60&logoHeight=60&shape=diamond)](https://www.java.com/)
[![C++](https://img.shields.io/badge/C++-green?style=for-the-badge&logo=c%2B%2B&logoColor=white&label=&labelColor=00599C&color=00599C&logoWidth=60&logoHeight=60&shape=triangle)](https://www.cplusplus.com/)
[![Go](https://img.shields.io/badge/Go-blue?style=for-the-badge&logo=go&logoColor=white&label=&labelColor=00ADD8&color=00ADD8&logoWidth=60&logoHeight=60&shape=hexagon)](https://golang.org/)
[![SQL](https://img.shields.io/badge/SQL-yellowgreen?style=for-the-badge&logo=mysql&logoColor=white&label=&labelColor=4479A1&color=4479A1&logoWidth=60&logoHeight=60&shape=circle)](https://www.w3schools.com/sql/)
[![HTML5](https://img.shields.io/badge/HTML5-orange?style=for-the-badge&logo=html5&logoColor=white&label=&labelColor=E34F26&color=E34F26&logoWidth=60&logoHeight=60&shape=hexagon)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-blueviolet?style=for-the-badge&logo=css3&logoColor=white&label=&labelColor=1572B6&color=1572B6&logoWidth=60&logoHeight=60&shape=star)](https://developer.mozilla.org/en-US/docs/Web/CSS)

<!-- Databases -->
[![SQLite](https://img.shields.io/badge/SQLite-blue?style=for-the-badge&logo=sqlite&logoColor=white&label=&labelColor=003B57&color=003B57&logoWidth=60&logoHeight=60&shape=circle)](https://www.sqlite.org/)

<!-- Frameworks & Tools -->
[![Docker](https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker&logoColor=white&label=&labelColor=2496ED&color=2496ED&logoWidth=60&logoHeight=60&shape=hexagon)](https://www.docker.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-blue?style=for-the-badge&logo=tailwindcss&logoColor=white&label=&labelColor=38B2AC&color=38B2AC&logoWidth=60&logoHeight=60&shape=square)](https://tailwindcss.com/)

<!-- Additional Tools and Technologies -->
[![Git](https://img.shields.io/badge/Git-orange?style=for-the-badge&logo=git&logoColor=white&label=&labelColor=F05032&color=F05032&logoWidth=60&logoHeight=60&shape=circle)](https://git-scm.com/)
[![Linux](https://img.shields.io/badge/Linux-black?style=for-the-badge&logo=linux&logoColor=white&label=&labelColor=000000&color=000000&logoWidth=60&logoHeight=60&shape=square)](https://www.linux.org/)
[![Bash](https://img.shields.io/badge/Bash-green?style=for-the-badge&logo=gnu-bash&logoColor=white&label=&labelColor=4EAA25&color=4EAA25&logoWidth=60&logoHeight=60&shape=circle)](https://www.gnu.org/software/bash/)
[![HTTP](https://img.shields.io/badge/HTTP-9B4F77?style=for-the-badge&logo=http&logoColor=white&label=&labelColor=9B4F77&color=9B4F77&logoWidth=60&logoHeight=60&shape=hexagon)](https://developer.mozilla.org/en-US/docs/Web/HTTP)
[![JSON](https://img.shields.io/badge/JSON-lightgrey?style=for-the-badge&logo=json&logoColor=white&label=&labelColor=005A1F&color=005A1F&logoWidth=60&logoHeight=60&shape=circle)](https://www.json.org/)

[![Kali Linux](https://img.shields.io/badge/Kali%20Linux-black?style=for-the-badge&logo=kali-linux&logoColor=white&label=&labelColor=000000&color=000000&logoWidth=60&logoHeight=60&shape=square)](https://www.kali.org/)
[![VS Code](https://img.shields.io/badge/VS%20Code-blue?style=for-the-badge&logo=visual-studio-code&logoColor=white&label=&labelColor=007ACC&color=007ACC&logoWidth=60&logoHeight=60&shape=hexagon)](https://code.visualstudio.com/)
[![VS Code Insider](https://img.shields.io/badge/VS%20Code%20Insider-darkblue?style=for-the-badge&logo=visual-studio-code&logoColor=white&label=&labelColor=0068C6&color=0068C6&logoWidth=60&logoHeight=60&shape=circle)](https://insiders.code.visualstudio.com/)
[![VS Code Community](https://img.shields.io/badge/VS%20Code%20Community-darkblue?style=for-the-badge&logo=visual-studio-code&logoColor=white&label=&labelColor=1E1E1E&color=1E1E1E&logoWidth=60&logoHeight=60&shape=square)](https://code.visualstudio.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-orange?style=for-the-badge&logo=jupyter&logoColor=white&label=&labelColor=F37626&color=F37626&logoWidth=60&logoHeight=60&shape=hexagon)](https://jupyter.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-blue?style=for-the-badge&logo=latex&logoColor=white&label=&labelColor=008080&color=008080&logoWidth=60&logoHeight=60&shape=circle)](https://www.latex-project.org/)
[![Markdown](https://img.shields.io/badge/Markdown-black?style=for-the-badge&logo=markdown&logoColor=white&label=&labelColor=000000&color=000000&logoWidth=60&logoHeight=60&shape=square)](https://daringfireball.net/projects/markdown/)
[![RStudio](https://img.shields.io/badge/RStudio-blue?style=for-the-badge&logo=r&logoColor=white&label=&labelColor=75AADB&color=75AADB&logoWidth=60&logoHeight=60&shape=hexagon)](https://rstudio.com/)
[![WSL](https://img.shields.io/badge/WSL-darkgreen?style=for-the-badge&logo=windows-subsystem-for-linux&logoColor=white&label=&labelColor=000000&color=000000&logoWidth=60&logoHeight=60&shape=square)](https://docs.microsoft.com/en-us/windows/wsl/)
[![YAML](https://img.shields.io/badge/YAML-darkblue?style=for-the-badge&logo=yaml&logoColor=white&label=&labelColor=000000&color=000000&logoWidth=60&logoHeight=60&shape=hexagon)](https://yaml.org/)

</div>

## Trophies

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=sailwalpranjal&theme=juicyfresh&no-frame=true&row=1&column=6" alt="GitHub Profile Trophy" />
</div>

### GitHub Stats and Streak

<div align="center">
  <table style="width: 100%; max-width: 800px; border-collapse: collapse;">
    <tr>
      <td style="border: none; padding: 0; width: 50%;">
        <img src="https://github-readme-stats.vercel.app/api?username=sailwalpranjal&show_icons=true&theme=highcontrast" alt="GitHub Stats" style="width: 100%; max-width: 400px; border-radius: 8px;" />
      </td>
      <td style="border: none; padding: 0; width: 50%;">
        <img src="https://github-readme-streak-stats.herokuapp.com/?user=sailwalpranjal&theme=highcontrast" alt="GitHub Streak" style="width: 100%; max-width: 400px; border-radius: 8px;" />
      </td>
    </tr>
  </table>
</div>

<div align="center">
  <h3> Contribution Graph </h3>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=sailwalpranjal&theme=tokyo-night&hide_border=true&bg_color=0D1117" alt="Contribution Graph" width="100%"/>
</div>

<!-- Wavy separator -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&text=Featured%20Projects&fontSize=42&fontColor=fff&animation=twinkling"/>


<div align="center">
  <table>
    <tr>
      <td width="50%">
        <a href="https://github.com/sailwalpranjal/sailwalpranjal">
          <img src="https://github-readme-stats.vercel.app/api/pin/?username=sailwalpranjal&repo=sailwalpranjal&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="GitHub Profile"/>
        </a>
        <p align="center">📌 My GitHub Profile Repository</p>
      </td>
      <td width="50%">
        <a href="https://github.com/sailwalpranjal/LeetCode">
          <img src="https://github-readme-stats.vercel.app/api/pin/?username=sailwalpranjal&repo=LeetCode&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="LeetCode Solutions"/>
        </a>
        <p align="center">🧩 My LeetCode Problem Solutions</p>
      </td>
    </tr>
  </table>
</div>

<!-- Project Showcase -->
<div align="center">
  <details>
    <summary>
      <h3>🚀 More Projects (Click to Expand)</h3>
    </summary>
    <table>
      <tr>
        <th>Project</th>
        <th>Description</th>
        <th>Status</th>
        <th>Tech Stack</th>
      </tr>
      <tr>
        <td>🔒 Cyber Security Tool</td>
        <td>A comprehensive security assessment and penetration testing tool</td>
        <td><img src="https://img.shields.io/badge/Status-Planning-yellow?style=flat-square" alt="Planning"></td>
        <td>Python, Go, Linux</td>
      </tr>
      <tr>
        <td>🌐 Personal Portfolio</td>
        <td>Interactive web portfolio showcasing projects and skills</td>
        <td><img src="https://img.shields.io/badge/Status-In_Progress-blue?style=flat-square" alt="In Progress"></td>
        <td>HTML, CSS, JavaScript, Tailwind</td>
      </tr>
      <tr>
        <td>🤖 AI Assistant</td>
        <td>Personal AI assistant for productivity tasks</td>
        <td><img src="https://img.shields.io/badge/Status-Concept-purple?style=flat-square" alt="Concept"></td>
        <td>Python, TensorFlow</td>
      </tr>
    </table>
  </details>
</div>

<!-- Sparkle divider -->
<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>


## Contributions

<img src="profile-3d-contrib/profile-night-rainbow.svg" alt="Profile Night Rainbow" width="600" height="400" />

<div align="center"><h1>📬 Connect With Me 📬</h1></div>

<div align="center">
  <table style="width: 100%; border-collapse: separate; border-spacing: 0 8px;">
    <tr>
      <td width="50%" align="center" style="background: linear-gradient(90deg, rgba(131,58,180,0.2) 0%, rgba(253,29,29,0.2) 50%, rgba(252,176,69,0.2) 100%); border-radius: 8px; padding: 15px;">
        <h3>💬 Let's Connect</h3>
        <p>I'm always open to interesting conversations, collaboration opportunities, and making new connections in the tech community!</p>
        <a href="https://www.linkedin.com/in/pranjal-sailwal/">
          <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
        </a>
        <a href="https://twitter.com/sailwalpranjal">
          <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/>
        </a>
        <a href="mailto:pranjalsailwal09@gmail.com">
          <img src="https://img.shields.io/badge/Email-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
        </a>
      </td>
      <td width="50%" align="center" style="background: linear-gradient(90deg, rgba(252,176,69,0.2) 0%, rgba(131,58,180,0.2) 50%, rgba(253,29,29,0.2) 100%); border-radius: 8px; padding: 15px;">
        <h3>📅 Schedule a Meeting</h3>
        <p>Interested in discussing a project or just want to chat about tech? Feel free to schedule a meeting!</p>
        <a href="https://www.google.com/calendar/render?action=TEMPLATE&text=Meeting+with+You&details=Let's+schedule+a+meeting&location=&dates=20250501T120000Z/20250501T130000Z" target="_blank">
          <img src="https://img.shields.io/badge/Schedule_Meeting-4285F4?style=for-the-badge&logo=google-calendar&logoColor=white" alt="Schedule Meeting"/>
        </a>
      </td>
    </tr>
  </table>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg" width="100%">
</div>

`;
  try {
    const filePath = path.join(__dirname, 'README.md');
    fs.writeFileSync(filePath, readmeContent);
    console.log('README.md has been updated successfully.');
  } catch (error) {
    console.error('Error writing README.md:', error.message);
  }
}

async function main() {
  try {
    const repos = await fetchRepos();
    await updateReadme(repos);
  } catch (error) {
    console.error('Error updating README:', error.message);
  }
}

main();
