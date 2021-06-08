import Grid from "./components/Grid";
import SettingsPanel from "./components/SettingsPanel";
import Title from "./components/MainTitle";


function App() {
  return (
    <div className="App">
      <Title mainText="Foo Bar"></Title>
      <Grid></Grid>
      <SettingsPanel></SettingsPanel> 
    </div>
  );
}

export default App;
