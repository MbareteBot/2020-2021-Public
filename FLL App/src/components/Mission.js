import React, { useState, useRef } from "react";
import { StyleSheet, View, Switch, Image, Animated } from "react-native";
import { Picker } from '@react-native-picker/picker';
import CText from "./CustomText";

const CONSTANTS = require("../constants.json");

export default function Mission(props){ 

  const missionPointsLabel = require("../translations.json").es.scorer.missionPointLabel;
  const [pointsAddedByOptions, setPointsAddedByOptions] = useState(0);
  const [isMissionEnabled, setIsMissionEnabled] = useState(false);
  const [isEnabled, setIsEnabled] = useState(props.options ? [...Array(props.options.length)].fill(0) : 0);

  const handleCounter = (state, counterHandler, points) => {
    if (state) counterHandler(prevPoints => (prevPoints + points + pointsAddedByPicker));
    else { 
      counterHandler(prevPoints => ((prevPoints - points) - pointsAddedByOptions - pointsAddedByPicker));
    }
  }
  
  const toggleMissionSwitch = () => setIsMissionEnabled(prevState => {
    if (prevState) {
      setPointsAddedByOptions(0);
      setPointsAddedByPicker(0);
      setIsEnabled([]);
      for (var index in props.picker) {
        pickerHandler(index, props.picker[index]["points"][0]);
        handlePickerLastValue(index, 0);
      }
    } else {
      console.log("Picker: " + pickerValue[0]);
    }
    return !prevState 
  });

  const toggleSwitch = (index, value) => setIsEnabled(prevStates => {
    handleMultipleElements(prevStates, index, value);
  });

  const pickerHandler = (index, value) => setPickerValue(prevStates => {
    handleMultipleElements(prevStates, index, value);
  });

  const handlePickerLastValue = (index, value) => setPickerLastValue(prevStates => {
    handleMultipleElements(prevStates, index, value);
  });

  const handleMultipleElements = (prevStates, index, value) => {
    var updatedStates = prevStates;
    var state = 0;
    for (state in updatedStates) {
      if (state == index) updatedStates[index] = value;
    }
    return updatedStates;  
  }

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

  const [pickerValue, setPickerValue] = useState(props.picker ? [...Array(props.picker.length)].fill(0) : 0);
  const [pointsAddedByPicker, setPointsAddedByPicker] = useState(0);
  const [pickerLastValue, setPickerLastValue] = useState(props.picker ? [...Array(props.picker.length)].fill(undefined) : 0);

  if (!props.enable && isMissionEnabled) {
    toggleMissionSwitch();
    handleCounter(false, props.counterHandler, props.points);
  }

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
          style={{flex: 2}}
          ios_backgroundColor={"#3E3E3E"}
          value={isMissionEnabled}
          onValueChange={(switchState) => {
            toggleMissionSwitch();
            handleCounter(switchState, props.counterHandler, props.points);
          }} />
      </View>
      { isMissionEnabled ? (
      <View>
          <View style={styles.missionDescription}>
            <CText>{props.description}</CText>
          </View> 
          
        { props.picker ? (
            
            <View>
            {
              props.picker.map((picker, pickerIndex) => (
                <View style={{marginTop: 10}} key={picker["title"]} >
                  <CText>{picker["title"]}</CText>
                  <View style={styles.picker}>
                    <Picker
                      selectedValue={pickerValue[pickerIndex]}
                      onValueChange={(value) => {
                        setPointsAddedByPicker(value);
                        if (!pickerLastValue.every(val => val == "undefined")) {
                          console.log("not the first time");
                          handleCounter(false, props.counterHandler, pickerLastValue);
                        }
                        handleCounter(true, props.counterHandler, value);
                        pickerHandler(pickerIndex, value);
                        hadlePickerLastValue(pickerIndex, value);
                        }} >
                      {
                        picker["options"].map((val, index) => 
                        <Picker.Item 
                          label={val} 
                          value={picker["points"][index]} 
                          color={picker["labelsColors"][index]}
                          key={val} /> )
                      }
                  </Picker>
                  </View>
                </View>
              ))
            }
            </View>
        ): null }  

        { props.options ? (
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
                    toggleSwitch(index, switchState);
                    handleCounterOptions(switchState, props.counterHandler, props.options[1][index]);
                  }} />
                </View>
            </View>  )
            ) : null } 
          
          <View style={styles.missionPoints}>
            <CText>{missionPointsLabel}: {props.points + pointsAddedByOptions + pointsAddedByPicker}</CText>
          </View>
          

        </View>   
        ):null}
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    borderRadius: 8,
    paddingHorizontal: 25,
    paddingBottom: "4%",
    margin: 10,
    marginVertical: 4,
    backgroundColor: CONSTANTS.secondaryColor,
  },
  missionInfo: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: CONSTANTS.secondaryColor,
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
    marginTop: 20,
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
    marginTop: 5
  },

})
