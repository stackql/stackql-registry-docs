---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="subsets" /> | `array` | The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1EndpointsForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind Endpoints |
| <CopyableCode code="listCoreV1NamespacedEndpoints" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind Endpoints |
| <CopyableCode code="readCoreV1NamespacedEndpoints" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified Endpoints |
| <CopyableCode code="createCoreV1NamespacedEndpoints" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create Endpoints |
| <CopyableCode code="deleteCoreV1CollectionNamespacedEndpoints" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of Endpoints |
| <CopyableCode code="deleteCoreV1NamespacedEndpoints" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete Endpoints |
| <CopyableCode code="patchCoreV1NamespacedEndpoints" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified Endpoints |
| <CopyableCode code="replaceCoreV1NamespacedEndpoints" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified Endpoints |
| <CopyableCode code="watchCoreV1EndpointsListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1NamespacedEndpoints" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedEndpointsList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. |
