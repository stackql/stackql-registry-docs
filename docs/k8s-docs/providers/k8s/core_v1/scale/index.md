---
title: scale
hide_title: false
hide_table_of_contents: false
keywords:
  - scale
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
<tr><td><b>Name</b></td><td><code>scale</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.scale" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | ScaleSpec describes the attributes of a scale subresource. |
| <CopyableCode code="status" /> | `object` | ScaleStatus represents the current status of a scale subresource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="readCoreV1NamespacedReplicationControllerScale" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read scale of the specified ReplicationController |
| <CopyableCode code="patchCoreV1NamespacedReplicationControllerScale" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update scale of the specified ReplicationController |
| <CopyableCode code="replaceCoreV1NamespacedReplicationControllerScale" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace scale of the specified ReplicationController |
