import React, { useState, useRef } from "react";
import { View, StyleSheet, StatusBar, Animated } from "react-native";
import Icon from "react-native-vector-icons/Ionicons";
import CText from "../components/CustomText";
import NavBar from "../components/NavBar";

const CONSTANTS = require("../constants.json");

export default function StopWatch({ navigation, route }) {

  const fadeAnim = useRef(new Animated.Value(1)).current;
  const fadeIn = () => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true
    }).start(() => setEnableInput("auto"));
  };

  const fadeOut = () => {
    Animated.timing(fadeAnim, {
      toValue: 0,
      duration: 500,
      useNativeDriver: true
    }).start(() => setEnableInput("none"));
  };

  const [playButton, setPlayButton] = useState("ios-play-outline");
  const [time, setTime] = useState(["00","00","00"]);
  const [timeInterval, setTimeInterval] = useState(0);
  const [elapsedTime, setElapsedTime] = useState(0);
  const [enableInput, setEnableInput] = useState("auto");

  const msecToString = initialMsec => {
    let msec = Math.floor((initialMsec % 1000) / 10);
    let sec = Math.floor((initialMsec / 1000) % 60);
    let min = Math.floor((initialMsec / (1000 * 60)) % 60);

    let formattedMin = min.toString().padStart(2, "0");
    let formattedSec = sec.toString().padStart(2, "0");
    let formattedMsec = msec.toString().padStart(2, "0");
    return [formattedMin.toString(),formattedSec.toString(),formattedMsec.toString()];
  }

  const handleControl = () => {
      if (playButton == "ios-play-outline") { 
        fadeOut();
        setPlayButton("ios-pause-outline");
        var startTime_ = Date.now() - elapsedTime;
        setTimeInterval(setInterval(() => {
          setElapsedTime(Date.now() - startTime_);
          setElapsedTime(prevState => {
            setTime(msecToString(prevState));
            return prevState;
          })
        }, 50))
      } else {
        setPlayButton("ios-play-outline");
        clearInterval(timeInterval);
      }
  }

  const handleStop = () => {
    fadeIn();
    setPlayButton("ios-play-outline");
    setElapsedTime(0);
    clearInterval(timeInterval);
    setTime(["00","00","00"]);
  }

  return (
    <View style={styles.container}>
      <StatusBar 
        style="light" 
        backgroundColor="#3B4457"/>
      <Animated.View style={{opacity: fadeAnim}} pointerEvents={enableInput}>
        <NavBar 
          title={[[route.params.LABELS.stopwatch, route.params.LABELS.timer],["StopWatch", "Timer"]]}
          active={[0, CONSTANTS.darkYellow]}
          pageNavigationHandler={navigation.navigate}
          contentLabels={route.params.LABELS} />
      </Animated.View>
      
      <View style={styles.stopwatchContainer}>
        <View style={styles.stopwatchElementsContainer}>
            <View style={styles.stopWatchRow}>
            <CText style={styles.stopWatchLabel}>MM</CText>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[0]}</CText>
            </View>
          </View>
          <CText style={styles.stopwatchElementDividor}>:</CText>
            <View style={styles.stopWatchRow}>
            <CText style={styles.stopWatchLabel}>SS</CText>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[1]}</CText>
            </View>
          </View>
          <CText style={styles.stopwatchElementDividor}>:</CText>
            <View style={styles.stopWatchRow}>
            <CText style={styles.stopWatchLabel}>MS</CText>
          <View style={styles.stopwatchElementContainer}>
            <CText style={styles.stopwatchElement}>{time[2]}</CText>
            </View>
          </View>
        </View>
        <View style={styles.stopwatchControls}>
          <Icon 
            name={playButton} 
            size={50} 
            color={CONSTANTS.primaryBgColor} 
            onPress={() => handleControl()} />
          <Icon 
            name="ios-stop" 
            size={50} 
            color={CONSTANTS.primaryBgColor} 
            onPress={() => handleStop()} />
        </View>
      </View>
      <Animated.View style={{opacity: fadeAnim}} pointerEvents={enableInput}>
      <NavBar 
          icons={[["md-calculator-outline", "stopwatch-outline", "book-outline"],
                  ["Scorer", "Timer", "Docs"]]}
          active={[1, CONSTANTS.darkYellow]}
          pageNavigationHandler={ navigation.navigate }
          contentLabels={route.params.LABELS} />
      </Animated.View>
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
    backgroundColor: CONSTANTS.secondaryColor,
    width: 80,
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 7
  }, 
  stopwatchElement: {
    fontSize: 40,
  },
  stopwatchElementDividor: {
    color: CONSTANTS.primaryBgColor,
    fontSize: 40,
    marginTop: 15
  },
  stopwatchControls: {
    flexDirection: "row",
    marginTop: 30,
    justifyContent: "space-evenly",
    width: "50%"
  },
  stopWatchLabel: {
    color: CONSTANTS.secondaryColor
  },
  stopWatchRow: {
    alignItems: "center",
  }
})