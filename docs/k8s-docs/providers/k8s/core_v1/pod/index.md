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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.pod" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | PodSpec is a description of a pod. |
| <CopyableCode code="status" /> | `object` | PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedPod" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind Pod |
| <CopyableCode code="listCoreV1PodForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind Pod |
| <CopyableCode code="readCoreV1NamespacedPod" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified Pod |
| <CopyableCode code="createCoreV1NamespacedPod" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a Pod |
| <CopyableCode code="deleteCoreV1CollectionNamespacedPod" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of Pod |
| <CopyableCode code="deleteCoreV1NamespacedPod" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a Pod |
| <CopyableCode code="patchCoreV1NamespacedPod" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified Pod |
| <CopyableCode code="patchCoreV1NamespacedPodEphemeralcontainers" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update ephemeralcontainers of the specified Pod |
| <CopyableCode code="patchCoreV1NamespacedPodStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update status of the specified Pod |
| <CopyableCode code="readCoreV1NamespacedPodEphemeralcontainers" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read ephemeralcontainers of the specified Pod |
| <CopyableCode code="readCoreV1NamespacedPodLog" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read log of the specified Pod |
| <CopyableCode code="readCoreV1NamespacedPodStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read status of the specified Pod |
| <CopyableCode code="replaceCoreV1NamespacedPod" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified Pod |
| <CopyableCode code="replaceCoreV1NamespacedPodEphemeralcontainers" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace ephemeralcontainers of the specified Pod |
| <CopyableCode code="replaceCoreV1NamespacedPodStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace status of the specified Pod |
| <CopyableCode code="watchCoreV1NamespacedPod" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedPodList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1PodListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
