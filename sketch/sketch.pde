void setup() {
  size(200, 200);
}
void draw() {
  background(0);
  text("進捗どうですか?", width/3-10+6*noise(random(1)), height/2-3+6*noise(random(1)));
  if((frameCount <= 600)&&(frameCount % 15 == 0))saveFrame("####.png");
  if(frameCount > 600) exit();
}