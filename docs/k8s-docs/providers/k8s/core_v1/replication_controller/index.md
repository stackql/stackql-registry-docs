---
title: replication_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_controller
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
<tr><td><b>Name</b></td><td><code>replication_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.replication_controller" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | ReplicationControllerSpec is the specification of a replication controller. |
| <CopyableCode code="status" /> | `object` | ReplicationControllerStatus represents the current status of a replication controller. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedReplicationController" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind ReplicationController |
| <CopyableCode code="listCoreV1ReplicationControllerForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind ReplicationController |
| <CopyableCode code="readCoreV1NamespacedReplicationController" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified ReplicationController |
| <CopyableCode code="createCoreV1NamespacedReplicationController" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a ReplicationController |
| <CopyableCode code="deleteCoreV1CollectionNamespacedReplicationController" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of ReplicationController |
| <CopyableCode code="deleteCoreV1NamespacedReplicationController" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a ReplicationController |
| <CopyableCode code="patchCoreV1NamespacedReplicationController" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified ReplicationController |
| <CopyableCode code="patchCoreV1NamespacedReplicationControllerStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update status of the specified ReplicationController |
| <CopyableCode code="readCoreV1NamespacedReplicationControllerStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read status of the specified ReplicationController |
| <CopyableCode code="replaceCoreV1NamespacedReplicationController" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified ReplicationController |
| <CopyableCode code="replaceCoreV1NamespacedReplicationControllerStatus" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace status of the specified ReplicationController |
| <CopyableCode code="watchCoreV1NamespacedReplicationController" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedReplicationControllerList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1ReplicationControllerListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. |
