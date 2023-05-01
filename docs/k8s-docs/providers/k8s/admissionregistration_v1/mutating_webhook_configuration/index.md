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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mutating_webhook_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.admissionregistration_v1.mutating_webhook_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `webhooks` | `array` | Webhooks is a list of webhooks and the affected resources and operations. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listAdmissionregistrationV1MutatingWebhookConfiguration` | `SELECT` |  | list or watch objects of kind MutatingWebhookConfiguration |
| `readAdmissionregistrationV1MutatingWebhookConfiguration` | `SELECT` | `name` | read the specified MutatingWebhookConfiguration |
| `createAdmissionregistrationV1MutatingWebhookConfiguration` | `INSERT` |  | create a MutatingWebhookConfiguration |
| `deleteAdmissionregistrationV1CollectionMutatingWebhookConfiguration` | `DELETE` |  | delete collection of MutatingWebhookConfiguration |
| `deleteAdmissionregistrationV1MutatingWebhookConfiguration` | `DELETE` | `name` | delete a MutatingWebhookConfiguration |
| `patchAdmissionregistrationV1MutatingWebhookConfiguration` | `EXEC` | `name` | partially update the specified MutatingWebhookConfiguration |
| `replaceAdmissionregistrationV1MutatingWebhookConfiguration` | `EXEC` | `name` | replace the specified MutatingWebhookConfiguration |
| `watchAdmissionregistrationV1MutatingWebhookConfiguration` | `EXEC` | `name` | watch changes to an object of kind MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchAdmissionregistrationV1MutatingWebhookConfigurationList` | `EXEC` |  | watch individual changes to a list of MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead. |
