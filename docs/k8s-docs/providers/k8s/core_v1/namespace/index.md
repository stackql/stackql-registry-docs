---
title: namespace
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
<tr><td><b>Name</b></td><td><code>namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.namespace</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `spec` | `object` | NamespaceSpec describes the attributes on a Namespace. |
| `status` | `object` | NamespaceStatus is information about the current status of a Namespace. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1Namespace` | `SELECT` |  | list or watch objects of kind Namespace |
| `readCoreV1Namespace` | `SELECT` | `name` | read the specified Namespace |
| `createCoreV1Namespace` | `INSERT` |  | create a Namespace |
| `deleteCoreV1Namespace` | `DELETE` | `name` | delete a Namespace |
| `patchCoreV1Namespace` | `EXEC` | `name` | partially update the specified Namespace |
| `patchCoreV1NamespaceStatus` | `EXEC` | `name` | partially update status of the specified Namespace |
| `readCoreV1NamespaceStatus` | `EXEC` | `name` | read status of the specified Namespace |
| `replaceCoreV1Namespace` | `EXEC` | `name` | replace the specified Namespace |
| `replaceCoreV1NamespaceFinalize` | `EXEC` | `name` | replace finalize of the specified Namespace |
| `replaceCoreV1NamespaceStatus` | `EXEC` | `name` | replace status of the specified Namespace |
| `watchCoreV1Namespace` | `EXEC` | `name` | watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespaceList` | `EXEC` |  | watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead. |
