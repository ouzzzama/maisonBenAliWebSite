const express = require("express");
const path = require("path");
const app = express();
const port = process.env.PORT || 3000;

// Tell the server to look ONE folder up (at the root of the repository)
const publicDir = path.join(__dirname, "..");

app.use(express.static(publicDir));

app.get("*", (req, res) => {
  res.sendFile(path.join(publicDir, "index.html"));
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
