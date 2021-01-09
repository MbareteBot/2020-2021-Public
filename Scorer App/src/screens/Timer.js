import React, { useState, useEffect } from "react";
import { View, StyleSheet } from "react-native";
import Icon from "react-native-vector-icons/Ionicons";
import { elastic } from "react-native/Libraries/Animated/src/Easing";
import CText from "../components/CustomText";
import Header from "../components/Header";
import NavBar from "../components/NavBar";

const constants = require("../constants.json")

export default function Timer({ navigation }) {
  const [playButton, setPlayButton] = useState("ios-play-outline");
  const [time, setTime] = useState(["00","00","00"]);
  const [timeInterval, setTimeInterval] = useState(0);
  const [elapsedTime, setElapsedTime] = useState(0);

  const timeToString = elapsedTime => {
    let initialHours = elapsedTime / 3600000;
    let hours = Math.floor(initialHours);
    let min = Math.floor((initialHours - hours) * 60);
    let sec = Math.floor((((initialHours - hours) * 60) - min) * 60);
    let msec = Math.floor((((((initialHours - hours) * 60) - min) * 60) - sec) * 60)

    let formattedMin = min.toString().padStart(2, "0");
    let formattedSec = sec.toString().padStart(2, "0");
    let formattedMsec = msec.toString().padStart(2, "0");
    return [formattedMin,formattedSec,formattedMsec];
  }

  const handleControl = () => {
    if (playButton == "ios-play-outline") { 
      setPlayButton("ios-pause-outline");
      var startTime_ = Date.now() - elapsedTime;
      setTimeInterval(setInterval(() => {
        setElapsedTime(Date.now() - startTime_);
        setElapsedTime(prevState => {
          setTime(timeToString(prevState));
          return prevState;
        })
      }, 1))
    } else {
      setPlayButton("ios-play-outline");
      clearInterval(timeInterval);
    }
  }

  const handleStop = () => {
    setPlayButton("ios-play-outline");
    setElapsedTime(0);
    clearInterval(timeInterval);
    setTime(["00","00","00"])
  }

  return (
    <View style={styles.container}>
      <Header>
        <CText style={{fontSize: 23}}>Timer</CText>
      </Header>
      <View style={styles.stopwatchContainer}>
        <View style={styles.stopwatchElementsContainer}>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[0]}</CText>
          </View>
          <CText style={styles.stopwatchElementDividor}>:</CText>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[1]}</CText>
          </View>
          <CText style={styles.stopwatchElementDividor}>:</CText>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[2]}</CText>
          </View>
        </View>
        <View style={styles.stopwatchControls}>
            <Icon 
              name={playButton} 
              size={50} 
              color={constants.primaryBgColor} 
              onPress={() => handleControl()} />
          <Icon name="ios-stop" size={50} color={constants.primaryBgColor} onPress={() => handleStop()} />
        </View>
      </View>
      <NavBar 
        icons={[["md-calculator-outline", "stopwatch-outline"],["Scorer", "Timer"]]}
        active={[1, "#EAAB3E"]}
        pageNavigationHandler={navigation.navigate} />
    </View>
  )
} 

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
  },
  stopwatchContainer: {
    alignItems: "center",
    justifyContent: "center",
    flex: 1
  },
  stopwatchElementsContainer: {
    flexDirection: "row"
  },
  stopwatchElementContainer: {
    marginHorizontal: 5,
    backgroundColor: constants.secondaryColor,
    width: 80,
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 7
  }, 
  stopwatchElement: {
    fontSize: 40,
  },
  stopwatchElementDividor: {
    color: constants.primaryBgColor,
    fontSize: 40,
  },
  stopwatchControls: {
    flexDirection: "row",
    marginTop: 30,
    justifyContent: "space-evenly",
    width: "50%"
  }
})