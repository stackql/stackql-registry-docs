---
title: node
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
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.node</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `object` | NodeStatus is information about the current status of a node. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | NodeSpec describes the attributes that a node is created with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1Node` | `SELECT` |  | list or watch objects of kind Node |
| `readCoreV1Node` | `SELECT` | `name` | read the specified Node |
| `createCoreV1Node` | `INSERT` |  | create a Node |
| `deleteCoreV1CollectionNode` | `DELETE` |  | delete collection of Node |
| `deleteCoreV1Node` | `DELETE` | `name` | delete a Node |
| `patchCoreV1Node` | `EXEC` | `name` | partially update the specified Node |
| `patchCoreV1NodeStatus` | `EXEC` | `name` | partially update status of the specified Node |
| `readCoreV1NodeStatus` | `EXEC` | `name` | read status of the specified Node |
| `replaceCoreV1Node` | `EXEC` | `name` | replace the specified Node |
| `replaceCoreV1NodeStatus` | `EXEC` | `name` | replace status of the specified Node |
| `watchCoreV1Node` | `EXEC` | `name` | watch changes to an object of kind Node. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NodeList` | `EXEC` |  | watch individual changes to a list of Node. deprecated: use the 'watch' parameter with a list operation instead. |
