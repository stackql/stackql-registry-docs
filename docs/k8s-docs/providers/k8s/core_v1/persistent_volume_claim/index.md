---
title: persistent_volume_claim
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
<tr><td><b>Name</b></td><td><code>persistent_volume_claim</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.persistent_volume_claim</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| `status` | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedPersistentVolumeClaim` | `SELECT` | `namespace` | list or watch objects of kind PersistentVolumeClaim |
| `listCoreV1PersistentVolumeClaimForAllNamespaces` | `SELECT` |  | list or watch objects of kind PersistentVolumeClaim |
| `readCoreV1NamespacedPersistentVolumeClaim` | `SELECT` | `name, namespace` | read the specified PersistentVolumeClaim |
| `createCoreV1NamespacedPersistentVolumeClaim` | `INSERT` | `namespace` | create a PersistentVolumeClaim |
| `deleteCoreV1CollectionNamespacedPersistentVolumeClaim` | `DELETE` | `namespace` | delete collection of PersistentVolumeClaim |
| `deleteCoreV1NamespacedPersistentVolumeClaim` | `DELETE` | `name, namespace` | delete a PersistentVolumeClaim |
| `patchCoreV1NamespacedPersistentVolumeClaim` | `EXEC` | `name, namespace` | partially update the specified PersistentVolumeClaim |
| `patchCoreV1NamespacedPersistentVolumeClaimStatus` | `EXEC` | `name, namespace` | partially update status of the specified PersistentVolumeClaim |
| `readCoreV1NamespacedPersistentVolumeClaimStatus` | `EXEC` | `name, namespace` | read status of the specified PersistentVolumeClaim |
| `replaceCoreV1NamespacedPersistentVolumeClaim` | `EXEC` | `name, namespace` | replace the specified PersistentVolumeClaim |
| `replaceCoreV1NamespacedPersistentVolumeClaimStatus` | `EXEC` | `name, namespace` | replace status of the specified PersistentVolumeClaim |
| `watchCoreV1NamespacedPersistentVolumeClaim` | `EXEC` | `name, namespace` | watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedPersistentVolumeClaimList` | `EXEC` | `namespace` | watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1PersistentVolumeClaimListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. |
