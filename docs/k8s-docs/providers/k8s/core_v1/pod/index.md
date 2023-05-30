---
title: pod
hide_title: false
hide_table_of_contents: false
keywords:
  - pod
  - core_v1
  - k8s    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: /img/providers/k8s/stackql-k8s-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.pod</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | PodSpec is a description of a pod. |
| `status` | `object` | PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedPod` | `SELECT` | `namespace, cluster_addr, protocol` | list or watch objects of kind Pod |
| `listCoreV1PodForAllNamespaces` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind Pod |
| `readCoreV1NamespacedPod` | `SELECT` | `name, namespace, cluster_addr, protocol` | read the specified Pod |
| `createCoreV1NamespacedPod` | `INSERT` | `namespace, cluster_addr, protocol` | create a Pod |
| `deleteCoreV1CollectionNamespacedPod` | `DELETE` | `namespace, cluster_addr, protocol` | delete collection of Pod |
| `deleteCoreV1NamespacedPod` | `DELETE` | `name, namespace, cluster_addr, protocol` | delete a Pod |
| `patchCoreV1NamespacedPod` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update the specified Pod |
| `patchCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update ephemeralcontainers of the specified Pod |
| `patchCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update status of the specified Pod |
| `readCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace, cluster_addr, protocol` | read ephemeralcontainers of the specified Pod |
| `readCoreV1NamespacedPodLog` | `EXEC` | `name, namespace, cluster_addr, protocol` | read log of the specified Pod |
| `readCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | read status of the specified Pod |
| `replaceCoreV1NamespacedPod` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace the specified Pod |
| `replaceCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace ephemeralcontainers of the specified Pod |
| `replaceCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace status of the specified Pod |
| `watchCoreV1NamespacedPod` | `EXEC` | `name, namespace, cluster_addr, protocol` | watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedPodList` | `EXEC` | `namespace, cluster_addr, protocol` | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1PodListForAllNamespaces` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
