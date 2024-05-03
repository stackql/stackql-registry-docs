---
title: mutating_webhook_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - mutating_webhook_configuration
  - admissionregistration_v1
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
<tr><td><b>Name</b></td><td><code>mutating_webhook_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.admissionregistration_v1.mutating_webhook_configuration" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="metadata" /> | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="webhooks" /> | `array` | Webhooks is a list of webhooks and the affected resources and operations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listAdmissionregistrationV1MutatingWebhookConfiguration" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> | list or watch objects of kind MutatingWebhookConfiguration |
| <CopyableCode code="readAdmissionregistrationV1MutatingWebhookConfiguration" /> | `SELECT` | <CopyableCode code="name, cluster_addr, protocol" /> | read the specified MutatingWebhookConfiguration |
| <CopyableCode code="createAdmissionregistrationV1MutatingWebhookConfiguration" /> | `INSERT` | <CopyableCode code="cluster_addr, protocol" /> | create a MutatingWebhookConfiguration |
| <CopyableCode code="deleteAdmissionregistrationV1CollectionMutatingWebhookConfiguration" /> | `DELETE` | <CopyableCode code="cluster_addr, protocol" /> | delete collection of MutatingWebhookConfiguration |
| <CopyableCode code="deleteAdmissionregistrationV1MutatingWebhookConfiguration" /> | `DELETE` | <CopyableCode code="name, cluster_addr, protocol" /> | delete a MutatingWebhookConfiguration |
| <CopyableCode code="patchAdmissionregistrationV1MutatingWebhookConfiguration" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | partially update the specified MutatingWebhookConfiguration |
| <CopyableCode code="replaceAdmissionregistrationV1MutatingWebhookConfiguration" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | replace the specified MutatingWebhookConfiguration |
| <CopyableCode code="watchAdmissionregistrationV1MutatingWebhookConfiguration" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | watch changes to an object of kind MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| <CopyableCode code="watchAdmissionregistrationV1MutatingWebhookConfigurationList" /> | `EXEC` | <CopyableCode code="cluster_addr, protocol" /> | watch individual changes to a list of MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead. |
