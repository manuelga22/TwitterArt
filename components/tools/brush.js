class Brush extends Tool{
    // 30 is the default width
    constructor(color,width = 30){
        super();
        this.color = color;
        this.width = width
    }
    getColor=()=>{
       return this.color;
    }
    setColor=(color)=>{
        this.color = color;
    }
    getWidth=()=>{
        return this.width;
    }
    setWidth=(width)=>{
        this.width = width;
    }
}
