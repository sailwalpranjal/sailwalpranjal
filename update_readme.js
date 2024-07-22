const axios = require('axios');
const fs = require('fs');

const username = 'sailwalpranjal';
const maxRepos = 6;

async function fetchRepos() {
  const response = await axios.get(`https://api.github.com/users/${username}/repos?sort=updated&per_page=100`);
  const repos = response.data;
  repos.sort((a, b) => b.stargazers_count - a.stargazers_count);
  return repos.slice(0, maxRepos);
}

async function updateReadme(repos) {
  const readmeContent = `
# Sailwal Pranjal's GitHub Profile

## Achievement Trophies and Rankings

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=${username}&theme=juicyfresh&no-frame=true&row=1&column=6" alt="GitHub Profile Trophy" />
</div>

## Contributions and Repositories

### GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=${username}&show_icons=true&theme=highcontrast" alt="GitHub Stats" style="width: 100%; max-width: 400px;" />
</div>

### Activity Graph

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=${username}&theme=highcontrast" alt="GitHub Activity Graph" style="width: 100%; max-width: 600px;" />
</div>

### GitHub Streak

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=${username}&theme=highcontrast" alt="GitHub Streak" style="width: 100%; max-width: 400px;" />
</div>

### Featured Repositories

<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center;">
  ${repos.map(repo => `
  <a href="${repo.html_url}">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=${username}&repo=${repo.name}&theme=highcontrast" alt="Repository Card" style="width: 100%; max-width: 400px; margin: 10px;" />
  </a>
  `).join('')}
</div>

## Reimagined ReadMe

<div align="center">
  <img src="https://myreadme.vercel.app/api/embed/${username}?panels=userstatistics,toprepositories,toplanguages,commitgraph" alt="Reimagined ReadMe" style="width: 100%; max-width: 600px;" />
</div>
`;

  fs.writeFileSync('README.md', readmeContent);
}

async function main() {
  const repos = await fetchRepos();
  await updateReadme(repos);
}

main().catch(console.error);
