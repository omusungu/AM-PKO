async function loadExperiments() {
  const response = await fetch("data/experiments.json");

  if (!response.ok) {
    throw new Error("Failed to load experiments.");
  }

  return response.json();
}

function renderExperiments(experiments, container) {
  container.innerHTML = "";

  experiments.forEach((experiment) => {
    const article = document.createElement("article");
    article.className = "experiment-card";

    article.innerHTML = `
      <h3>${experiment.id} — ${experiment.name}</h3>
      <p>${experiment.description}</p>
      <small>
        ${experiment.type} ·
        Status: ${experiment.status}
      </small>
    `;

    container.appendChild(article);
  });
}
