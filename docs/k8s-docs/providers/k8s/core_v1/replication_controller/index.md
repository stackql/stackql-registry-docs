---
title: replication_controller
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
<tr><td><b>Name</b></td><td><code>replication_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.replication_controller</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `object` | ReplicationControllerStatus represents the current status of a replication controller. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | ReplicationControllerSpec is the specification of a replication controller. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedReplicationController` | `SELECT` | `namespace` | list or watch objects of kind ReplicationController |
| `listCoreV1ReplicationControllerForAllNamespaces` | `SELECT` |  | list or watch objects of kind ReplicationController |
| `readCoreV1NamespacedReplicationController` | `SELECT` | `name, namespace` | read the specified ReplicationController |
| `createCoreV1NamespacedReplicationController` | `INSERT` | `namespace` | create a ReplicationController |
| `deleteCoreV1CollectionNamespacedReplicationController` | `DELETE` | `namespace` | delete collection of ReplicationController |
| `deleteCoreV1NamespacedReplicationController` | `DELETE` | `name, namespace` | delete a ReplicationController |
| `patchCoreV1NamespacedReplicationController` | `EXEC` | `name, namespace` | partially update the specified ReplicationController |
| `patchCoreV1NamespacedReplicationControllerStatus` | `EXEC` | `name, namespace` | partially update status of the specified ReplicationController |
| `readCoreV1NamespacedReplicationControllerStatus` | `EXEC` | `name, namespace` | read status of the specified ReplicationController |
| `replaceCoreV1NamespacedReplicationController` | `EXEC` | `name, namespace` | replace the specified ReplicationController |
| `replaceCoreV1NamespacedReplicationControllerStatus` | `EXEC` | `name, namespace` | replace status of the specified ReplicationController |
| `watchCoreV1NamespacedReplicationController` | `EXEC` | `name, namespace` | watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedReplicationControllerList` | `EXEC` | `namespace` | watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1ReplicationControllerListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. |
