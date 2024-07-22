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
# Sailwal Pranjal's GitHub Profile

## Achievement Trophies and Rankings

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=${username}&theme=juicyfresh&no-frame=true&row=1&column=6" alt="GitHub Profile Trophy" />
</div>

## Contributions and Repositories

### GitHub Stats and Streak

<div align="center">
  <table style="width: 100%; max-width: 800px; border-collapse: collapse;">
    <tr>
      <td style="border: none; padding: 0; width: 50%;">
        <img src="https://github-readme-stats.vercel.app/api?username=${username}&show_icons=true&theme=highcontrast" alt="GitHub Stats" style="width: 100%; max-width: 400px; border-radius: 8px;" />
      </td>
      <td style="border: none; padding: 0; width: 50%;">
        <img src="https://github-readme-streak-stats.herokuapp.com/?user=${username}&theme=highcontrast" alt="GitHub Streak" style="width: 100%; max-width: 400px; border-radius: 8px;" />
      </td>
    </tr>
  </table>
</div>

### Activity Graph

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=${username}&theme=highcontrast" alt="GitHub Activity Graph" style="width: 100%; max-width: 600px; border-radius: 8px;" />
</div>

### Featured Repositories

<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center;">
  ${repos.length > 0 ? repos.map(repo => `
  <a href="${repo.html_url}" style="margin: 10px;">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=${username}&repo=${repo.name}&theme=highcontrast" alt="Repository Card" style="width: 100%; max-width: 400px; border-radius: 8px;" />
  </a>
  `).join('') : '<p>No repositories found.</p>'}
</div>

## Reimagined ReadMe

<div align="center">
  <img src="https://myreadme.vercel.app/api/embed/${username}?panels=userstatistics,toprepositories,toplanguages,commitgraph" alt="Reimagined ReadMe" style="width: 100%; max-width: 600px; border-radius: 8px;" />
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
