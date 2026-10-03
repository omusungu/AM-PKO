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

function renderRelationshipGraph(relationships, container) {
  container.innerHTML = "";

  const nodes = [...new Set(
    relationships.flatMap((relationship) => [
      relationship.source,
      relationship.target
    ])
  )];

  const positions = {
    "K-000001": [120, 80],
    "K-000002": [360, 80],
    "K-000003": [120, 220],
    "K-000004": [360, 220],
    "K-000005": [600, 150]
  };

  const svg = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "svg"
  );

  svg.setAttribute("viewBox", "0 0 720 300");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", "AM-PKO knowledge relationship graph");

  relationships.forEach((relationship) => {
    const [x1, y1] = positions[relationship.source];
    const [x2, y2] = positions[relationship.target];

    const line = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "line"
    );

    line.setAttribute("x1", x1);
    line.setAttribute("y1", y1);
    line.setAttribute("x2", x2);
    line.setAttribute("y2", y2);
    line.setAttribute("class", "graph-edge");
    svg.appendChild(line);

    const label = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "text"
    );

    label.setAttribute("x", (x1 + x2) / 2);
    label.setAttribute("y", (y1 + y2) / 2 - 8);
    label.setAttribute("text-anchor", "middle");
    label.setAttribute("class", "graph-edge-label");
    label.textContent = relationship.type;

    svg.appendChild(label);
  });

  nodes.forEach((node) => {
    const [x, y] = positions[node];

    const group = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "g"
    );

    const circle = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "circle"
    );

    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", "32");
    circle.setAttribute("class", "graph-node");

    const text = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "text"
    );

    text.setAttribute("x", x);
    text.setAttribute("y", y + 5);
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("class", "graph-label");
    text.textContent = node;

    group.appendChild(circle);
    group.appendChild(text);
    svg.appendChild(group);
  });

  container.appendChild(svg);
}
