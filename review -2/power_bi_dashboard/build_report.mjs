import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const reportDir = path.join(here, "Bike_Sharing_Dashboard.Report");
const definitionDir = path.join(reportDir, "definition");
const pagesDir = path.join(definitionDir, "pages");

const SCHEMA = {
  pbip: "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",
  platform: "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
  definition: "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  version: "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
  report: "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.3.0/schema.json",
  pages: "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.1.0/schema.json",
  page: "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json",
  visual: "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
};

const pageSpecs = [
  { name: "SectionExecutiveOverview", displayName: "1. Executive Overview & KPIs" },
  { name: "SectionCommuterDynamics", displayName: "2. Commuter vs Leisure Dynamics" },
  { name: "SectionWeatherImpact", displayName: "3. Weather & Environmental Drivers" },
  { name: "SectionMLForecasts", displayName: "4. ML Predictions & Demand Forecast" },
];

const json = (value) => `${JSON.stringify(value, null, 2)}\n`;
const ensure = (dir) => fs.mkdirSync(dir, { recursive: true });
const writeJson = (file, value) => {
  ensure(path.dirname(file));
  fs.writeFileSync(file, json(value), "utf8");
};
const idFor = (page, label) => crypto.createHash("sha1").update(`${page}:${label}`).digest("hex").slice(0, 20);

const literal = (value) => ({ expr: { Literal: { Value: value } } });
const column = (table, property, native = property) => ({
  field: { Column: { Expression: { SourceRef: { Entity: table } }, Property: property } },
  queryRef: `${table}.${property}`,
  nativeQueryRef: native,
});
const measure = (property, native = property) => ({
  field: { Measure: { Expression: { SourceRef: { Entity: "Key_Measures" } }, Property: property } },
  queryRef: `Key_Measures.${property}`,
  nativeQueryRef: native,
});

const titleObjects = (title) => ({
  title: [{
    properties: {
      show: literal("true"),
      text: literal(`'${title.replaceAll("'", "''")}'`),
      alignment: literal("'left'"),
      fontSize: literal("12D"),
    },
  }],
  background: [{ properties: { show: literal("true"), transparency: literal("0D") } }],
  border: [{ properties: { show: literal("true"), radius: literal("8D") } }],
});

const position = (x, y, width, height, z) => ({ x, y, z, height, width, tabOrder: z });

function textbox(page, key, x, y, width, height, text, size = 18, color = "#12372A", weight = "normal") {
  const name = idFor(page, key);
  return {
    $schema: SCHEMA.visual,
    name,
    position: position(x, y, width, height, 1000),
    visual: {
      visualType: "textbox",
      objects: {
        general: [{ properties: { paragraphs: [{ textRuns: [{ value: text, textStyle: { fontFamily: "Segoe UI", fontSize: `${size}px`, color, fontWeight: weight } }], horizontalTextAlignment: "left" }] } }],
      },
      visualContainerObjects: {
        background: [{ properties: { show: literal("false") } }],
        border: [{ properties: { show: literal("false") } }],
        padding: [{ properties: { top: literal("0D"), bottom: literal("0D"), left: literal("0D"), right: literal("0D") } }],
      },
    },
  };
}

function card(page, key, x, y, width, height, measures) {
  const name = idFor(page, key);
  return {
    $schema: SCHEMA.visual,
    name,
    position: position(x, y, width, height, 2000),
    visual: {
      visualType: "cardVisual",
      query: { queryState: { Data: { projections: measures.map((m) => measure(m)) } } },
      objects: {
        value: [{ properties: { fontSize: literal("24D") }, selector: { id: "default" } }],
        label: [{ properties: { fontSize: literal("10D") }, selector: { id: "default" } }],
        padding: [{ properties: { paddingUniform: literal("8D") }, selector: { id: "default" } }],
      },
      visualContainerObjects: {
        background: [{ properties: { show: literal("true"), transparency: literal("0D") } }],
        border: [{ properties: { show: literal("true"), radius: literal("10D") } }],
        padding: [{ properties: { top: literal("8D"), bottom: literal("8D"), left: literal("8D"), right: literal("8D") }, selector: { id: "default" } }],
      },
    },
  };
}

function slicer(page, key, x, y, width, table, property, label) {
  const name = idFor(page, key);
  return {
    $schema: SCHEMA.visual,
    name,
    position: position(x, y, width, 80, 3000),
    visual: {
      visualType: "slicer",
      query: { queryState: { Values: { projections: [column(table, property)] } } },
      objects: {
        data: [{ properties: { mode: literal("'Dropdown'") } }],
        header: [{ properties: { show: literal("true"), text: literal(`'${label}'`) } }],
      },
      visualContainerObjects: {
        padding: [{ properties: { top: literal("8D"), bottom: literal("8D"), left: literal("8D"), right: literal("8D") } }],
        border: [{ properties: { show: literal("true"), radius: literal("8D") } }],
      },
    },
  };
}

function chart(page, key, type, x, y, width, height, title, roles) {
  const name = idFor(page, key);
  const queryState = {};
  for (const [role, projections] of Object.entries(roles)) queryState[role] = { projections };
  return {
    $schema: SCHEMA.visual,
    name,
    position: position(x, y, width, height, 4000),
    visual: {
      visualType: type,
      query: { queryState },
      visualContainerObjects: titleObjects(title),
    },
  };
}

function tableVisual(page, key, x, y, width, height, title, projections) {
  const name = idFor(page, key);
  return {
    $schema: SCHEMA.visual,
    name,
    position: position(x, y, width, height, 4000),
    visual: {
      visualType: "tableEx",
      query: { queryState: { Values: { projections } } },
      objects: { columnHeaders: [{ properties: { autoSizeColumnWidth: literal("true") } }] },
      visualContainerObjects: titleObjects(title),
    },
  };
}

function pageHeader(page, title, subtitle) {
  return [
    textbox(page, "title", 20, 12, 1240, 44, title, 26, "#0B2F26", "bold"),
    textbox(page, "subtitle", 20, 57, 1240, 23, subtitle, 12, "#5D706A"),
  ];
}

const visualsByPage = {};

{
  const p = pageSpecs[0].name;
  visualsByPage[p] = [
    ...pageHeader(p, "Bike Sharing Executive Overview", "Filter the report, inspect headline demand, and compare the strongest operational drivers."),
    card(p, "headline-kpis", 20, 88, 810, 125, ["Total Fleet Rentals", "Daily Average Rentals", "YoY Growth %", "Registered Share %"]),
    slicer(p, "year-filter", 850, 88, 190, "Daily_Analytics", "year_label", "Year"),
    slicer(p, "season-filter", 1060, 88, 200, "Daily_Analytics", "season_label", "Season"),
    chart(p, "daily-trend", "lineChart", 20, 228, 780, 462, "Daily rental trend", { Category: [column("Daily_Analytics", "dteday")], Y: [measure("Total Fleet Rentals")] }),
    chart(p, "season-demand", "clusteredBarChart", 820, 228, 440, 218, "Average demand by season", { Category: [column("Daily_Analytics", "season_label")], Y: [measure("Daily Average Rentals")] }),
    chart(p, "weather-demand", "clusteredBarChart", 820, 462, 440, 228, "Average demand by weather", { Category: [column("Daily_Analytics", "weather_label")], Y: [measure("Daily Average Rentals")] }),
  ];
}

{
  const p = pageSpecs[1].name;
  visualsByPage[p] = [
    ...pageHeader(p, "Commuter vs Leisure Dynamics", "Hourly usage exposes commute peaks, weekday behavior, and the registered-versus-casual rider mix."),
    card(p, "commuter-kpis", 20, 88, 580, 125, ["Hourly Average Demand", "Peak Hourly Volume", "Hourly Total Rentals"]),
    slicer(p, "period-filter", 620, 88, 220, "Hourly_Analytics", "time_period", "Time period"),
    slicer(p, "working-filter", 860, 88, 180, "Hourly_Analytics", "workingday", "Working day"),
    slicer(p, "year-filter", 1060, 88, 200, "Hourly_Analytics", "year_label", "Year"),
    chart(p, "hourly-curve", "lineChart", 20, 228, 780, 280, "Demand curve by hour and working-day status", { Category: [column("Hourly_Analytics", "hr")], Series: [column("Hourly_Analytics", "workingday")], Y: [measure("Hourly Average Demand")] }),
    chart(p, "weekday-rider-mix", "clusteredColumnChart", 820, 228, 440, 280, "Registered and casual demand by weekday", { Category: [column("Hourly_Analytics", "weekday_label")], Y: [measure("Hourly Registered Rentals"), measure("Hourly Casual Rentals")] }),
    chart(p, "period-demand", "clusteredBarChart", 20, 524, 600, 166, "Average demand by time period", { Category: [column("Hourly_Analytics", "time_period")], Y: [measure("Hourly Average Demand")] }),
    chart(p, "monthly-demand", "clusteredColumnChart", 640, 524, 620, 166, "Average hourly demand by month", { Category: [column("Hourly_Analytics", "month_label")], Y: [measure("Hourly Average Demand")] }),
  ];
}

{
  const p = pageSpecs[2].name;
  visualsByPage[p] = [
    ...pageHeader(p, "Weather & Environmental Drivers", "Compare demand with temperature, humidity, wind, season, and recorded weather conditions."),
    card(p, "weather-kpis", 20, 88, 740, 125, ["Daily Average Rentals", "Average Temperature", "Average Humidity", "Average Wind Speed"]),
    slicer(p, "weather-filter", 780, 88, 240, "Daily_Analytics", "weather_label", "Weather"),
    slicer(p, "season-filter", 1040, 88, 220, "Daily_Analytics", "season_label", "Season"),
    chart(p, "temp-demand-scatter", "scatterChart", 20, 228, 600, 280, "Temperature vs average demand by weather", { Category: [column("Daily_Analytics", "weather_label")], X: [measure("Average Temperature")], Y: [measure("Daily Average Rentals")], Size: [measure("Total Fleet Rentals")] }),
    chart(p, "weather-demand", "clusteredBarChart", 640, 228, 620, 280, "Demand penalty across weather conditions", { Category: [column("Daily_Analytics", "weather_label")], Y: [measure("Daily Average Rentals")] }),
    chart(p, "monthly-weather-demand", "lineChart", 20, 524, 760, 166, "Monthly demand with temperature context", { Category: [column("Daily_Analytics", "month_label")], Y: [measure("Daily Average Rentals")], Y2: [measure("Average Temperature")] }),
    chart(p, "environment-profile", "clusteredColumnChart", 800, 524, 460, 166, "Humidity and wind by weather", { Category: [column("Daily_Analytics", "weather_label")], Y: [measure("Average Humidity"), measure("Average Wind Speed")] }),
  ];
}

{
  const p = pageSpecs[3].name;
  visualsByPage[p] = [
    ...pageHeader(p, "ML Predictions & Demand Forecast", "Random Forest is evaluated as supporting evidence; the case study remains analysis-led, not ML-only."),
    card(p, "model-kpis", 20, 88, 600, 125, ["Model R2 Score (RF)", "Model MAE (Random Forest)", "Average Actual Rentals", "Average RF Prediction"]),
    textbox(p, "decision", 640, 91, 620, 115, "Decision: use Random Forest for operational demand planning because it explains most held-out variation and has the lowest practical error, while EDA and hypothesis tests remain the primary evidence.", 14, "#0B2F26", "bold"),
    chart(p, "rf-actual-scatter", "scatterChart", 20, 228, 600, 280, "Actual vs Random Forest prediction", { Category: [column("ML_Predictions", "Actual_Rentals")], X: [measure("Average Actual Rentals")], Y: [measure("Average RF Prediction")] }),
    chart(p, "models-curve", "lineChart", 640, 228, 620, 280, "Model comparison across actual demand", { Category: [column("ML_Predictions", "Actual_Rentals")], Y: [measure("Average RF Prediction"), measure("Average GB Prediction"), measure("Average LR Prediction")] }),
    chart(p, "rf-residuals", "clusteredColumnChart", 20, 524, 600, 166, "Random Forest residuals by actual demand", { Category: [column("ML_Predictions", "Actual_Rentals")], Y: [measure("Average RF Residual")] }),
    tableVisual(p, "prediction-table", 640, 524, 620, 166, "Prediction evidence table", [column("ML_Predictions", "Actual_Rentals"), column("ML_Predictions", "Random_Forest"), column("ML_Predictions", "Gradient_Boosting"), column("ML_Predictions", "Linear_Regression"), column("ML_Predictions", "Residual_RF")]),
  ];
}

fs.rmSync(definitionDir, { recursive: true, force: true });
fs.rmSync(path.join(reportDir, "report.json"), { force: true });
ensure(pagesDir);

writeJson(path.join(here, "Bike_Sharing_Dashboard.pbip"), {
  $schema: SCHEMA.pbip,
  version: "1.0",
  artifacts: [{ report: { path: "Bike_Sharing_Dashboard.Report" } }],
  settings: { enableAutoRecovery: true },
});

writeJson(path.join(reportDir, ".platform"), {
  $schema: SCHEMA.platform,
  metadata: { type: "Report", displayName: "Bike_Sharing_Dashboard" },
  config: { version: "2.0", logicalId: "4c3e5ad3-a905-4cfa-9635-28c27f29dd6a" },
});

writeJson(path.join(reportDir, "definition.pbir"), {
  $schema: SCHEMA.definition,
  version: "4.0",
  datasetReference: { byPath: { path: "../Bike_Sharing_Dashboard.SemanticModel" } },
});

writeJson(path.join(definitionDir, "version.json"), { $schema: SCHEMA.version, version: "2.0.0" });
writeJson(path.join(definitionDir, "report.json"), {
  $schema: SCHEMA.report,
  themeCollection: {
    baseTheme: {
      name: "Fluent2-CY26SU10",
      reportVersionAtImport: { visual: "2.11.0", report: "3.4.0", page: "2.3.1" },
      type: "SharedResources",
    },
  },
  resourcePackages: [{
    name: "SharedResources",
    type: "SharedResources",
    items: [{ name: "Fluent2-CY26SU10", path: "BaseThemes/Fluent2-CY26SU10.json", type: "BaseTheme" }],
  }],
  settings: {
    useStylableVisualContainerHeader: true,
    exportDataMode: "AllowSummarized",
    defaultDrillFilterOtherVisuals: true,
    allowChangeFilterTypes: true,
    useEnhancedTooltips: true,
    useDefaultAggregateDisplayName: true,
  },
});
writeJson(path.join(pagesDir, "pages.json"), {
  $schema: SCHEMA.pages,
  pageOrder: pageSpecs.map((p) => p.name),
  activePageName: pageSpecs[0].name,
});

let visualCount = 0;
for (const page of pageSpecs) {
  writeJson(path.join(pagesDir, page.name, "page.json"), {
    $schema: SCHEMA.page,
    name: page.name,
    displayName: page.displayName,
    displayOption: "FitToPage",
    height: 720,
    width: 1280,
  });
  for (const visual of visualsByPage[page.name]) {
    writeJson(path.join(pagesDir, page.name, "visuals", visual.name, "visual.json"), visual);
    visualCount += 1;
  }
}

console.log(`Built ${pageSpecs.length} Power BI pages with ${visualCount} native visuals.`);
