# OpenShift Virtualization Application Examples

## Microshift Instance
The `microshift-instance` playbook is designed to set up Microshift 4.15. It is currently a work in progress (WIP) and under active development. We welcome contributions to help bring this project to completion. For more details, see [microshift-instance.md](microshift-instance.md).

## Ollama Langchain
Ollama Langchain is an innovative chatbot that leverages Langchain for natural language processing and response generation. Our playbook facilitates the deployment of Ollama Langchain on OpenShift within a virtual machine (VM) environment. Explore the setup guide at [ollama-langchain.md](ollama-langchain.md).

## Windows BIOS Installer
 Windows BIOS Installer installs and syspreps a machine using Windows 10 or 2019 iso's downloaded feom microsft.com. [windows-bios-installer.md](windows-bios-installer.md).

## Windows EFI Installer
We are also working on documentation for the Windows EFI Installer. More information will be available soon at [windows-efi-installer.md](windows-efi-installer.md).

## Contributing to the Repository
We encourage contributions to this repository! If you're interested in contributing, please feel free to submit a pull request or raise an issue. To add a new pipeline, place it in the `components/kubevirt-pipelines` directory and create a corresponding overlay in the `overlays` directory. Then, update the `README.md` file in the root of the repository with a link to the new pipeline. If you would like to contriube to documentation, please add it to the `docs` directory. Your contributions are greatly appreciated and help enhance the OpenShift virtualization experience for everyone.

