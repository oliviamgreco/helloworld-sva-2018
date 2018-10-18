var r, g, b;

function setup() {
  createCanvas(720, 400);
  r = random(255); // Picks colors randomly
  g = random(255);
  b = random(255);
}
  // Draws a circle
function draw() {
  background(155, 244, 227);

  strokeWeight(2);
  stroke(r, g, b);
  fill(r, g, b, 127);
  ellipse(360, 200, 200, 200);
}

// When the user clicks the mouse
function mousePressed() {
  // Check if mouse is inside the circle
  var d = dist(mouseX, mouseY, 360, 200);
  if (d < 100) {
    // Picks new random color values
    r = random(255);
    g = random(255);
    b = random(255);
  }

}