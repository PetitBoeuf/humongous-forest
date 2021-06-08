import Arbre from "./Arbre";
import Terre from "./Terre";

export default function Grid(props) {
    const [forest, setForest] = props.forest;

    const handleStateClick = index => {
        let previousForest = [...forest];
        let three = {...previousForest[index]};

        if (three.currentState === "normal") three.currentState = 'fire';
        else three.currentState = 'normal';

        previousForest[index] = three;
        setForest(previousForest)
    }

    return (
        <div className="grid">
            {
                forest.map(element => {    
                    if(element.type === "three") {
                        return <Arbre key={element.id} state={element.currentState} onClick={() => handleStateClick(element.id)}></Arbre>;                    
                    }
                    return <Terre key={element.id}></Terre>; 
                })
            }
        </div>
    )
}