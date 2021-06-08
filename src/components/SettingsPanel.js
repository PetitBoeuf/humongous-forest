import { useEffect, useState } from "react";
import createForest from "./Grid";
import setForest from "./Grid";

export default function SettingsPanel(props) {
    return (
        <div className="settingsPanel">
            <button>Start <br></br>arson</button>
            <button onClick={
                    setForest(createForest()) 
            }>Reset <br></br>forest</button>
        </div>
    )
}