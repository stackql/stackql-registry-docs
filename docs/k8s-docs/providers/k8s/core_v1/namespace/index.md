---
title: namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace
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
<tr><td><b>Name</b></td><td><code>namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.namespace</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | NamespaceSpec describes the attributes on a Namespace. |
| `status` | `object` | NamespaceStatus is information about the current status of a Namespace. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1Namespace` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind Namespace |
| `readCoreV1Namespace` | `SELECT` | `name, cluster_addr, protocol` | read the specified Namespace |
| `createCoreV1Namespace` | `INSERT` | `cluster_addr, protocol` | create a Namespace |
| `deleteCoreV1Namespace` | `DELETE` | `name, cluster_addr, protocol` | delete a Namespace |
| `patchCoreV1Namespace` | `EXEC` | `name, cluster_addr, protocol` | partially update the specified Namespace |
| `patchCoreV1NamespaceStatus` | `EXEC` | `name, cluster_addr, protocol` | partially update status of the specified Namespace |
| `readCoreV1NamespaceStatus` | `EXEC` | `name, cluster_addr, protocol` | read status of the specified Namespace |
| `replaceCoreV1Namespace` | `EXEC` | `name, cluster_addr, protocol` | replace the specified Namespace |
| `replaceCoreV1NamespaceFinalize` | `EXEC` | `name, cluster_addr, protocol` | replace finalize of the specified Namespace |
| `replaceCoreV1NamespaceStatus` | `EXEC` | `name, cluster_addr, protocol` | replace status of the specified Namespace |
| `watchCoreV1Namespace` | `EXEC` | `name, cluster_addr, protocol` | watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespaceList` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead. |
