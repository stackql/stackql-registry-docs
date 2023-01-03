---
title: pod_template
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
<tr><td><b>Name</b></td><td><code>pod_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.pod_template</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `template` | `object` | PodTemplateSpec describes the data a pod should have when created from a template |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedPodTemplate` | `SELECT` | `namespace` | list or watch objects of kind PodTemplate |
| `listCoreV1PodTemplateForAllNamespaces` | `SELECT` |  | list or watch objects of kind PodTemplate |
| `readCoreV1NamespacedPodTemplate` | `SELECT` | `name, namespace` | read the specified PodTemplate |
| `createCoreV1NamespacedPodTemplate` | `INSERT` | `namespace` | create a PodTemplate |
| `deleteCoreV1CollectionNamespacedPodTemplate` | `DELETE` | `namespace` | delete collection of PodTemplate |
| `deleteCoreV1NamespacedPodTemplate` | `DELETE` | `name, namespace` | delete a PodTemplate |
| `patchCoreV1NamespacedPodTemplate` | `EXEC` | `name, namespace` | partially update the specified PodTemplate |
| `replaceCoreV1NamespacedPodTemplate` | `EXEC` | `name, namespace` | replace the specified PodTemplate |
| `watchCoreV1NamespacedPodTemplate` | `EXEC` | `name, namespace` | watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedPodTemplateList` | `EXEC` | `namespace` | watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1PodTemplateListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead. |