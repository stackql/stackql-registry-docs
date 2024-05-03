---
title: secret
hide_title: false
hide_table_of_contents: false
keywords:
  - secret
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
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.secret" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="data" /> | `object` | Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4 |
| <CopyableCode code="immutable" /> | `boolean` | Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="stringData" /> | `object` | stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. |
| <CopyableCode code="type" /> | `string` | Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedSecret" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind Secret |
| <CopyableCode code="listCoreV1SecretForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind Secret |
| <CopyableCode code="readCoreV1NamespacedSecret" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified Secret |
| <CopyableCode code="createCoreV1NamespacedSecret" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a Secret |
| <CopyableCode code="deleteCoreV1CollectionNamespacedSecret" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of Secret |
| <CopyableCode code="deleteCoreV1NamespacedSecret" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a Secret |
| <CopyableCode code="patchCoreV1NamespacedSecret" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified Secret |
| <CopyableCode code="replaceCoreV1NamespacedSecret" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified Secret |
| <CopyableCode code="watchCoreV1NamespacedSecret" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedSecretList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1SecretListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. |
