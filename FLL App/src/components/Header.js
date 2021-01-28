import React from "react";
import { StyleSheet, View, StatusBar } from "react-native";

const CONSTANTS = require("../constants.json")

export default function Header(props) {
  return (
    
    <View style={[styles.container, props.style]}>
      <StatusBar 
        style="light" 
        backgroundColor={CONSTANTS.primaryBgColor} />
      { props.children }
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
    backgroundColor: CONSTANTS.primaryBgColor,
    width: "100%",
  }
})