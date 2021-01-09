import React, { useState } from "react";
import { StyleSheet, View, Switch, Image } from "react-native";
import { Picker } from '@react-native-picker/picker';
import CText from "./CustomText"

const constants = require("../constants.json")

export default function Mission(props) {

  /*
    Default args: {imgSource, name, description, counterHandler, points}
    options args: {[["name1", "name2", "etc"], [pointname1, pointname2, etc]]} 
  */
  const [pointsAddedByOptions, setPointsAddedByOptions] = useState(0);
  const [isMissionEnabled, setIsMissionEnabled] = useState(false);
  const [isEnabled, setIsEnabled] = useState([]);

  const handleCounter = (state, counterHandler, points) => {
    if (state) counterHandler(prevPoints => (prevPoints + points + pointsAddedByPicker));
    else { 
      counterHandler(prevPoints => ((prevPoints - points) - pointsAddedByOptions - pointsAddedByPicker));
    }
  }
  const toggleMissionSwitch = () => setIsMissionEnabled(prevState => {
    if (props.state != undefined) props.state(!prevState);
    if (prevState) {
      setPointsAddedByOptions(0);
      setPointsAddedByPicker(0);
      setIsEnabled([]);
      if (props.pickerOptions) {
        setPickerValue(props.pickerOptions[1][0]);
        setPickerLastValue(0);
      }
    } 
    return !prevState
  });
  const toggleSwitch = (index) => setIsEnabled(prevStates => {
    if (prevStates.length == 0) for (let i = 0; i < props.options[0].length; i++) prevStates.push(false)
    var updatedStates = prevStates;
    var state = 0;
    for (state in updatedStates) {
      if (state == index) updatedStates[index] = !updatedStates[index];
    }
    return updatedStates;
  });
  const handleCounterOptions = (state, counterHandler, points) => {
    if (state) {
      counterHandler(prevPoints => prevPoints + points);
      setPointsAddedByOptions(prevState => prevState + points);
    }
    else {
      counterHandler(prevPoints => prevPoints - points);
      setPointsAddedByOptions(prevState => prevState - points);
    }
  }
  const [pickerValue, setPickerValue] = useState();
  const [pointsAddedByPicker, setPointsAddedByPicker] = useState(0);
  const [pickerLastValue, setPickerLastValue] = useState("NaN");
  return (
    <View style={styles.container}>
      <View style={styles.options}>
        <View style={styles.missionInfo}>
          { props.imgSource != undefined ? (
            <View style={styles.missionImg}>
                <Image
                  source={props.imgSource}
                  style={{width: 60, height: 60, borderRadius: 2, backgroundColor: "white"}}
                />
              </View>
            ) : null }
            <CText style={{fontSize: 17}}>{props.name}</CText>
        </View>
        <Switch
          trackColor={{ false: "gray", true: "lightblue" }}
          thumbColor={"white"}
          style={{flex: 1}}
          ios_backgroundColor={"#3E3E3E"}
          value={isMissionEnabled}
          onValueChange={(switchState) => {
            toggleMissionSwitch();
            handleCounter(switchState, props.counterHandler, props.points);
          }} />
      </View>

      { isMissionEnabled ? (
        <View style={styles.missionDescription}>
          <CText>{props.description}</CText>
        </View> ) : null }

      { props.pickerOptions && isMissionEnabled ? (
          <View style={styles.picker}>
            <Picker
              selectedValue={pickerValue}
              onValueChange={(value) => {
                setPointsAddedByPicker(value)
                console.log("value changed " + value)
                if (pickerLastValue != "NaN") {
                  handleCounter(false, props.counterHandler, pickerLastValue)
                }
                handleCounter(true, props.counterHandler, value)
                setPickerValue(value)
                setPickerLastValue(value)
                }} >
              {props.pickerOptions[0].map((val, index) => 
                <Picker.Item 
                  label={val} 
                  value={props.pickerOptions[1][index]} 
                  color={props.pickerOptions[2][index]}
                  key={Math.random()} />
              )}
            </Picker>
          </View>
      ): null }  

      { props.options && isMissionEnabled ? (
        props.options[0].map((value, index) => 
          <View style={styles.options} key={index.toString()}>
            <View style={styles.optionDescription}>
            <CText>{value}</CText>
            </View>
            <View>
              <Switch
                trackColor={{ false: "gray", true: "lightblue" }}
                thumbColor={"white"}
                ios_backgroundColor={"#3e3e3e"}
                value={isEnabled[index]}
                onValueChange={(switchState) => {
                  toggleSwitch(index);
                  handleCounterOptions(switchState, props.counterHandler, props.options[1][index]);
                }} />
              </View>
          </View>  
        )) : null } 

        { isMissionEnabled ? (
          <View style={styles.missionPoints}>
            <CText>Points: {props.points + pointsAddedByOptions + pointsAddedByPicker}</CText>
          </View>
        ) : null}      

    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    borderRadius: 8,
    paddingHorizontal: 25,
    paddingTop: 10,
    paddingBottom: 20,
    margin: 10,
    marginVertical: 4,
    backgroundColor: constants.secondaryColor,
  },
  missionInfo: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#424C61",
    flex: 2
  },
  missionImg: {
    paddingRight: 10,
    marginRight: 10,
    borderRightWidth: 1,
    borderRightColor: "rgba(255,255,255,0.3)"
  },
  missionDescription: {
    alignItems: "center",
    marginTop: 10,
  },
  options: {
    marginTop: 10,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  optionDescription: {
    flex: 1
  },
  missionPoints: {
    alignItems: "center",
    marginTop: 20,
    borderBottomWidth: 1,
    borderBottomColor: "white"
  },
  picker: {
    borderWidth: 1,
    backgroundColor: "#fff",
    marginTop: 10
  },

})
