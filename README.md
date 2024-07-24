# Openshift Virtualization Tekton Reference Demo

The `Openshift Virtualization Tekton Reference Demo` repository is a collection of resources and configurations designed to manage OpenShift 4 instances using Tekton, a powerful Kubernetes-native CI/CD framework. This repository serves as a reference for applying Kubernetes configurations to OpenShift clusters, leveraging Tekton's custom resource definitions (CRDs) to create portable and efficient CI/CD pipelines.

## Main Purpose

![20240303212440](https://i.imgur.com/0hEl4Gs.png)

The primary goal of this repository is to provide a structured and standardized way to manage virtual machines and their lifecycles within OpenShift environments using Tekton pipelines. It includes examples and templates that can be used to create, manage, and manipulate virtual machines (VMs), persistent volume claims (PVCs), and data volumes, as well as to run commands within VMs and handle disk images with libguestfs tools.

![20240303212551](https://i.imgur.com/2G6uswF.png)

## Features

- **Tekton Task and Pipeline Definitions**: Utilizes Tekton's CRDs such as `Task`, `Pipeline`, and `ClusterTask` to define the steps required for managing OpenShift virtualization workloads.
- **Integration with OpenShift Virtualization**: Provides examples that integrate with OpenShift Virtualization, allowing for the deployment and management of VMs using the `oc` CLI.
- **Reusable Tasks**: Leverages reusable tasks from the Tekton catalog, enabling the creation of generic pipelines that can be adapted across different environments and stages of the application lifecycle.

## Getting Started

To use the resources in this repository, you should have:

- An OpenShift Container Platform cluster with `cluster-admin` permissions.
- The OpenShift CLI (`oc`) installed.
- OpenShift Pipelines installed on your cluster.
- ArgoCD installed on your cluster.

Follow the instructions within the repository to apply the provided Kubernetes configurations to your OpenShift clusters using the `oc apply -k` command with URLs pointing to specific overlays.

### Documentation contains the Examples:
* [Documentation](docs/README.md)

**OpenShift 4.15 Workshop instance**
```
oc apply -k https://github.com/tosin2013/openshift-virt-tekton-ref/clusters/overlays/4.15-workshop
```

**OpenShift 4.16 Workshop instance**
```
oc apply -k https://github.com/tosin2013/openshift-virt-tekton-ref/clusters/overlays/4.16-workshop
```

**Deploying to multiple clusters**  
*Example cluster1*
```
oc apply -k https://github.com/tosin2013/openshift-virt-tekton-ref/clusters/overlays/cluster1
```
*Example cluster 2*
```
oc apply -k https://github.com/tosin2013/openshift-virt-tekton-ref/clusters/overlays/cluster2
```

![20240303212700](https://i.imgur.com/mLZjbOy.png)

## Links 
* https://github.com/kubevirt/kubevirt-tekton-tasks
* https://www.redhat.com/en/blog/building-vm-images-using-tekton-and-secrets


## To allow for rhel virtual machines to be created and registered with the Red Hat Subscription Manager:
`Settings->Guest management->Automatic subscription of new RHEL VirtualMachines`
![20240723185006](https://i.imgur.com/zKmhvmG.png)
## Contributing

Contributions to the `Openshift Virtualization Tekton Reference Demo` repository are welcome. Whether it's submitting an issue, a pull request, or suggesting new features, your input is valuable in making this resource more useful for everyone managing OpenShift virtualization with Tekton.

