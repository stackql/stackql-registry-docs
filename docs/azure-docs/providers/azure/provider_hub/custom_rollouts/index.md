---
title: custom_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_rollouts
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>custom_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.custom_rollouts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomRollouts_Get` | `SELECT` | `providerNamespace, rolloutName, subscriptionId` | Gets the custom rollout details. |
| `CustomRollouts_ListByProviderRegistration` | `SELECT` | `providerNamespace, subscriptionId` | Gets the list of the custom rollouts for the given provider. |
| `CustomRollouts_CreateOrUpdate` | `INSERT` | `providerNamespace, rolloutName, subscriptionId, data__properties` | Creates or updates the rollout details. |
