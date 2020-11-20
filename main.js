
   const DEFAULT_COLOR = "black";
   let canvas;
   const brush = new Brush(DEFAULT_COLOR);
   const pencil = new Pencil(DEFAULT_COLOR);
   const eraser = new Eraser();
   let currentColor = $("#colorInput").val();
   let brushWeight = $("#strokeWeightInput").val();

  function setup(){
    $("#colorInput").value = DEFAULT_COLOR
    canvas = createCanvas(400, 350);
    canvas.parent("canvas-wrapper");
    frameRate(30);
    background(255);
  };

  function draw(){
    if(mouseIsPressed && pencil.isSelected()){
      console.log(pencil.isSelected())
      stroke(pencil.getColor())
      line(mouseX,mouseY, pmouseX,pmouseY);
    }else if(mouseIsPressed && brush.isSelected() ){
      stroke(brush.getColor())
      strokeWeight(brush.getWidth())
      console.log(brush.getWidth())
      line(mouseX,mouseY, pmouseX,pmouseY);
    }else if(mouseIsPressed && eraser.isSelected()){
      strokeWeight(brushWeight);
      stroke(255);
      line(mouseX, mouseY, pmouseX, pmouseY);
    }
    noStroke();
  };
  function clearCanvas(){
    clear();
    background(255)
  }


  $("#pencilBtn").on("click",()=>{
    pencil.select()
    brush.unSelect()
  })
  $("#brushBtn").on("click",()=>{
    brush.select()
    pencil.unSelect()
  })
  $("#resetBtn").on("click", ()=>{
    clearCanvas()
  })
  $("#eraserBtn").on("click", ()=>{
    pencil.unSelect()
    brush.unSelect()
    eraser.select();
  })
  $("#colorInput").on("change",()=>{
    currentColor = $("#colorInput").val()
    pencil.setColor(currentColor)
    brush.setColor(currentColor)
  })
  $("#strokeWeightInput").on("change", ()=>{
    brushWeight = $("#strokeWeightInput").val()
    console.log(brushWeight)
    brush.setWidth(brushWeight)
  })


