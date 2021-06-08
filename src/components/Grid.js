import Arbre from "./Arbre";
import Terre from "./Terre";
import { useEffect, useState } from "react";

export default function Grid(props) {

    const height = 15;
    const width = 30;
    var forestKeys = [];

    const [forest, setForest] = useState(createForest);


    useEffect( () => {
        setForest(createForest());
    },[]);
    
    function createForest() {
        for(let i = 0 ; i<height; i++){
            for(let j = 0 ; j<width; j++){
                // setForest(old => {
                //     return [...old, j+i*width]
                // });
                forestKeys.push(j+i*width);
            }
        }
        return forestKeys;
    }

    return (
        <div className="grid">
            {
                forest.map((forestElement) => {           
                    let random = Math.random();
                    if(random < 0.80){
                        return <Arbre key={forestElement}></Arbre>;                    
                    }
                    return <Terre key={forestElement}></Terre>;
                })
            }
        </div>
    )

}