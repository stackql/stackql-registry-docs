---
title: config_map
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
<tr><td><b>Name</b></td><td><code>config_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.config_map</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `immutable` | `boolean` | Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `binaryData` | `object` | BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. |
| `data` | `object` | Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1ConfigMapForAllNamespaces` | `SELECT` |  | list or watch objects of kind ConfigMap |
| `listCoreV1NamespacedConfigMap` | `SELECT` | `namespace` | list or watch objects of kind ConfigMap |
| `readCoreV1NamespacedConfigMap` | `SELECT` | `name, namespace` | read the specified ConfigMap |
| `createCoreV1NamespacedConfigMap` | `INSERT` | `namespace` | create a ConfigMap |
| `deleteCoreV1CollectionNamespacedConfigMap` | `DELETE` | `namespace` | delete collection of ConfigMap |
| `deleteCoreV1NamespacedConfigMap` | `DELETE` | `name, namespace` | delete a ConfigMap |
| `patchCoreV1NamespacedConfigMap` | `EXEC` | `name, namespace` | partially update the specified ConfigMap |
| `replaceCoreV1NamespacedConfigMap` | `EXEC` | `name, namespace` | replace the specified ConfigMap |
| `watchCoreV1ConfigMapListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1NamespacedConfigMap` | `EXEC` | `name, namespace` | watch changes to an object of kind ConfigMap. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedConfigMapList` | `EXEC` | `namespace` | watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead. |
