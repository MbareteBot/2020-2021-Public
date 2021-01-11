import React, { useState } from "react";
import { StyleSheet, View, Text, TouchableOpacity } from "react-native";
import Icon from "react-native-vector-icons/Ionicons"
import CText from "./CustomText";

const constants = require("../constants.json")

export default function NavBar(props) {
  /*
    args: [[icons(name)], [iconPage], [activeIcon]] 
  */
  const [color, setColor] = useState(constants.primaryColor)
  return (
      <View style={styles.container}>
      { props.icons ? (
        <View style={styles.iconContainer}>
        {
          props.icons[0].map((iconName, index) => {
            if (index == props.active[0]) {
              return <Icon 
                        key={index} 
                        name={iconName} 
                        size={30} 
                        color={props.active[1]} 
                        style={{borderBottomWidth: 3, 
                          borderBottomColor: props.active[1], 
                          paddingHorizontal: 3}} />    
            }
            return <Icon 
                      key={index} 
                      name={iconName} 
                      size={30} 
                      color={color} 
                      onPress={() => props.pageNavigationHandler(props.icons[1][index])}/>      
        
          })
        }
        </View>    
        ) : null }

        { props.title ? (
          <View style={styles.titleContainer}>
            {
              props.title[0].map((title, index) => {
                if (index == props.active[0]) {
                  return <TouchableOpacity key={index} >
                          <CText 
                            style={[{color: props.active[1]}, styles.title]}>{title}</CText>
                          </TouchableOpacity>
                }
                return <TouchableOpacity 
                        key={index}
                        onPress={() => props.pageNavigationHandler(props.title[1][index])}>
                        <CText 
                          style={styles.title}>{title}</CText>
                        </TouchableOpacity>
              })
            }
          </View>
        ) : null }
    </View>
  )
} 

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    backgroundColor: constants.primaryBgColor,
    width: "100%",
  },
  iconContainer: {
    flexDirection: "row",
    width: "100%",
    justifyContent: "space-around",
    paddingVertical: 10
  },
  titleContainer: {
    paddingVertical: 15,
    flexDirection: "row",
    justifyContent: "space-around",
    width: "100%",
  },
  title: {
    fontSize: 23
  }
})