---
title: default_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_rollouts
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
<tr><td><b>Name</b></td><td><code>default_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.default_rollouts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `providerNamespace, rolloutName, subscriptionId` | Gets the default rollout details. |
| `list_by_provider_registration` | `SELECT` | `providerNamespace, subscriptionId` | Gets the list of the rollouts for the given provider. |
| `create_or_update` | `INSERT` | `providerNamespace, rolloutName, subscriptionId` | Creates or updates the rollout details. |
| `delete` | `DELETE` | `providerNamespace, rolloutName, subscriptionId` | Deletes the rollout resource. Rollout must be in terminal state. |
| `_list_by_provider_registration` | `EXEC` | `providerNamespace, subscriptionId` | Gets the list of the rollouts for the given provider. |
| `stop` | `EXEC` | `providerNamespace, rolloutName, subscriptionId` | Stops or cancels the rollout, if in progress. |
