async function initDashboard() {
  try {
    const records = await loadKnowledgeRecords();
    const relationships = await loadRelationships();
    const modules = await loadModules();
    const experiments = await loadExperiments();

    renderKnowledgeRecords(
      records,
      document.getElementById("records-container")
    );

    renderRelationships(
      relationships,
      document.getElementById("relationships-container")
    );

    renderRelationshipGraph(
      relationships,
      document.getElementById("relationship-graph")
    );

    renderModules(
      modules,
      document.getElementById("modules-container")
    );

    renderExperiments(
      experiments,
      document.getElementById("experiments-container")
    );
  } catch (error) {
    console.error("Dashboard initialization failed:", error);
  }
}

initDashboard();console.log("AM-PKO Architecture Dashboard loaded.");
