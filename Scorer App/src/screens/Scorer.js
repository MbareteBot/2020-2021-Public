import React, { useState } from 'react';
import { StyleSheet, View, ScrollView, Button, StatusBar } from 'react-native';
import CText from '../components/CustomText';
import Mission from '../components/Mission';
import NavBar from '../components/NavBar';
import Header from '../components/Header';
import { set } from 'react-native-reanimated';
import { TouchableOpacity } from 'react-native-gesture-handler';

const constants = require("../constants.json")

export default function Scorer({ navigation }) {
  const [currentScore, setCurrentScore] = useState(0);
  const [enagleAllMissions, setEnableAllMissions] = useState(true);
  const setTrue = () => setEnableAllMissions(true);
  const mainRoot = "../assets/missions/";
  return (
    <View style={styles.container}>
      <StatusBar 
        style="light" 
        backgroundColor="#3B4457"/>
        <Header>
            <View style={{flexDirection: "row"}}>
              <CText style={{fontSize: 23}}>Scorer: </CText>
              <CText style={{fontSize: 23, color: constants.darkYellow}}>{currentScore}</CText>
            </View>
        </Header>
      <ScrollView>
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m0.png")}
          name="M00 | Equipment Inspection Bonus" 
          description="If all your equipment fits in the small inspection space"
          counterHandler={setCurrentScore}
          points={25} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m1.png")}
          name="M01 | Innovation Project" 
          description="The robot moves
          your Innovation
          Project onto the
          RePLAY logo or the
          gray area around
          the bench (M04)."
          counterHandler={setCurrentScore}
          points={20} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m2.png")}
          name="M02 | Step Counter" 
          description="The robot slides the
          step counter slow
          and steady. The
          farther the “walk,”
          the better."
          counterHandler={setCurrentScore}
          points={10}
          pickerOptions={[["Magenta", "Yellow", "Middle"],
                          [0,5,10],
                          [constants.magenta, constants.yellow, constants.black]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m3.png")}
          name="M03 | Slide" 
          description="The robot slides the
          people (called “slide
          figures”) down the
          slide and moves
          them to other areas."
          counterHandler={setCurrentScore}
          points={5}
          pickerOptions={[["1 Figure", "2 Figures"],
                          [0,15],
                          [constants.black, constants.black]]} 
          options={[["If a slide figure is completely in home","If a slide figure is held completely off the mat by the heavy tire and is touching nothing else"],
                  [10,20]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m4.png")}
          name="M04 | Bench" 
          description="The robot removes
          the backrest,
          flattens the bench,
          and gets cubes
          into the hopscotch
          spaces."
          counterHandler={setCurrentScore}
          points={10}
          pickerOptions={[["1", "2", "3"],
                          [10,20,30],
                          [constants.black, constants.black, constants.black]]} 
          options={[["If the backrest is completely out of both of its holes"],
                  [15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m5.png")}
          name="M05 | Basketball" 
          description="The robot raises the
          crate up the post
          and gets a cube into
          it."
          counterHandler={setCurrentScore}
          points={10}
          pickerOptions={[["Middle height’s white stopper", "Height’s white stopper"],
                          [15,20],
                          [constants.black, constants.black]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m6.png")}
          name="M06 | Pull-Up Bar" 
          description="The robot passes completely under the bar any time. Separately, it is held off the mat by the bar at the end of the match."
          counterHandler={setCurrentScore}
          points={0}
          options={[["If the robot passes completely through the pull-up bar’s upright frame at any time", "If the pull-up bar holds 100% of the robot up off the mat at the end of the match"],
                    [15,15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m7.png")}
          name="M07 | Robot Dance" 
          description="The robot is dancing
          on the dance floor
          at the end of the
          match."
          counterHandler={setCurrentScore}
          points={20} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m8.png")}
          name="M08 | Boccia" 
          description="If both share models have sent only one cube
          anywhere onto the opposing field and those cubes
          color-match each other"
          counterHandler={setCurrentScore}
          points={25}
          pickerOptions={[[...Array(18)].map((a,b) => ((b-1) + 1).toString()),
                          [...Array(18)].map((a,b) => (((b-1) + 1) * 5)),
                          [...Array(18)].fill(constants.black)]}
          options={[["If there are cubes completely in your frame or target", "If there is at least one yellow cube completely in your target"], 
                    [5,10]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m9.png")}
          name="M09 | Tire Flip" 
          description="The robot flips
          tires so their white
          centers face up and
          moves them into
          their large target
          circle.
          Select the amount of tires completely in the large target circle."
          counterHandler={setCurrentScore}
          points={0}
          pickerOptions={[["0","1","2"],
                          [0,5,10],
                          [constants.black, constants.black, constants.black]]}
          options={[["If the light (blue tread) tire is white center up", "If the heavy (black tread) tire is white center up:"],
                    [10,15]]} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m10.png")}
          name="M10 | Cell Phone" 
          description="The robot flips the
          cell phone white
          side up (resting on only the mat)."
          counterHandler={setCurrentScore}
          points={15} />
        <Mission
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m11.png")}
          name="M11 | Treadmill" 
          description="The robot spins
          the rollers to move
          the pointer as
          far clockwise as
          possible."
          counterHandler={setCurrentScore}
          points={5}
          pickerOptions={[["Gray", "Red", "Orange", "rgb(2304,234,0)", "Light green", "Dark green"],
                          [0,5,10,15,20,25],
                          ["gray", "red", "orange", "rgb(2304,234,0)", "lightgreen", "darkgreen"]]} />
      
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m12.png")}
          name="M12 | Row Machine" 
          description="The robot moves
          the free wheel out of
          the large circle and
          into the small target
          circle. Select where the free wheel is."
          counterHandler={setCurrentScore}
          points={0}
          options={[["Completely outside the large circle", "Completely in the small circle"],
                    [15,15]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m13.png")}
          name="M13 | Weight Machine" 
          description="During the match,
          the robot moves the
          lever until the little
          yellow stopper falls.
          Select the lever setting"
          counterHandler={setCurrentScore}
          points={10}
          pickerOptions={[["Blue", "Magenta", "Yellow"],
                          [0,5,10],
                          ["blue", constants.magenta, "rgb(2304,234,0)"]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m14.png")}
          name="M14 | Health Units" 
          description="The robot collects
          health units from
          around the field
          and moves them to
          target areas."
          counterHandler={setCurrentScore}
          points={5}
          pickerOptions={[["1","2","3","4","5","6"],
                          [0,5,10,15,20,25],
                          [constants.black, constants.black,constants.black, constants.black,constants.black, constants.black]]} />
        <Mission 
          enable={enagleAllMissions} 
          imgSource={require(mainRoot + "m15.png")}
          name="M15 | Precision" 
          description="The less often you
          interrupt the robot
          outside home, the
          more points you
          keep.
          Select how many tokens are left."
          counterHandler={setCurrentScore}
          points={5}
          pickerOptions={[["1","2","3","4","5","6"],
                          [0,5,15,25,40,55],
                          [constants.black, constants.black,constants.black,constants.black,constants.black]]} />

        <View style={styles.footer}>
          <TouchableOpacity
            onPressIn={() => setEnableAllMissions(false)}
            onPressOut={() => setEnableAllMissions(true)} >
            <View style={styles.button}>
              <CText>Reset</CText>
            </View>
          </TouchableOpacity>
        </View>
      </ScrollView>

      <View>
        <NavBar 
          icons={[["md-calculator-outline", "stopwatch-outline"],["Scorer", "Timer"]]}
          active={[0, constants.darkYellow]}
          pageNavigationHandler={navigation.navigate} />
      </View>
      
    </View>

  );
}

/*
      <View style={styles.totalScore}>
        <CText>Total: {currentScore}</CText>

      </View> */
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
  }
});