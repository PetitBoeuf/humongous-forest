import { useEffect, useState } from "react";
import createForest from "./Grid";
import setForest from "./Grid";

export default function SettingsPanel(props) {
    return (
        <div className="settingsPanel">
            <button>Start <br/>arson</button>
            <button onClick={props.resetFn}>Reset <br/>forest</button>
        </div>
    )
}