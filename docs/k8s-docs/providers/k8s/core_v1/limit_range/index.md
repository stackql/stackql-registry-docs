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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>limit_range</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.limit_range" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | LimitRangeSpec defines a min/max usage limit for resources that match on kind. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1LimitRangeForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind LimitRange |
| <CopyableCode code="listCoreV1NamespacedLimitRange" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind LimitRange |
| <CopyableCode code="readCoreV1NamespacedLimitRange" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified LimitRange |
| <CopyableCode code="createCoreV1NamespacedLimitRange" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a LimitRange |
| <CopyableCode code="deleteCoreV1CollectionNamespacedLimitRange" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of LimitRange |
| <CopyableCode code="deleteCoreV1NamespacedLimitRange" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a LimitRange |
| <CopyableCode code="patchCoreV1NamespacedLimitRange" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified LimitRange |
| <CopyableCode code="replaceCoreV1NamespacedLimitRange" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified LimitRange |
| <CopyableCode code="watchCoreV1LimitRangeListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1NamespacedLimitRange" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedLimitRangeList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead. |
