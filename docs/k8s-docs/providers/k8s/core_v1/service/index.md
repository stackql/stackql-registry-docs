---
title: service
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | ServiceSpec describes the attributes that a user creates on a service. |
| `status` | `object` | ServiceStatus represents the current status of a service. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedService` | `SELECT` | `namespace` | list or watch objects of kind Service |
| `listCoreV1ServiceForAllNamespaces` | `SELECT` |  | list or watch objects of kind Service |
| `readCoreV1NamespacedService` | `SELECT` | `name, namespace` | read the specified Service |
| `createCoreV1NamespacedService` | `INSERT` | `namespace` | create a Service |
| `deleteCoreV1CollectionNamespacedService` | `DELETE` | `namespace` | delete collection of Service |
| `deleteCoreV1NamespacedService` | `DELETE` | `name, namespace` | delete a Service |
| `patchCoreV1NamespacedService` | `EXEC` | `name, namespace` | partially update the specified Service |
| `patchCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace` | partially update status of the specified Service |
| `readCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace` | read status of the specified Service |
| `replaceCoreV1NamespacedService` | `EXEC` | `name, namespace` | replace the specified Service |
| `replaceCoreV1NamespacedServiceStatus` | `EXEC` | `name, namespace` | replace status of the specified Service |
| `watchCoreV1NamespacedService` | `EXEC` | `name, namespace` | watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedServiceList` | `EXEC` | `namespace` | watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1ServiceListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. |
