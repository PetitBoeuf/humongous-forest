export default function SettingsPanel(props) {
    return (
        <div className="settingsPanel">
            <button>Start <br/>arson</button>
            <button onClick={props.resetFn}>Reset <br/>forest</button>
        </div>
    )
}