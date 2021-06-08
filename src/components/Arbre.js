import { useState } from "react";
import forestImage from '../forest-smashicons.png';
import forestFireImage from '../forest-fire-smashicons.png';

export default function Arbre() {
    
    const [currentForestState, setFire] = useState("normal");
    
    function burnTree(){
        if(currentForestState === "normal") setFire("setImage");
        else setFire("normal");
    }
    
    return (
        // <div className= {`arbre${currentForestState === 1 ? " feu" : ""} `} >
        <div className="container tree-container" onClick={burnTree}>
                <img 
                    src={currentForestState === "normal" ? forestImage : forestFireImage}
                    alt={currentForestState === "normal" ? "Three" : "Three with fire"}
                />
        </div>  
    )
}