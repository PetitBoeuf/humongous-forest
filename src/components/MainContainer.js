import Grid from "./Grid";
import SettingsPanel from "./SettingsPanel";

import { useState, useEffect } from 'react';

const THREE_PERCENTAGE = .8

export default function MainContainer(props) {
    const [loading, setLoading] = useState(true);

    const height = 15;
    const width = 30;
    
    const [forest, setForest] = useState([]);  

    useEffect( () => {
        setForest(createForest())
    },[]);
    
    function createForest() {
        setLoading(true)
        
        const forestKeys = [];

        for(let i = 0 ; i<height; i++){
            for(let j = 0 ; j<width; j++){
                let random = Math.random();

                forestKeys.push({ 
                    id: j+i*width,
                    type: random <= THREE_PERCENTAGE ? "three" : "ground"
                });
            }
        }

        setLoading(false)
        return forestKeys;
    }

    return (
        loading ? <div className="loading" /> :
        <>
            <Grid forest={forest}></Grid>
            <SettingsPanel resetFn={() => { setForest(createForest()) }}></SettingsPanel>
        </>
    )
}