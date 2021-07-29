Attribute VB_Name = "Module1"
Dim Email As String
Dim FilePath As String
    
Sub SummitEmailSend()
    'This is the sub where we will search emails from the ZGFilePath
    'Then attach the corresponding CSV in the folder.
    'We then will send the emails
    'EmailType is used to determine which of the three types of emails we need to send
    '0 = PastDuePOsUpdate
    '1 = UnconfirmedPOsUpdate
    '2 = LeadTimeUpdate
    
'    On Error GoTo ErrorHandler

    
    Dim strTextRow As String
    Dim iFileNo As Integer
    Dim iCount As Integer: iCount = 1
    Dim CSVFile As String
    Dim CSVFileCheck As String
    Dim strFileName As String
    Dim TodayDate As String
    Dim Signature As String
    Dim SigString As String
    Dim StrBody As String
    Dim StrSubject As String
    Dim signImageFolderName As String
    Dim completeFolderPath As String
    
    Dim myInspector As Outlook.Inspector
    
    TodayDate = Date
    
    LinesWritten = 0


    MsgBox "Click OK, and select a Emails file (XLSX)."
    
    FilePath = SelectFile(FilePath)
    
    'Converting the PowerBI XLSX file to TSV so the script can read and filter through it
    ConvertXlSX2TSV (FilePath)
    'MsgBox "TSV File Path: " + UpdatedFilePath
    
'    'Change only Mysig.htm to the name of your signature
'    SigString = Environ("appdata") & _
'                "\Microsoft\Signatures\Program%20Signature.htm"
'
'   ' Files folder name is always same name as html file name appended by
'    ' "_files"
'    signImageFolderName = "Program Signature_files"
'
'    completeFolderPath = Environ("appdata") & "\Microsoft\Signatures\" & signImageFolderName
'
'    If Dir(SigString) <> "" Then
'        Signature = GetBoiler(SigString)
'
'        Signature = VBA.Replace(Signature, signImageFolderName, completeFolderPath)
'    Else
'        Signature = ""
'    End If
    strFileName = FilePath

    iFileNo = FreeFile

    Open strFileName For Input As #iFileNo
    
    SigString = Environ("appdata") & "\Microsoft\Signatures\Program Signature.htm"
    
    If Dir(SigString) <> "" Then
        Signature = GetBoiler(SigString)
    Else
        Signature = ""
    End If
    Do While Not EOF(iFileNo)
        Line Input #iFileNo, strTextRow
        
        'Should be splitting lines into arrays via COMMAS
        vTextData = Split(strTextRow, Chr(9))
        
        If iCount > 0 Then
            'Takes Split Data Array and gives individual Vars the data necessary
            Email = vTextData(0)
            
            If Not Email = "" Then
                StrSubject = "Important message from The Toro Company Sourcing"
                
                Dim Emailer As Outlook.Application
                Set Emailer = New Outlook.Application
                Dim Sr As String
                Dim newmail As Outlook.MailItem
                Set newmail = Emailer.CreateItem(olMailItem)

                'Set myInspector = newmail.GetInspector
                'Application.Wait (Now + TimeValue("0:00:01"))
                'Grabbing the standard signature before it's overwritten
                newmail.To = Email & ";"
                
                'newmail.CC = "xyz@gmail.com"
                newmail.Subject = StrSubject
                newmail.HTMLBody = "Hello. <br><br>" & _
                "The Toro Company Sourcing group recently held an informational event for our supplier partners.<br><br>" & _
                "Please watch this important message from Blake Grams, VP, Global Operations, and Cabrini Brandl, Managing Director, Supply Chain.<br><br>" & _
                "This presentation also includes guest speakers, Rick Rodier, Group VP, Construction, Contractor and Residential; and Brad Hamilton, Group VP, Commercial, Intl, Ventrac & irrigation.<br><br>" & _
                "Check out this video: " & _
                "<a href=" & """" & "http://videoshare.toro.com/watch/qGYERwtC8y4XgpSFnG5At5?" & """" & ">Information Event Recording </a>" & "<br><br>" & _
                "Thank you for your continued support of The Toro Company.<br><br>" & _
                "Best Regards,<br>" & _
                "V.Nacole Schwandt<br>" & _
                "Director , Sourcing<br>" & _
                "Sent by David Hiltzman on behalf of Nacole Schwandt" & "<br>" & Signature
                
                ' "<a href= " / "http://videoshare.toro.com/watch/qGYERwtC8y4XgpSFnG5At5?""> Information Event Recording </a> " & "<br><br>"
                'newmail.Display
                newmail.Send
                LinesWritten = LinesWritten + 1
                  
            End If
        End If
        iCount = iCount + 1

    Loop
    Close #iFileNo
    Exit Sub
'ErrorHandler:
'    MsgBox "An error occurred during sending emails. Check your sent box for who got sent emails. Returning to menu."
'    Exit Sub
End Sub

Function SelectFile(ByRef FilePathCreation As String) As String
    'Resetting strFile to nothing
    On Error GoTo ErrorHandler
    strFile = ""
    Dim XL As Object
    Set XL = CreateObject("Excel.Application")
    strFile = XL.GetOpenFilename()
    SelectFile = strFile
    Exit Function
'    MsgBox strFile
ErrorHandler:
    MsgBox "An error occurred during file selection. Returning to menu."
    Exit Function
End Function

Function ConvertXlSX2TSV(sXlsFile As String)
    On Error Resume Next
    Dim oExcel          As Object
    Dim oExcelWrkBk     As Object
    Dim bExcelOpened    As Boolean    'Was Excel already open or not
    'Review 'XlFileFormat Enumeration' for more formats
    'https://docs.microsoft.com/en-us/office/vba/api/excel.xlfileformat
    Const xlTSVWindows = 20 'Windows TSV Format

 
    Set oExcel = GetObject(, "Excel.Application")    'Bind to existing instance of Excel
 
    If Err.Number <> 0 Then    'Could not get instance of Excel, so create a new one
        Err.Clear
        On Error GoTo Error_Handler
        Set oExcel = CreateObject("Excel.Application")
        bExcelOpened = False
    Else    'Excel was already running
        bExcelOpened = True
    End If
 
    On Error GoTo Error_Handler
    oExcel.ScreenUpdating = False
    oExcel.Visible = False   'Keep Excel hidden from the user
    oExcel.Application.DisplayAlerts = False
 
    Set oExcelWrkBk = oExcel.Workbooks.Open(sXlsFile)
    'Note: you may wish to change the file format constant for another type declared
    '      above based on your usage/needs in the following line.
    oExcelWrkBk.SaveAs Left(sXlsFile, InStrRev(sXlsFile, ".")) & "tsv", xlTSVWindows
    UpdatedFilePath = Left(sXlsFile, InStrRev(sXlsFile, ".")) & "tsv"
    oExcelWrkBk.Close False
 
    If bExcelOpened = False Then
        oExcel.Quit
    End If
 
Error_Handler_Exit:
    On Error Resume Next
    Set oExcelWrkBk = Nothing
    Set oExcel = Nothing
    Exit Function
 
Error_Handler:
    MsgBox "The following error has occurred." & vbCrLf & vbCrLf & _
            "Error Number: " & Err.Number & vbCrLf & _
            "Error Source: ConvertXls2CSV" & vbCrLf & _
            "Error Description: " & Err.Description, _
            vbCritical, "An Error has Occurred!"
    Resume Error_Handler_Exit
End Function

Function GetBoiler(ByVal sFile As String) As String
'Dick Kusleika
    Dim fso As Object
    Dim ts As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set ts = fso.GetFile(sFile).OpenAsTextStream(1, -2)
    GetBoiler = ts.readall
    ts.Close
End Function
