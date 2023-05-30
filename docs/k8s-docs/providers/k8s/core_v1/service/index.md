---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `spec` | `object` | ServiceSpec describes the attributes that a user creates on a service. |
| `status` | `object` | ServiceStatus represents the current status of a service. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedService` | `SELECT` | `namespace, cluster_addr, protocol` | list or watch objects of kind Service |
| `listCoreV1ServiceForAllNamespaces` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind Service |
| `readCoreV1NamespacedService` | `SELECT` | `name, namespace, cluster_addr, protocol` | read the specified Service |
| `createCoreV1NamespacedService` | `INSERT` | `namespace, cluster_addr, protocol` | create a Service |
| `deleteCoreV1CollectionNamespacedService` | `DELETE` | `namespace, cluster_addr, protocol` | delete collection of Service |
| `deleteCoreV1NamespacedService` | `DELETE` | `name, namespace, cluster_addr, protocol` | delete a Service |
| `patchCoreV1NamespacedService` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update the specified Service |
| `patchCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | partially update status of the specified Service |
| `readCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | read status of the specified Service |
| `replaceCoreV1NamespacedService` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace the specified Service |
| `replaceCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace, cluster_addr, protocol` | replace status of the specified Service |
| `watchCoreV1NamespacedService` | `EXEC` | `name, namespace, cluster_addr, protocol` | watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedServiceList` | `EXEC` | `namespace, cluster_addr, protocol` | watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1ServiceListForAllNamespaces` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. |
