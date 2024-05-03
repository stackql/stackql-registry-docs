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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.resource_quota" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | ResourceQuotaSpec defines the desired hard limits to enforce for Quota. |
| <CopyableCode code="status" /> | `object` | ResourceQuotaStatus defines the enforced hard limits and observed use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedResourceQuota" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind ResourceQuota |
| <CopyableCode code="listCoreV1ResourceQuotaForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind ResourceQuota |
| <CopyableCode code="readCoreV1NamespacedResourceQuota" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified ResourceQuota |
| <CopyableCode code="createCoreV1NamespacedResourceQuota" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a ResourceQuota |
| <CopyableCode code="deleteCoreV1CollectionNamespacedResourceQuota" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of ResourceQuota |
| <CopyableCode code="deleteCoreV1NamespacedResourceQuota" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a ResourceQuota |
| <CopyableCode code="patchCoreV1NamespacedResourceQuota" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified ResourceQuota |
| <CopyableCode code="patchCoreV1NamespacedResourceQuotaStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update status of the specified ResourceQuota |
| <CopyableCode code="readCoreV1NamespacedResourceQuotaStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read status of the specified ResourceQuota |
| <CopyableCode code="replaceCoreV1NamespacedResourceQuota" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified ResourceQuota |
| <CopyableCode code="replaceCoreV1NamespacedResourceQuotaStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace status of the specified ResourceQuota |
| <CopyableCode code="watchCoreV1NamespacedResourceQuota" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedResourceQuotaList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1ResourceQuotaListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. |
