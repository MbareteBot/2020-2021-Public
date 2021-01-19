import React, { useState } from "react";
import { StyleSheet, TouchableOpacity, View, ActivityIndicator } from "react-native";
import WebView from "react-native-webview";
import CText from "../components/CustomText";
import Header from "../components/Header";
import NavBar from "../components/NavBar";
import Icon from "react-native-vector-icons/Ionicons";

const CONSTANTS = require("../constants.json");

const ActivityIndicatorElement = () => {
  return (
    <ActivityIndicator
      color="#009688"
      size="large"
      style={styles.activityIndicatorStyle} />
  );
};

export default function Docs({ navigation, route }) {

  const CONTENT = route.params.LABELS.documentation;
  const [viewLink, setViewLink] = useState("");
  const handleLink = (link) => {
    setViewLink(link);
  }
  const goBack = () => {
    setViewLink("");
  }
  const docLinks = {
    modelOverview: {
      name: CONTENT.modelOverview.name,
      icon: "eye",
      link: CONTENT.modelOverview.link
    },
    robotGameRulebook: {
      name: CONTENT.robotGameRulebook.name,
      icon: "eye",
      link: CONTENT.robotGameRulebook.link
    },
    rubrics: {
      name: CONTENT.rubrics.name,
      icon: "eye",
      link: CONTENT.rubrics.link
    },
    robotGameScoresheet: {
      name: CONTENT.robotGameScoresheet.name,
      icon: "eye",
      link: CONTENT.robotGameScoresheet.link
    },
    awards: {
      name: CONTENT.awards.name,
      icon: "eye",
      link: CONTENT.awards.link
    },
    judgingSessionForTeams: {
      name: CONTENT.judgingSessionForTeams.name,
      icon: "eye",
      link: CONTENT.judgingSessionForTeams.link
    },
    updates: {
      name: CONTENT.updates.name,
      icon: "eye",
      link: CONTENT.updates.link
    }
  }
  const docLinksNames = ["modelOverview", "robotGameRulebook", "rubrics", "robotGameScoresheet", "awards", "judgingSessionForTeams", "updates"]
  return (
    <View style={ styles.container }>
      <Header style={{ backgroundColor: "#fff", flexDirection: "row" }}>
        <View style={{ position: "absolute", left: 20 }}>
          <Icon name="arrow-back" size={30} color={CONSTANTS.secondaryColor} onPress={goBack} />
        </View>
        <CText style={{ fontSize: 23, color: CONSTANTS.secondaryColor }}>{ CONTENT.title }</CText>
      </Header>
      <View style={{flex: 1}}>
      { viewLink ? (
          <WebView 
            style={styles.onlineDoc} 
            scalesPageToFit={false}
            containerStyle={{ position: "absolute", top: 0, width: "100%", height: "100%", zIndex: 1 }}
            renderLoading={ActivityIndicatorElement}
            source={{ uri: `http://docs.google.com/gview?embedded=true&url=${viewLink}` }} />
        ): null}
      <View style={ styles.docsContainer }>
        {
          docLinksNames.map(name => (
            <TouchableOpacity style={ styles.docContainer } onPress={() => handleLink(docLinks[name].link)}>
              <Icon name={docLinks[name].icon} size={30} color={"white"} />
              <CText style={styles.docLink}>{docLinks[name].name}</CText>
          </TouchableOpacity> 
          ))
        }

      </View>
      </View>
      <NavBar 
          icons={[["md-calculator-outline", "stopwatch-outline", "book-outline"],
                  ["Scorer", "Timer", "Docs"]]}
          active={[2, CONSTANTS.darkYellow]}
          pageNavigationHandler={ navigation.navigate }
          contentLabels={route.params.LABELS} />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: CONSTANTS.primaryBgColor,
  },
  docContainer: {
    padding: 20,
    backgroundColor: CONSTANTS.secondaryColor,
    borderBottomLeftRadius: 10,
    borderBottomColor: "white",
    borderBottomWidth: 1,
    flexDirection: "row",
    alignItems: "center",
  },
  docLink: {
    marginLeft: 10
  },  
  activityIndicatorStyle: {
    flex: 1,
    position: 'absolute',
    marginLeft: 'auto',
    marginRight: 'auto',
    marginTop: 'auto',
    marginBottom: 'auto',
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    justifyContent: 'center',
  },
})