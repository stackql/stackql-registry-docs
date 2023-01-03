---
title: persistent_volume
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes
  - k8s
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>persistent_volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.persistent_volume</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | PersistentVolumeSpec is the specification of a persistent volume. |
| `status` | `object` | PersistentVolumeStatus is the current status of a persistent volume. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1PersistentVolume` | `SELECT` |  | list or watch objects of kind PersistentVolume |
| `readCoreV1PersistentVolume` | `SELECT` | `name` | read the specified PersistentVolume |
| `createCoreV1PersistentVolume` | `INSERT` |  | create a PersistentVolume |
| `deleteCoreV1CollectionPersistentVolume` | `DELETE` |  | delete collection of PersistentVolume |
| `deleteCoreV1PersistentVolume` | `DELETE` | `name` | delete a PersistentVolume |
| `patchCoreV1PersistentVolume` | `EXEC` | `name` | partially update the specified PersistentVolume |
| `patchCoreV1PersistentVolumeStatus` | `EXEC` | `name` | partially update status of the specified PersistentVolume |
| `readCoreV1PersistentVolumeStatus` | `EXEC` | `name` | read status of the specified PersistentVolume |
| `replaceCoreV1PersistentVolume` | `EXEC` | `name` | replace the specified PersistentVolume |
| `replaceCoreV1PersistentVolumeStatus` | `EXEC` | `name` | replace status of the specified PersistentVolume |
| `watchCoreV1PersistentVolume` | `EXEC` | `name` | watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1PersistentVolumeList` | `EXEC` |  | watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead. |
