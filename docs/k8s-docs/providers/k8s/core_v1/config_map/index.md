---
title: config_map
hide_title: false
hide_table_of_contents: false
keywords:
  - config_map
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
<tr><td><b>Name</b></td><td><code>config_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.config_map" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="binaryData" /> | `object` | BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. |
| <CopyableCode code="data" /> | `object` | Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. |
| <CopyableCode code="immutable" /> | `boolean` | Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1ConfigMapForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind ConfigMap |
| <CopyableCode code="listCoreV1NamespacedConfigMap" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind ConfigMap |
| <CopyableCode code="readCoreV1NamespacedConfigMap" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified ConfigMap |
| <CopyableCode code="createCoreV1NamespacedConfigMap" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a ConfigMap |
| <CopyableCode code="deleteCoreV1CollectionNamespacedConfigMap" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of ConfigMap |
| <CopyableCode code="deleteCoreV1NamespacedConfigMap" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a ConfigMap |
| <CopyableCode code="patchCoreV1NamespacedConfigMap" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified ConfigMap |
| <CopyableCode code="replaceCoreV1NamespacedConfigMap" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified ConfigMap |
| <CopyableCode code="watchCoreV1ConfigMapListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1NamespacedConfigMap" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind ConfigMap. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedConfigMapList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead. |
