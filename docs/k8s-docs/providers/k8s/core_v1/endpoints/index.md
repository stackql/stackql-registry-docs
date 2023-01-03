---
title: endpoints
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subsets` | `array` | The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1EndpointsForAllNamespaces` | `SELECT` |  | list or watch objects of kind Endpoints |
| `listCoreV1NamespacedEndpoints` | `SELECT` | `namespace` | list or watch objects of kind Endpoints |
| `readCoreV1NamespacedEndpoints` | `SELECT` | `name, namespace` | read the specified Endpoints |
| `createCoreV1NamespacedEndpoints` | `INSERT` | `namespace` | create Endpoints |
| `deleteCoreV1CollectionNamespacedEndpoints` | `DELETE` | `namespace` | delete collection of Endpoints |
| `deleteCoreV1NamespacedEndpoints` | `DELETE` | `name, namespace` | delete Endpoints |
| `patchCoreV1NamespacedEndpoints` | `EXEC` | `name, namespace` | partially update the specified Endpoints |
| `replaceCoreV1NamespacedEndpoints` | `EXEC` | `name, namespace` | replace the specified Endpoints |
| `watchCoreV1EndpointsListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1NamespacedEndpoints` | `EXEC` | `name, namespace` | watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedEndpointsList` | `EXEC` | `namespace` | watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. |
