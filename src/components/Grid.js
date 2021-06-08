import Arbre from "./Arbre";
import Terre from "./Terre";

export default function Grid(props) {
    return (
        <div className="grid">
            {
                props.forest.map(element => {      
                    if(element.type === "three") {
                        return <Arbre key={element.id}></Arbre>;                    
                    }
                    return <Terre key={element.id}></Terre>; 
                })
            }
        </div>
    )
}