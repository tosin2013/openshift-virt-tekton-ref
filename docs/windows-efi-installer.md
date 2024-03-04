# Windows EFI Installer Pipeline

## Replace the INSERT_WINDOWS_ISO_URL with the URL of the Windows ISO file.

### Windows 11 Pipeline run 
```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: windows11-installer-run-
spec:
  params:
    - name: winImageDownloadURL
      value: INSERT_WINDOWS_ISO_URL
  pipelineRef:
    name: windows-efi-installer
  serviceAccountName: pipeline
```

### Windows 2022 Pipeline run 
```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: windows2k22-installer-run-
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

  