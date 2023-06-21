import QtQuick 2.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import MuseScore 3.0

import FileIO 3.0

MuseScore {
      menuPath: "Plugins.harmonies_analysis"
      description: "Description goes here"
      version: "1.0"
      pluginType: "dock";
      dockArea: "left";
      implicitHeight: 160;
      implicitWidth: 240;
      
      QProcess {
            id: proc
      }
      FileDialog {
            id: fileDialog
            title: "Please choose a file"
            folder: shortcuts.home
            nameFilters: ["XML (*.mxl *.xml)", "All files (*)"]
            onAccepted: {
                  var path = fileDialog.fileUrl
                  console.log("You chose: " + path)
            }
            onRejected: {
                  console.log("Canceled")
            }
      }           
    

      property int margin: 10
      property var range_mode : false
      property var the_note : null
      property var stop_recurse : false;
      property var nnflag : "not-note"
      property var display_up : false

      width:  240
      height: 160
      
      
      
      Rectangle {
            id: wrapperPanel
            color: "white"
            Text {
                  id: title
                  text: "Harmonies_analysis"
                  font.family: "Helvetica"
                  font.pointSize: 20
                  color: "white"
                  anchors.top: wrapperPanel.top
                  anchors.topMargin: 30
                  anchors.left: wrapperPanel.left
                  anchors.leftMargin: 20
                  font.underline: true
             }
       }
       
       Text{
            id: warning
            text : "Please select the frequence"
            color: "white"
            anchors.top: wrapperPanel.top
            anchors.topMargin: 270
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 20
            visible : false
      }
       
       Text{
            id: information
            text: "Save your score in XML format \n   to start the analysis using \n           the button below "
            color: "white"
            anchors.top: wrapperPanel.top
            anchors.topMargin: 70
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 20
      }
            
        Rectangle {
            id:button
            anchors.top: wrapperPanel.top
            anchors.topMargin: 140
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 30
            color: "blue"
            width: 150; height: 75
 
            Text{
                  id: buttonLabel
                  font.pointSize: 20
                  color : "white"
                  anchors.centerIn: parent
                  text: "Chose score"
            }
            MouseArea{
                   id: buttonMouseArea
 
                  anchors.fill: parent //anchor all sides of the mouse area to the rectangle's anchors
                  //onClicked handles valid mouse button clicks
                  
                  onClicked: {
                        fileDialog.open()
                        select.visible= true
                        button2.visible = true
                        button.visible = false
                        console.log(buttonLabel.text + " clicked" )
                        try {
                              var out=proc.readAllStandardOutput()
                              console.log("-- Command output: "+out)
                              if (val) {
                                    console.log('terminated correctly.')
                              } else {
                                    console.log('failure')
                              }
                        } catch (err) {
                              console.log("--" + err.message);
                        }
                  }
            }
      }
      Rectangle {
            id:button2
            anchors.top: wrapperPanel.top
            anchors.topMargin: 180
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 30
            color: "blue"
            visible: false
            width: 150; height: 75
 
            Text{
                  id: buttonLabel2
                  font.pointSize: 20
                  color : "white"
                  anchors.centerIn: parent
                  text: "Start analysis"
            }
            MouseArea{
                   id: buttonMouseArea2
 
                  anchors.fill: parent //anchor all sides of the mouse area to the rectangle's anchors
                  //onClicked handles valid mouse button clicks
                  
                  onClicked: {
                        if (select.currentText == "Select freq"){
                              warning.visible = true
                        }else{
                              warning.visible = false
                              var docu_path = fileDialog.fileUrl;
                              console.log(docu_path)
                              var freq = select.currentText
                              var ind = select.currentIndex
                              var doulbe_freq = [0, 2, 4, 6, 8];
                              console.log(doulbe_freq[0])
                              //var d = '/bin/sh -c "~/Documents/MuseScore3/Plugins/lancerpy.sh %1 %2 %3"';
                              //var d = '/bin/sh -c "~/Documents/MuseScore3/Plugins/firstscript.sh %1 %2 %3"';
                        
                        
                              //proc.start(d.arg(docu_path).arg(freq).arg(doulbe_freq[ind]))
                              var e = '/bin/sh -c "~/Documents/MuseScore3/Plugins/analyse.sh %1 %2 %3"';
                              proc.start(e.arg(docu_path).arg(freq).arg(doulbe_freq[ind]))
                              var val=proc.waitForFinished(5000)
                              button3.visible = true
                              console.log(buttonLabel.text + " clicked" )
                              try {
                                    var out=proc.readAllStandardOutput()
                                    console.log("-- Command output: "+out)
                                    if (val) {
                                          console.log('terminated correctly.')
                                    } else {
                                          console.log('failure')
                                    }
                              } catch (err) {
                                    console.log("--" + err.message);
                              }
                        }
                  }
            }
      }
       Rectangle {
            id:button3
            anchors.top: wrapperPanel.top
            anchors.topMargin: 270
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 30
            color: "gray"
            visible: false
            width: 150; height: 50
 
            Text{
                  id: buttonLabel3
                  font.pointSize: 20
                  color : "white"
                  anchors.centerIn: parent
                  text: "New analysis"
            }
            MouseArea{
                   id: buttonMouseArea3
                   anchors.fill: parent
                   
                   onClicked: {
                        button.visible = true
                        button2.visible = false
                        select.visible = false
                        button3.visible = false
                  }
            }
     }
     ComboBox {
            id : select
            anchors.top: wrapperPanel.top
            anchors.topMargin: 140
            anchors.left: wrapperPanel.left
            anchors.leftMargin: 45
            model: ["Select freq","croche","noire","noire_pointe","blanche"]
            visible: false
      }
}

