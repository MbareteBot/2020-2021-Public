import React, { useState, useRef } from "react";
import { StyleSheet, View, TextInput, Keyboard } from "react-native";
import Icon from "react-native-vector-icons/Ionicons";
import CText from "../components/CustomText";
import NavBar from "../components/NavBar"

const constants = require("../constants.json")

export default function Timer({ navigation }) {
  const [playButton, setPlayButton] = useState("ios-play-outline");
  const [time, setTime] = useState([0,0,0]);
  const elapsedTime = useRef(null);
  const timeInterval = useRef(null);
  const isMounted = useRef(true);

  const formateMsec = initialMsec => {
    let sec = Math.floor((initialMsec / 1000) % 60);
    let min = Math.floor((initialMsec / (1000 * 60)) % 60);
    let hours = Math.floor((initialMsec / (1000 * 60 * 60)) % 24);

    let formattedHour = hours.toString().padStart(2, "0");
    let formattedMin = min.toString().padStart(2, "0");
    let formattedSec = sec.toString().padStart(2, "0");
    return [formattedHour.toString(),formattedMin.toString(),formattedSec.toString()];
  }

  
    const handleControl = () => {
      
      if (timeInterval.current == null) {
        elapsedTime.current = ((time[0] * 3600000) + (time[1] * 60000) + (time[2] * 1000));
        if (elapsedTime.current >= 1) {
          Keyboard.dismiss()
          setPlayButton("ios-pause-outline");
          timeInterval.current = setInterval(() => {
            elapsedTime.current -= 1000
            setTime(formateMsec(elapsedTime.current))
            if (elapsedTime.current <= 100) handleStop();
          }, 1000)} 
      } else {
        clearInterval(timeInterval.current);
        timeInterval.current = null;
        setPlayButton("ios-play-outline"); 
      }
      }
    
    
  const handleStop = () => {
    clearInterval(timeInterval.current);
    timeInterval.current = null
    setTime([0,0,0]);
    setPlayButton("ios-play-outline");
  }

  return (
    <View style={styles.container}>
       <NavBar 
        title={[["StopWatch", "Timer"],["StopWatch", "Timer"]]}
        active={[1, constants.darkYellow]}
        pageNavigationHandler={navigation.navigate} />
        <View style={styles.timerContainer}>
          <View style={styles.timerInputContainer}>
            <View style={styles.timerRow}>
              <CText style={styles.timerLabel}>HH</CText>
              <TextInput
                keyboardType="numeric" 
                value={time[0]}
                onChangeText={value => setTime([value,time[1],time[2]])}
                style={styles.timerInput}
                placeholder={"00"}
                placeholderTextColor="white"
                maxLength={2} />
            </View>
              <CText style={styles.timerInputDividor}>:</CText>
            <View style={styles.timerRow}>
              <CText style={styles.timerLabel}>MM</CText>
              <TextInput
                keyboardType="numeric" 
                value={time[1]}
                onChangeText={value => setTime([time[0],value,time[2]])}
                style={styles.timerInput}
                placeholder={"00"}
                placeholderTextColor="white"
                maxLength={2} />
            </View>
              <CText style={styles.timerInputDividor}>:</CText>
            <View style={styles.timerRow}>
              <CText style={styles.timerLabel}>SS</CText>
              <TextInput
                keyboardType="numeric" 
                value={time[2]}
                onChangeText={value => setTime([time[0],time[1],value])}
                style={styles.timerInput}
                placeholder={"00"}
                placeholderTextColor="white"
                maxLength={2} />
            </View>
          </View>
          <View style={styles.timerControls}>
            <Icon 
              name={playButton} 
              size={50} 
              color={constants.primaryBgColor} 
              onPress={() => handleControl()} />
            <Icon 
              name="ios-stop" 
              size={50} 
              color={constants.primaryBgColor} 
              onPress={() => handleStop()} />
          </View>
        </View>
        <NavBar 
          icons={[["md-calculator-outline", "stopwatch-outline"],["Scorer", "Timer"]]}
          active={[1, constants.darkYellow]}
          pageNavigationHandler={navigation.navigate}
          timeManagement={["Timer", elapsedTime.current]} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center"
  },
  timerInputContainer: {
    alignItems: "center",
    justifyContent: "center",
    flexDirection: "row"
  },
  timerContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  },
  timerInput: {
    marginHorizontal: 5,
    backgroundColor: constants.secondaryColor,
    width: 80,
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 7,
    fontSize: 40,
    color: "white",
    textAlign: "center"
  },
  timerInputDividor: {
    color: constants.primaryBgColor,
    fontSize: 40,
    marginTop: 15
  },
  timerControls: {
    flexDirection: "row",
    marginTop: 30,
    justifyContent: "space-evenly",
    width: "50%"
  },
  timerLabel: {
    color: constants.secondaryColor
  },
  timerRow: {
    alignItems: "center",
  }

})
