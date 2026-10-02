async function loadRelationships() {
  const response = await fetch("data/relationships.json");

  if (!response.ok) {
    throw new Error("Failed to load relationships.");
  }

  return response.json();
}

function renderRelationships(relationships, container) {
  container.innerHTML = "";

  relationships.forEach((relationship) => {
    const article = document.createElement("article");
    article.className = "relationship-card";

    article.innerHTML = `
      <h3>${relationship.id} — ${relationship.type}</h3>
      <p>${relationship.source} → ${relationship.target}</p>
    `;

    container.appendChild(article);
  });
}
