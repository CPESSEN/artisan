import prettytable
import re
try:
  from PyQt5.QtWidgets import QApplication
except Exception:
  from PyQt6.QtWidgets import QApplication

def content():
    strlist = []
    helpstr = ''  #@UnusedVariable
    newline = '\n'  #@UnusedVariable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append("<b>")
    strlist.append(QApplication.translate('HelpDlg','EVENT ANNOTATIONS',None))
    strlist.append("</b>")
    tbl_Annotations = prettytable.PrettyTable()
    tbl_Annotations.field_names = [QApplication.translate('HelpDlg','Prefix Field',None),QApplication.translate('HelpDlg','Source',None),QApplication.translate('HelpDlg','Example',None)]
    tbl_Annotations.add_row(['~E',QApplication.translate('HelpDlg','The value of Event',None),60])
    tbl_Annotations.add_row(['~Y1',QApplication.translate('HelpDlg','ET value',None),420])
    tbl_Annotations.add_row(['~Y2',QApplication.translate('HelpDlg','BT value',None),372])
    tbl_Annotations.add_row(['~descr',QApplication.translate('HelpDlg','The Description field of the Event',None),'Gas 10'])
    tbl_Annotations.add_row(['~type',QApplication.translate('HelpDlg','The Type field of the Event',None),'Power'])
    tbl_Annotations.add_row(['~sldrunit',QApplication.translate('HelpDlg','The value of the Slider Unit for this Event',None),'kPa'])
    tbl_Annotations.add_row(['~dCHARGE',QApplication.translate('HelpDlg','Number of seconds since CHARGE',None),522])
    tbl_Annotations.add_row(['~dFCs',QApplication.translate('HelpDlg','Number of seconds after FCs \nBest used inside double quotes (see notes below) \nDisplays &#39;*&#39; prior to FCs',None),47])
    tbl_Annotations.add_row(['~preFCs',QApplication.translate('HelpDlg','Number of seconds before FCs \nBest used inside single quotes or back ticks (see notes below) \nDisplays &#39;*&#39; after FCs',None),50])
    tbl_Annotations.add_row(['~DTR',QApplication.translate('HelpDlg','Development time ratio. Note: DTR=0 before FCs \n100*(t{Event}-t{FCs})/(t{FCs}-t{CHARGE})',None),12])
    tbl_Annotations.add_row(['~deg',QApplication.translate('HelpDlg','The degree symbol',None),'\u00b0'])
    tbl_Annotations.add_row(['~mode',QApplication.translate('HelpDlg','Temperature mode (&#39;C&#39; or &#39;F&#39;)',None),'F'])
    tbl_Annotations.add_row(['~degmode',QApplication.translate('HelpDlg','Degree symbol with Temperature mode',None),'\u00b0C'])
    tbl_Annotations.add_row(['~R1',QApplication.translate('HelpDlg','ET RoR value\nDisplays &#39;--&#39; when the RoR value is not available.',None),9.9])
    tbl_Annotations.add_row(['~R2',QApplication.translate('HelpDlg','BT RoR value\nShows &#39;--&#39; when the RoR value Is not available.',None),18.2])
    tbl_Annotations.add_row(['~degmin',QApplication.translate('HelpDlg','RoR units\nShorthand for &#39;~deg~mode/min&#39;',None),'\u00b0C/min'])
    tbl_Annotations.add_row(['~R1degmin',QApplication.translate('HelpDlg','ET RoR with units\nField is hidden when the RoR value is not available.',None),'9.9\u00b0C/min'])
    tbl_Annotations.add_row(['~R2degmin',QApplication.translate('HelpDlg','BT RoR with units\nField is hidden when the RoR value is not available.',None),'18.2\u00b0C/min'])
    tbl_Annotations.add_row(['~quot',QApplication.translate('HelpDlg','Quote symbol',None),'"'])
    tbl_Annotations.add_row(['~squot',QApplication.translate('HelpDlg','Single quote symbol',None),'&#39;'])
    strlist.append(tbl_Annotations.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','EXAMPLES',None))
    strlist.append("</b>")
    tbl_Examplestop = prettytable.PrettyTable()
    tbl_Examplestop.header = False
    tbl_Examplestop.add_row([QApplication.translate('HelpDlg','Assumptions:  The event value is 50.  In the case of Gas the value 50 corresponds to either 5.0kPh or 50%.  \nFor a sensory milestone (see notes above) the value 50 corresponds to the "Hay" aroma. ',None)])
    strlist.append(tbl_Examplestop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Examples = prettytable.PrettyTable()
    tbl_Examples.field_names = [QApplication.translate('HelpDlg','Annotation Field',None),QApplication.translate('HelpDlg','Displays',None)]
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E @~Y2~degmode',None),QApplication.translate('HelpDlg','Gas 50 @340\u00b0F',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E% @~Y2~mode',None),QApplication.translate('HelpDlg','Gas 50% @340F',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E/10kPh @~Y2~mode',None),QApplication.translate('HelpDlg','Gas 5.0kPh @340F',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E/10kPh @~Y2~mode and ~R2~degmin',None),QApplication.translate('HelpDlg','Gas 5.0kPh @340F and 32.8\u00b0F/min',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E% &#39;@~Y2 ~degmode&#39;"@~DTR% DTR"',None),QApplication.translate('HelpDlg','Before FCs:\nGas 50% @340 \u00b0F\n\nAfter FCs:\nGas 50% @12% DTR',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','Gas ~E% &#39;@~Y2 ~degmode`, ~preFCs sec before FCs`&#39;"@~DTR% DTR"',None),QApplication.translate('HelpDlg','More than 90 seconds before FCs:\nGas 50% @340 \u00b0F\n\nLess than 90 seconds before FCs:\nGas 50% @340 \u00b0F, 50 sec before FCs \n\nAfter FCs:\nGas 50% @12% DTR',None)])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','{20Fresh Cut Grass|50Hay|80Baking Bread|100A Point} @~Y2~degmode',None),QApplication.translate('HelpDlg','Hay @340 \u00b0F',None)])
    strlist.append(tbl_Examples.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','NOTES:',None))
    strlist.append("</b>")
    tbl_Notes = prettytable.PrettyTable()
    tbl_Notes.field_names = ['&#160;']
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Event annotations apply only for &#39;Step&#39; and &#39;Step+&#39; Events settings',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Anything between double quotes " will show only after FCs. Example: "~E1 @~DTR%"',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Anything between single quotes &#39; will show only before FCs. Example: &#39;~E1 @~degmode&#39;',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Anything between back ticks ` will show only within 90 seconds before FCs. Example: `~E1 `FCs~dFCs sec`',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','When combining back ticks with single or double quotes the back ticks should be inside the quotes.',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Background event annotations can be seen during a roast when &#39;Annotations&#39; is checked in the Profile Background window.',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Simple scaling of the event value is possible. Use a single math operator (&#39;*&#39;, &#39;/&#39;, &#39;+&#39; or &#39;-&#39;) immediately following the field name "E". For example: \n&#39;~E/10&#39; will divide the E value by 10. \n&#39;~E+5&#39; adds 5 to the the value of E.',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','Another style of annotations allows to replace an event&#39;s numeric value with a text string, known as a nominal value. One example where this can be useful is when an event is used to record sensory milestones. The value 20 might be used for &#39;Fresh Cut Grass&#39; aroma, 50 for &#39;Hay&#39;, 80 for &#39;Baking Bread&#39;, and 100 to represent the &#39;A Point&#39;.  \n\nThis form of annotation must be enclosed in curly brackets &#39;{}&#39;. Entries are numeric values immediately followed by their nominal representation text.  Entries are separated by the vertical bar &#39;|&#39;. The following Annotation string implements this example.   \n{~E|20Fresh Cut Grass|50Hay|80Baking Bread|100A Point} \n\nNote that if the event value  does not match any value in the Annotation definition a blank string will be returned.  In the example above an event value of 30 will return a blank string.  The easiest way to ensure these values match is to use Custom Buttons to for the Event.',None)])
    tbl_Notes.add_row([QApplication.translate('HelpDlg','When annotations overlap to the point they can not be read, try reducing the value of the &#39;Allowed Annotation Overlap&#39; found on the Annotations configuration page.  The default value for this setting is 100%.',None)])
    strlist.append(tbl_Notes.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("</body>")
    helpstr = "".join(strlist)
    helpstr = re.sub(r"&amp;", r"&",helpstr)
    return helpstr