# Windows EFI Installer Pipeline
[Windows EFI Installer Pipeline](components/kubevirt-pipelines/overlays/windows-efi-installer/overlays/windows-efi-installer/README.md)

## Replace the INSERT_WINDOWS_ISO_URL with the URL of the Windows ISO file.

### Windows 11 Pipeline run 
* https://www.microsoft.com/en-us/software-download/windows11

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: windows11-installer-run-
  namespace: windows-efi-installer
spec:
  params:
    - name: winImageDownloadURL
      value: INSERT_WINDOWS_ISO_URL
  pipelineRef:
    name: windows-efi-installer
  serviceAccountName: pipeline
```

### Windows 2022 Pipeline run 
* https://www.microsoft.com/en-us/evalcenter/download-windows-server-2022
```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: windows2k22-installer-run-
  namespace: windows-efi-installer
spec:
  params:
    - name: winImageDownloadURL
      value: INSERT_WINDOWS_ISO_URL
    - name: preferenceName
      value: "windows.2k22"
    - name: autounattendConfigMapName
      value: windows2k22-autounattend
    - name: baseDvName
      value: win2k22
    - name: isoDVName
      value: win2k22
  pipelineRef:
    name: windows-efi-installer
  timeout: 1h0m0s
  serviceAccountName: pipeline      
  ```
![20240304155512](https://i.imgur.com/VQIUJEb.png)

Validate that the pipeline has started to run. 
![20240304155825](https://i.imgur.com/brxYz8K.png)
Validate that the Windows 11 or 2022 installation is successful by navigating to the virtual machine console.
![20240304160156](https://i.imgur.com/OK1NjHb.png)

![20240304160803](https://i.imgur.com/zhCeGkI.png)]
