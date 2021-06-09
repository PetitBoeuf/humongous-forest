import Arbre from "./Arbre";
import Terre from "./Terre";

export default function Grid(props) {
    const [forest, setForest] = props.forest;

    const handleStateClick = index => {
        let previousForest = [...forest];
        let tree = {...previousForest[index]};

        if (tree.currentState === "normal") tree.currentState = 'fire';
        else tree.currentState = 'normal';

        previousForest[index] = tree;
        setForest(previousForest)
    }

    return (
        <div className="grid">
            {
                forest.map(element => {    
                    if(element.type === "tree") {
                        return <Arbre key={element.id} state={element.currentState} onClick={() => handleStateClick(element.id)}></Arbre>;                    
                    }
                    return <Terre key={element.id}></Terre>; 
                })
            }
        </div>
    )
}