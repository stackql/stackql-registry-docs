---
title: content_key_policies_policy_properties_with_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies_policy_properties_with_secrets
  - media_services
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_key_policies_policy_properties_with_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.content_key_policies_policy_properties_with_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description for the Policy. |
| `created` | `string` | The creation date of the Policy |
| `lastModified` | `string` | The last modified date of the Policy |
| `options` | `array` | The Key Policy options. |
| `policyId` | `string` | The legacy Policy ID. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` |
