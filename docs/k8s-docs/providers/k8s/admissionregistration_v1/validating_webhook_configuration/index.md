---
title: validating_webhook_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - validating_webhook_configuration
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
<tr><td><b>Name</b></td><td><code>validating_webhook_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.admissionregistration_v1.validating_webhook_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `metadata` | `object` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `webhooks` | `array` | Webhooks is a list of webhooks and the affected resources and operations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listAdmissionregistrationV1ValidatingWebhookConfiguration` | `SELECT` | `cluster_addr, protocol` | list or watch objects of kind ValidatingWebhookConfiguration |
| `readAdmissionregistrationV1ValidatingWebhookConfiguration` | `SELECT` | `name, cluster_addr, protocol` | read the specified ValidatingWebhookConfiguration |
| `createAdmissionregistrationV1ValidatingWebhookConfiguration` | `INSERT` | `cluster_addr, protocol` | create a ValidatingWebhookConfiguration |
| `deleteAdmissionregistrationV1CollectionValidatingWebhookConfiguration` | `DELETE` | `cluster_addr, protocol` | delete collection of ValidatingWebhookConfiguration |
| `deleteAdmissionregistrationV1ValidatingWebhookConfiguration` | `DELETE` | `name, cluster_addr, protocol` | delete a ValidatingWebhookConfiguration |
| `patchAdmissionregistrationV1ValidatingWebhookConfiguration` | `EXEC` | `name, cluster_addr, protocol` | partially update the specified ValidatingWebhookConfiguration |
| `replaceAdmissionregistrationV1ValidatingWebhookConfiguration` | `EXEC` | `name, cluster_addr, protocol` | replace the specified ValidatingWebhookConfiguration |
| `watchAdmissionregistrationV1ValidatingWebhookConfiguration` | `EXEC` | `name, cluster_addr, protocol` | watch changes to an object of kind ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. |
| `watchAdmissionregistrationV1ValidatingWebhookConfigurationList` | `EXEC` | `cluster_addr, protocol` | watch individual changes to a list of ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead. |
