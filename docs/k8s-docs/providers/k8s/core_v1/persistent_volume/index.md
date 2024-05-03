---
title: persistent_volume
hide_title: false
hide_table_of_contents: false
keywords:
  - persistent_volume
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
<tr><td><b>Name</b></td><td><code>persistent_volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.persistent_volume" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | PersistentVolumeSpec is the specification of a persistent volume. |
| <CopyableCode code="status" /> | `object` | PersistentVolumeStatus is the current status of a persistent volume. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1PersistentVolume" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind PersistentVolume |
| <CopyableCode code="readCoreV1PersistentVolume" /> | `SELECT` | <CopyableCode code="name, cluster_addr, protocol" /> | read the specified PersistentVolume |
| <CopyableCode code="createCoreV1PersistentVolume" /> | `INSERT` | <CopyableCode code="cluster_addr, protocol" /> | create a PersistentVolume |
| <CopyableCode code="deleteCoreV1CollectionPersistentVolume" /> | `DELETE` | <CopyableCode code="cluster_addr, protocol" /> | delete collection of PersistentVolume |
| <CopyableCode code="deleteCoreV1PersistentVolume" /> | `DELETE` | <CopyableCode code="name, cluster_addr, protocol" /> | delete a PersistentVolume |
| <CopyableCode code="patchCoreV1PersistentVolume" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | partially update the specified PersistentVolume |
| <CopyableCode code="patchCoreV1PersistentVolumeStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | partially update status of the specified PersistentVolume |
| <CopyableCode code="readCoreV1PersistentVolumeStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | read status of the specified PersistentVolume |
| <CopyableCode code="replaceCoreV1PersistentVolume" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace the specified PersistentVolume |
| <CopyableCode code="replaceCoreV1PersistentVolumeStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace status of the specified PersistentVolume |
| <CopyableCode code="watchCoreV1PersistentVolume" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1PersistentVolumeList" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead. |
