import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import 'react-native-gesture-handler';
import Scorer from "./screens/Scorer";
import Timer from "./screens/Timer";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
          screenOptions={{ headerShown: false }}>
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