# Ollama Langchain

This is an example of running the ollama-langchain pipeline. 

![20240304132211](https://i.imgur.com/NIf1jkW.png)

The PipelineRun named "ollama-langchain-btpsj3" and is part of the "ollama-langchain" project (or namespace). The goal, as mentioned, is to run "Ollama Langchain" on OpenShift in a virtual machine (VM).

![20240304123944](https://i.imgur.com/5y4plVG.png)

The pipelien successfully completed. The VM was created and the ollama server  was deployed in the VM.
![20240304125246](https://i.imgur.com/IFtK9id.png)

Load the mistral model once you login to the VM using 
```bash
cd ollama-langchain
./start_ollama.sh mistral
```

![20240304125343](https://i.imgur.com/4ugf5bk.png)

Start the streamlit app using 
```bash 
# /bye to exit the mistral model 
# streamlit run app.py
```

![20240304125902](https://i.imgur.com/N5xb4L2.png)

Navigate to the OpenShift Route to access your Ollama Langchain application.
![20240304131017](https://i.imgur.com/VwqdzwD.png)
![20240304130006](https://i.imgur.com/JkOVFbn.png)