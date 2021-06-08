import forestImage from '../forest-smashicons.png';
import forestFireImage from '../forest-fire-smashicons.png';

export default function Arbre(props) {
    const state = props.state
    
    return (
        <div className={`container tree-container ${state}`} onClick={props.onClick}>
                <img 
                    src={state === "normal" ? forestImage : forestFireImage}
                    alt={state === "normal" ? "Three" : "Three with fire"}
                />
        </div>  
    )
}