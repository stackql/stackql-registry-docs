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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.secret</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `immutable` | `boolean` | Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `stringData` | `object` | stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. |
| `type` | `string` | Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `data` | `object` | Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4 |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedSecret` | `SELECT` | `namespace` | list or watch objects of kind Secret |
| `listCoreV1SecretForAllNamespaces` | `SELECT` |  | list or watch objects of kind Secret |
| `readCoreV1NamespacedSecret` | `SELECT` | `name, namespace` | read the specified Secret |
| `createCoreV1NamespacedSecret` | `INSERT` | `namespace` | create a Secret |
| `deleteCoreV1CollectionNamespacedSecret` | `DELETE` | `namespace` | delete collection of Secret |
| `deleteCoreV1NamespacedSecret` | `DELETE` | `name, namespace` | delete a Secret |
| `patchCoreV1NamespacedSecret` | `EXEC` | `name, namespace` | partially update the specified Secret |
| `replaceCoreV1NamespacedSecret` | `EXEC` | `name, namespace` | replace the specified Secret |
| `watchCoreV1NamespacedSecret` | `EXEC` | `name, namespace` | watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedSecretList` | `EXEC` | `namespace` | watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1SecretListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. |
