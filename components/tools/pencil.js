class Pencil extends Tool{
    constructor(color){
       super();
       this.color = color;
    }
    getColor=()=>{
        return this.color;
     }
    setColor=(newColor)=>{
        this.color = newColor;
    }
  
}
