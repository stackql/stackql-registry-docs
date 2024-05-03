---
title: service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account
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
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.service_account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="automountServiceAccountToken" /> | `boolean` | AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. |
| <CopyableCode code="imagePullSecrets" /> | `array` | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="secrets" /> | `array` | Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listCoreV1NamespacedServiceAccount" /> | `SELECT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | list or watch objects of kind ServiceAccount |
| <CopyableCode code="listCoreV1ServiceAccountForAllNamespaces" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind ServiceAccount |
| <CopyableCode code="readCoreV1NamespacedServiceAccount" /> | `SELECT` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | read the specified ServiceAccount |
| <CopyableCode code="createCoreV1NamespacedServiceAccount" /> | `INSERT` | <CopyableCode code="namespace, cluster_addr, protocol" /> | create a ServiceAccount |
| <CopyableCode code="deleteCoreV1CollectionNamespacedServiceAccount" /> | `DELETE` | <CopyableCode code="namespace, cluster_addr, protocol" /> | delete collection of ServiceAccount |
| <CopyableCode code="deleteCoreV1NamespacedServiceAccount" /> | `DELETE` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | delete a ServiceAccount |
| <CopyableCode code="patchCoreV1NamespacedServiceAccount" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | partially update the specified ServiceAccount |
| <CopyableCode code="replaceCoreV1NamespacedServiceAccount" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | replace the specified ServiceAccount |
| <CopyableCode code="watchCoreV1NamespacedServiceAccount" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchCoreV1NamespacedServiceAccountList" /> | `EXEC` | <CopyableCode code="namespace, cluster_addr, protocol" /> | watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. |
| <CopyableCode code="watchCoreV1ServiceAccountListForAllNamespaces" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. |
