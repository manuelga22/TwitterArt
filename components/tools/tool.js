class Tool{
    constructor(){
        this.selected=false;
    }
    isSelected=()=>{
        return this.selected;
    }
    select=()=>{
        this.selected=true;
    }
    unSelect=()=>{
        this.selected=false;
    }

}