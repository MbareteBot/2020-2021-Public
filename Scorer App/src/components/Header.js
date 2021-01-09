import React from "react";
import { StyleSheet, View, StatusBar } from "react-native";
import CText from "./CustomText"

const constants = require("../constants.json")

export default function Header(props) {
  return (
    <View style={styles.container}>
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