# Windows BIOS Installer Pipeline 

This is an example of running the windows10-installer pipeline. 


![20240304150512](https://i.imgur.com/qLnwSRW.png)

 The example  pipeline `windows10-installer` in the   "Windows BIOS Installer" project automates the installation of a Windows operating system on a virtual machine (VM) using a BIOS firmware interface.


## Create the pipelineRun
**Replace the INSERT_WINDOWS_ISO_URL with the URL of the Windows ISO file.**
* https://www.microsoft.com/en-us/software-download/windows10ISO
* https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019 
  
```
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: windows10-installer-run-
  namespace: windows-bios-installer
spec:
  params:
  - name: winImageDownloadURL
    value: INSERT_WINDOWS_ISO_URL
  pipelineRef:
    name: windows-bios-installer
  serviceAccountName: pipeline
status: {}
```


![20240304141725](https://i.imgur.com/Mdfnoo8.png)

Nativgate to the virtula machine console to see the installation process.
![20240304142043](https://i.imgur.com/tNHnlQH.png)

