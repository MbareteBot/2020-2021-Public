import React from "react";
import { StyleSheet, View, StatusBar } from "react-native";

const constants = require("../constants.json")

export default function Header(props) {
  return (
    
    <View style={[styles.container, props.style]}>
      <StatusBar 
        style="light" 
        backgroundColor="#3B4457"/>
      { props.children }
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
    backgroundColor: constants.primaryBgColor,
    width: "100%",
  }
})