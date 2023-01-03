---
title: service_account
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
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.service_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `imagePullSecrets` | `array` | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `secrets` | `array` | Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `automountServiceAccountToken` | `boolean` | AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listCoreV1NamespacedServiceAccount` | `SELECT` | `namespace` | list or watch objects of kind ServiceAccount |
| `listCoreV1ServiceAccountForAllNamespaces` | `SELECT` |  | list or watch objects of kind ServiceAccount |
| `readCoreV1NamespacedServiceAccount` | `SELECT` | `name, namespace` | read the specified ServiceAccount |
| `createCoreV1NamespacedServiceAccount` | `INSERT` | `namespace` | create a ServiceAccount |
| `deleteCoreV1CollectionNamespacedServiceAccount` | `DELETE` | `namespace` | delete collection of ServiceAccount |
| `deleteCoreV1NamespacedServiceAccount` | `DELETE` | `name, namespace` | delete a ServiceAccount |
| `patchCoreV1NamespacedServiceAccount` | `EXEC` | `name, namespace` | partially update the specified ServiceAccount |
| `replaceCoreV1NamespacedServiceAccount` | `EXEC` | `name, namespace` | replace the specified ServiceAccount |
| `watchCoreV1NamespacedServiceAccount` | `EXEC` | `name, namespace` | watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchCoreV1NamespacedServiceAccountList` | `EXEC` | `namespace` | watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. |
| `watchCoreV1ServiceAccountListForAllNamespaces` | `EXEC` |  | watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. |
