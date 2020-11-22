   const DEFAULT_COLOR = "black";
   let canvas;
   const brush = new Brush(DEFAULT_COLOR);
   const pencil = new Pencil(DEFAULT_COLOR);
   const eraser = new Eraser();
   let topLayer;
   let imageInput;

   let currentColor = $("#colorInput").val();
   let brushWeight = $("#strokeWeightInput").val();

  function setup(){
    $("#colorInput").value = DEFAULT_COLOR

  
    //second layer where painting is done
    canvas = createCanvas(400, 350);
     canvas.parent("canvas-wrapper");
     background(255)

    //transparent layer behind  canvas
    topLayer = createGraphics(400,350);
    topLayer.parent("canvas-wrapper")
    topLayer.clear();
    

    frameRate(30);

  };

  function draw(){
    if(imageInput){
      loadImage(imageInput, drawImage)
    }
    if(mouseIsPressed && pencil.isSelected()){
      topLayer.stroke(pencil.getColor())
      topLayer.strokeWeight(1)
      topLayer.line(mouseX,mouseY, pmouseX,pmouseY);
      image(topLayer,0,0) 
    }else if(mouseIsPressed && brush.isSelected() ){
      topLayer.stroke(brush.getColor())
      topLayer.strokeWeight(brush.getWidth())
      topLayer.line(mouseX,mouseY, pmouseX,pmouseY);
      image(topLayer,0,0) 
    }else if(mouseIsPressed && eraser.isSelected()){
      
        console.log("erase")
        //topLayer.setAlpha(255);
        topLayer.stroke("transparent")
        topLayer.strokeWeight(brushWeight);
        topLayer.line(mouseX, mouseY, pmouseX, pmouseY);
   image(topLayer,0,0) 
    }
      
      

  };
  function tweet(){
      let image = canvas.toDataURL("image/png");
      
      axios.post("/upload",{picture:image}).then((res)=>{console.log(res)})
     
  }
  function clearCanvas(){
    clear();
    background(255)
    topLayer.clear();
  };
  function drawImage(img){
    background(img)
    image(topLayer,0,0)
  }
  $("#pencilBtn").on("click",()=>{
    pencil.select()
    brush.unSelect()
    eraser.unSelect()
  })
  $("#brushBtn").on("click",()=>{
    brush.select()
    pencil.unSelect()
    eraser.unSelect()
  })
  $("#resetBtn").on("click", ()=>{
    clearCanvas();
    pencil.unSelect();
    brush.unSelect()
    eraser.unSelect()
  })
  $("#eraserBtn").on("click", ()=>{
    pencil.unSelect()
    brush.unSelect()
    eraser.select();
  }) 
  $("#saveBtn").on("click",()=>{
      saveCanvas(canvas, "newImage", 'jpg')
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
$("tweetBtn").on("click",()=>{
    tweet()
})
  $("#imageInput").on("change",()=>{
    imageInput = $("#imageInput")[0].files[0]
    
    const reader = new FileReader();
    reader.addEventListener("load",()=>{
      localStorage.setItem("recent-image", reader.result)
    })

    reader.readAsDataURL(imageInput)

    imageInput = localStorage.getItem("recent-image")

  })



