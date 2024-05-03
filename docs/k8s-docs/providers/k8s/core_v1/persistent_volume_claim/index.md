---
title: persistent_volume_claim
hide_title: false
hide_table_of_contents: false
keywords:
  - persistent_volume_claim
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
<tr><td><b>Name</b></td><td><code>persistent_volume_claim</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.persistent_volume_claim" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| <CopyableCode code="status" /> | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedPersistentVolumeClaim" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind PersistentVolumeClaim |
| <CopyableCode code="listCoreV1PersistentVolumeClaimForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind PersistentVolumeClaim |
| <CopyableCode code="readCoreV1NamespacedPersistentVolumeClaim" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified PersistentVolumeClaim |
| <CopyableCode code="createCoreV1NamespacedPersistentVolumeClaim" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a PersistentVolumeClaim |
| <CopyableCode code="deleteCoreV1CollectionNamespacedPersistentVolumeClaim" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of PersistentVolumeClaim |
| <CopyableCode code="deleteCoreV1NamespacedPersistentVolumeClaim" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a PersistentVolumeClaim |
| <CopyableCode code="patchCoreV1NamespacedPersistentVolumeClaim" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified PersistentVolumeClaim |
| <CopyableCode code="patchCoreV1NamespacedPersistentVolumeClaimStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update status of the specified PersistentVolumeClaim |
| <CopyableCode code="readCoreV1NamespacedPersistentVolumeClaimStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read status of the specified PersistentVolumeClaim |
| <CopyableCode code="replaceCoreV1NamespacedPersistentVolumeClaim" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified PersistentVolumeClaim |
| <CopyableCode code="replaceCoreV1NamespacedPersistentVolumeClaimStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace status of the specified PersistentVolumeClaim |
| <CopyableCode code="watchCoreV1NamespacedPersistentVolumeClaim" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedPersistentVolumeClaimList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1PersistentVolumeClaimListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. |
