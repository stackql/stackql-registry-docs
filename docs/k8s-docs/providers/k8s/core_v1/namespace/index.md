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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.namespace" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | NamespaceSpec describes the attributes on a Namespace. |
| <CopyableCode code="status" /> | `object` | NamespaceStatus is information about the current status of a Namespace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1Namespace" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind Namespace |
| <CopyableCode code="readCoreV1Namespace" /> | `SELECT` | <CopyableCode code="name, cluster_addr, protocol" /> | read the specified Namespace |
| <CopyableCode code="createCoreV1Namespace" /> | `INSERT` | <CopyableCode code="cluster_addr, protocol" /> | create a Namespace |
| <CopyableCode code="deleteCoreV1Namespace" /> | `DELETE` | <CopyableCode code="name, cluster_addr, protocol" /> | delete a Namespace |
| <CopyableCode code="patchCoreV1Namespace" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | partially update the specified Namespace |
| <CopyableCode code="patchCoreV1NamespaceStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | partially update status of the specified Namespace |
| <CopyableCode code="readCoreV1NamespaceStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | read status of the specified Namespace |
| <CopyableCode code="replaceCoreV1Namespace" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace the specified Namespace |
| <CopyableCode code="replaceCoreV1NamespaceFinalize" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace finalize of the specified Namespace |
| <CopyableCode code="replaceCoreV1NamespaceStatus" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace status of the specified Namespace |
| <CopyableCode code="watchCoreV1Namespace" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespaceList" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead. |
