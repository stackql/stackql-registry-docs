---
title: resource_quota
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quota
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
<tr><td><b>Name</b></td><td><code>resource_quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.resource_quota</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | ResourceQuotaSpec defines the desired hard limits to enforce for Quota. |
| `status` | `object` | ResourceQuotaStatus defines the enforced hard limits and observed use. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedResourceQuota` | `SELECT` | `namespace, cluster_addr, protocol` | list or watch objects of kind ResourceQuota |
| `listCoreV1ResourceQuotaForAllNamespaces` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind ResourceQuota |
| `readCoreV1NamespacedResourceQuota` | `SELECT` | `name, namespace, cluster_addr, protocol` | read the specified ResourceQuota |
| `createCoreV1NamespacedResourceQuota` | `INSERT` | `namespace, cluster_addr, protocol` | create a ResourceQuota |
| `deleteCoreV1CollectionNamespacedResourceQuota` | `DELETE` | `namespace, cluster_addr, protocol` | delete collection of ResourceQuota |
| `deleteCoreV1NamespacedResourceQuota` | `DELETE` | `name, namespace, cluster_addr, protocol` | delete a ResourceQuota |
| `patchCoreV1NamespacedResourceQuota` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update the specified ResourceQuota |
| `patchCoreV1NamespacedResourceQuotaStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update status of the specified ResourceQuota |
| `readCoreV1NamespacedResourceQuotaStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | read status of the specified ResourceQuota |
| `replaceCoreV1NamespacedResourceQuota` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace the specified ResourceQuota |
| `replaceCoreV1NamespacedResourceQuotaStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace status of the specified ResourceQuota |
| `watchCoreV1NamespacedResourceQuota` | `EXEC` | `name, namespace, cluster_addr, protocol` | watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedResourceQuotaList` | `EXEC` | `namespace, cluster_addr, protocol` | watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1ResourceQuotaListForAllNamespaces` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. |
