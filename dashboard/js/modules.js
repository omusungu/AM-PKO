async function loadModules() {
  const response = await fetch("data/modules.json");

  if (!response.ok) {
    throw new Error("Failed to load modules.");
  }

  return response.json();
}

function renderModules(modules, container) {
  container.innerHTML = "";

  modules.forEach((module) => {
    const article = document.createElement("article");
    article.className = "module-card";

    article.innerHTML = `
      <h3>${module.id} — ${module.name}</h3>
      <p>${module.function}</p>
      <small>
        ${module.category} ·
        Interface: ${module.interface}
      </small>
    `;

    container.appendChild(article);
  });
}
