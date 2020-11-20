class Pencil extends Tool{
    constructor(color){
       super();
       this.color = color;
    }
    getColor=()=>{
        console.log(this.color)
        return this.color;
     }
    setColor=(newColor)=>{
        this.color = newColor;
    }
  
}
