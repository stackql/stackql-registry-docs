---
title: secret
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
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.secret</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
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
