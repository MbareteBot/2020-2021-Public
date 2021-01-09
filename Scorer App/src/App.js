import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import 'react-native-gesture-handler';
import Scorer from "./screens/Scorer";
import Timer from "./screens/Timer";

const constants = require("./constants.json")
const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator           
        screenOptions={{
          headerStyle: {
            backgroundColor: constants.primaryBgColor,
          },
          headerTitleStyle: { 
            alignSelf: 'center',
            fontSize: 20,
          },
          headerTintColor: constants.primaryColor,
          headerLeft: ""
        }} >
        <Stack.Screen
          name="Scorer"
          component={Scorer} />
        <Stack.Screen 
          name="Timer" 
          component={Timer} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}