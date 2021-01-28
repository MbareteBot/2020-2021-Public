import React from "react";
import { StyleSheet, Text } from "react-native";

export default function CText(props) {
  return (
    <Text style={[styles.text, props.style]}>{props.children}</Text>
  )
}

const styles = StyleSheet.create({
  text: {
    color: "#fff",
  }
})