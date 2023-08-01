---
title: limit_range
hide_title: false
hide_table_of_contents: false
keywords:
  - limit_range
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
<tr><td><b>Name</b></td><td><code>limit_range</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.limit_range</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | LimitRangeSpec defines a min/max usage limit for resources that match on kind. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1LimitRangeForAllNamespaces` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind LimitRange |
| `listCoreV1NamespacedLimitRange` | `SELECT` | `namespace, cluster_addr, protocol` | list or watch objects of kind LimitRange |
| `readCoreV1NamespacedLimitRange` | `SELECT` | `name, namespace, cluster_addr, protocol` | read the specified LimitRange |
| `createCoreV1NamespacedLimitRange` | `INSERT` | `namespace, cluster_addr, protocol` | create a LimitRange |
| `deleteCoreV1CollectionNamespacedLimitRange` | `DELETE` | `namespace, cluster_addr, protocol` | delete collection of LimitRange |
| `deleteCoreV1NamespacedLimitRange` | `DELETE` | `name, namespace, cluster_addr, protocol` | delete a LimitRange |
| `patchCoreV1NamespacedLimitRange` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update the specified LimitRange |
| `replaceCoreV1NamespacedLimitRange` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace the specified LimitRange |
| `watchCoreV1LimitRangeListForAllNamespaces` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1NamespacedLimitRange` | `EXEC` | `name, namespace, cluster_addr, protocol` | watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedLimitRangeList` | `EXEC` | `namespace, cluster_addr, protocol` | watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead. |
