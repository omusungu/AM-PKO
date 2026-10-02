async function loadKnowledgeRecords() {
  const response = await fetch("data/knowledge-records.json");

  if (!response.ok) {
    throw new Error("Failed to load knowledge records.");
  }

  return response.json();
}

function renderKnowledgeRecords(records, container) {
  container.innerHTML = "";

  records.forEach((record) => {
    const article = document.createElement("article");
    article.className = "record-card";

    article.innerHTML = `
      <h3>${record.id} — ${record.title}</h3>
      <p>${record.content}</p>
      <small>
        ${record.knowledge_type} ·
        ${record.granularity} ·
        ${record.status}
      </small>
    `;

    container.appendChild(article);
  });
}
