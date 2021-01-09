import React, { useState } from "react";
import { StyleSheet, View, Text, Button, TouchableOpacity } from "react-native";
import { TouchableHighlight } from "react-native-gesture-handler";
import Icon from "react-native-vector-icons/Ionicons"

const constants = require("../constants.json")

export default function NavBar(props) {
  /*
    args: [[icons(name)], [iconPage], [activeIcon]] 
  */
  const [color, setColor] = useState(constants.primaryColor)
  return (
    <View style={styles.container}>
      { props.icons[0].map((iconName, index) => {
        if (index == props.active[0]) {
          return <Icon key={index} name={iconName} size={30} color={props.active[1]} style={{borderBottomWidth: 3, borderBottomColor: props.active[1], paddingHorizontal: 3}} onPress={() => {}}/>
        }
        return <Icon key={index} name={iconName} size={30} color={color} onPress={() => props.pageNavigationHandler(props.icons[1][index])}/>
                
      })}
    </View>
  )
} 

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "space-around",
    paddingVertical: 10,
    backgroundColor: constants.primaryBgColor,
    width: "100%",
  }
})