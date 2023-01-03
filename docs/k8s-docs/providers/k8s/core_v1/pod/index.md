---
title: pod
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
<tr><td><b>Name</b></td><td><code>pod</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.pod</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedPod` | `SELECT` | `namespace` | list or watch objects of kind Pod |
| `listCoreV1PodForAllNamespaces` | `SELECT` |  | list or watch objects of kind Pod |
| `readCoreV1NamespacedPod` | `SELECT` | `name, namespace` | read the specified Pod |
| `createCoreV1NamespacedPod` | `INSERT` | `namespace` | create a Pod |
| `deleteCoreV1CollectionNamespacedPod` | `DELETE` | `namespace` | delete collection of Pod |
| `deleteCoreV1NamespacedPod` | `DELETE` | `name, namespace` | delete a Pod |
| `patchCoreV1NamespacedPod` | `EXEC` | `name, namespace` | partially update the specified Pod |
| `patchCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace` | partially update ephemeralcontainers of the specified Pod |
| `patchCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace` | partially update status of the specified Pod |
| `readCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace` | read ephemeralcontainers of the specified Pod |
| `readCoreV1NamespacedPodLog` | `EXEC` | `name, namespace` | read log of the specified Pod |
| `readCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace` | read status of the specified Pod |
| `replaceCoreV1NamespacedPod` | `EXEC` | `name, namespace` | replace the specified Pod |
| `replaceCoreV1NamespacedPodEphemeralcontainers` | `EXEC` | `name, namespace` | replace ephemeralcontainers of the specified Pod |
| `replaceCoreV1NamespacedPodStatus` | `EXEC` | `name, namespace` | replace status of the specified Pod |
| `watchCoreV1NamespacedPod` | `EXEC` | `name, namespace` | watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedPodList` | `EXEC` | `namespace` | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1PodListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. |
