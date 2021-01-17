import React, { useState, useRef } from 'react';
import { StyleSheet, View, ScrollView, StatusBar, TouchableOpacity } from 'react-native';
import CText from '../components/CustomText';
import Mission from '../components/Mission';
import NavBar from '../components/NavBar';
import Header from '../components/Header';



export default function Scorer({ navigation, route }) {

  try {
    //SETS WICH SCREEN THE "TIME" BUTTON SHOULD TAKE USER TO
    var lastScreen = route.params.screenName;
  } catch(e) {
    var lastScreen = "StopWatch";
  }

  const [currentScore, setCurrentScore] = useState(0);
  const [enagleAllMissions, setEnableAllMissions] = useState(true);
  const mainRoot = "../assets/missions/";
  const CONSTANTS = require("../constants.json");
  const FULLCONTENT = require("../translations.json");
  const [CONTENT, setContent] = useState(FULLCONTENT.es)


  return (
    <View style={styles.container}>
      <StatusBar 
        style="light" 
        backgroundColor="#3B4457"/>
        <Header>
            <View style={{flexDirection: "row"}}>
              <CText style={{fontSize: 23}}>{CONTENT.scorer.title}: </CText>
              <CText style={{fontSize: 23, color: CONSTANTS.darkYellow}}>{currentScore}</CText>
            </View>
        </Header>
      <ScrollView>
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m0-min.png")}
          name={CONTENT.scorer.m00.name} 
          description={CONTENT.scorer.m00.description}
          counterHandler={setCurrentScore}
          points={25} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m1-min.png")}
          name={CONTENT.scorer.m01.name} 
          description={CONTENT.scorer.m01.description}
          counterHandler={setCurrentScore}
          points={20} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m2-min.png")}
          name={CONTENT.scorer.m02.name} 
          description={CONTENT.scorer.m02.description}
          counterHandler={setCurrentScore}
          points={10}
          picker={[CONTENT.scorer.m02.case1.name,
                  [CONTENT.scorer.m02.case1.option1, CONTENT.scorer.m02.case1.option2, CONTENT.scorer.m02.case1.option3],
                  [0,5,10],
                  [CONSTANTS.magenta, CONSTANTS.yellow, CONSTANTS.black]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m3-min.png")}
          name={CONTENT.scorer.m03.name} 
          description={CONTENT.scorer.m03.description}
          counterHandler={setCurrentScore}
          points={5}
          picker={[CONTENT.scorer.m03.case1.name,
                  [CONTENT.scorer.m03.case1.option1, CONTENT.scorer.m03.case1.option2],
                  [0,15],
                  [CONSTANTS.black, CONSTANTS.black]]} 
          options={[[CONTENT.scorer.m03.case2,CONTENT.scorer.m03.case3],
                  [10,20]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m4-min.png")}
          name={CONTENT.scorer.m04.name} 
          description={CONTENT.scorer.m04.description}
          counterHandler={setCurrentScore}
          points={10}
          picker={[CONTENT.scorer.m04.case1.name,
                  [CONTENT.scorer.m04.case1.option1,CONTENT.scorer.m04.case1.option2,CONTENT.scorer.m04.case1.option3, CONTENT.scorer.m04.case1.option4],
                  [0,10,20,30],
                  [CONSTANTS.black, CONSTANTS.black, CONSTANTS.black]]} 
          options={[[CONTENT.scorer.m04.case2],
                  [15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m5-min.png")}
          name={CONTENT.scorer.m05.name} 
          description={CONTENT.scorer.m05.description}
          counterHandler={setCurrentScore}
          points={10}
          picker={[CONTENT.scorer.m05.case1.name,[CONTENT.scorer.m05.case1.option1,CONTENT.scorer.m05.case1.option2],
                  [15,20],
                  [CONSTANTS.black, CONSTANTS.black]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m6-min.png")}
          name={CONTENT.scorer.m06.name} 
          description={CONTENT.scorer.m06.description}
          counterHandler={setCurrentScore}
          points={0}
          options={[[CONTENT.scorer.m06.case1,CONTENT.scorer.m06.case2],
                    [15,15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m7-min.png")}
          name={CONTENT.scorer.m07.name} 
          description={CONTENT.scorer.m07.description}
          counterHandler={setCurrentScore}
          points={20} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m8-min.png")}
          name={CONTENT.scorer.m08.name} 
          description={CONTENT.scorer.m08.description}
          counterHandler={setCurrentScore}
          points={25}
          picker={[CONTENT.scorer.m08.case1,
                  [...Array(18)].map((a,b) => ((b-1) + 1).toString()),
                  [...Array(18)].map((a,b) => (((b-1) + 1) * 5)),
                  [...Array(18)].fill(CONSTANTS.black)]}
          options={[[CONTENT.scorer.m08.case2,CONTENT.scorer.m08.case3], 
                    [5,10]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m9-min.png")}
          name={CONTENT.scorer.m09.name} 
          description={CONTENT.scorer.m09.description}
          counterHandler={setCurrentScore}
          points={0}
          picker={[CONTENT.scorer.m09.case1.name,
                  [CONTENT.scorer.m09.case1.option1,CONTENT.scorer.m09.case1.option2,CONTENT.scorer.m09.case1.option3],
                  [0,5,10],
                  [CONSTANTS.black, CONSTANTS.black, CONSTANTS.black]]}
          options={[[CONTENT.scorer.m09.case2,CONTENT.scorer.m09.case3],
                    [10,15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m10-min.png")}
          name={CONTENT.scorer.m10.name} 
          description={CONTENT.scorer.m10.description}
          counterHandler={setCurrentScore}
          points={15} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m11-min.png")}
          name={CONTENT.scorer.m11.name} 
          description={CONTENT.scorer.m11.description}
          counterHandler={setCurrentScore}
          points={5}
          picker={[CONTENT.scorer.m11.case1.name,
                  [CONTENT.scorer.m11.case1.option1, CONTENT.scorer.m11.case1.option2, CONTENT.scorer.m11.case1.option3, CONTENT.scorer.m11.case1.option4, CONTENT.scorer.m11.case1.option5, CONTENT.scorer.m11.case1.option6],
                  [0,5,10,15,20,25],
                  ["gray", "red", "orange", "rgb(2304,234,0)", "lightgreen", "darkgreen"]]} />    
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m12-min.png")}
          name={CONTENT.scorer.m12.name} 
          description={CONTENT.scorer.m12.description}
          counterHandler={setCurrentScore}
          points={0}
          options={[[CONTENT.scorer.m12.case1,CONTENT.scorer.m12.case2],
                    [15,15]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m13-min.png")}
          name={CONTENT.scorer.m13.name} 
          description={CONTENT.scorer.m13.description}
          counterHandler={setCurrentScore}
          points={10}
          picker={[CONTENT.scorer.m13.case1.name,
                  [CONTENT.scorer.m13.case1.option1,CONTENT.scorer.m13.case1.option2,CONTENT.scorer.m13.case1.option3],
                  [0,5,10],
                  ["blue", CONSTANTS.magenta, "rgb(2304,234,0)"]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m14-min.png")}
          name={CONTENT.scorer.m14.name} 
          description={CONTENT.scorer.m14.description}
          counterHandler={setCurrentScore}
          points={5}
          picker={[CONTENT.scorer.m14.case1.name,
                  [CONTENT.scorer.m14.case1.option1,CONTENT.scorer.m14.case1.option2,CONTENT.scorer.m14.case1.option3,CONTENT.scorer.m14.case1.option4,CONTENT.scorer.m14.case1.option5,CONTENT.scorer.m14.case1.option6],
                  [0,5,10,15,20,25],
                  [CONSTANTS.black, CONSTANTS.black,CONSTANTS.black, CONSTANTS.black,CONSTANTS.black, CONSTANTS.black]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m15-min.png")}
          name={CONTENT.scorer.m15.name} 
          description={CONTENT.scorer.m15.description}
          counterHandler={setCurrentScore}
          points={5}
          picker={[CONTENT.scorer.m15.case1.name,
                  [CONTENT.scorer.m15.case1.option1,CONTENT.scorer.m15.case1.option2,CONTENT.scorer.m15.case1.option3,CONTENT.scorer.m15.case1.option4,CONTENT.scorer.m15.case1.option5,CONTENT.scorer.m15.case1.option6],
                  [0,5,15,25,40,55],
                  [CONSTANTS.black, CONSTANTS.black,CONSTANTS.black,CONSTANTS.black,CONSTANTS.black]]} />
        <View style={styles.footer}>
          <TouchableOpacity
            onPressIn={() => setEnableAllMissions(false)}
            onPressOut={() => setEnableAllMissions(true)} >
            <View style={styles.button}>
              <CText>Reset</CText>
            </View>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => {
              if (CONTENT == FULLCONTENT.es) setContent(FULLCONTENT.en)
              else setContent(FULLCONTENT.es)
            }} >
            <View style={styles.button}>
              <CText>Cambia Idioma(solo prueba)</CText>
            </View>
          </TouchableOpacity>
        </View>
      </ScrollView>
      <View>
        <NavBar 
          icons={[["md-calculator-outline", "stopwatch-outline"],
                  ["Scorer",  lastScreen == "Timer" ? "Timer" : "StopWatch"]]}
          active={[0, CONSTANTS.darkYellow]}
          pageNavigationHandler={navigation.navigate} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#3B4457",
    position: "relative"
  },
  header: {
    alignItems: "center",
    padding: 20,
  },
  headerTitle: {
    fontFamily: "normal",
  },
  button: {
    backgroundColor: "gray",
    padding: 10
  },
  footer: {
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: "rgba(255,255,255,0.9)",
  },
});
