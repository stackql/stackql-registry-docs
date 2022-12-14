---
title: sentinel_onboarding_states
hide_title: false
hide_table_of_contents: false
keywords:
  - sentinel_onboarding_states
  - security_insights
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
<tr><td><b>Name</b></td><td><code>sentinel_onboarding_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.sentinel_onboarding_states</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Sentinel onboarding state properties |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SentinelOnboardingStates_Get` | `SELECT` | `resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName` | Get Sentinel onboarding state |
| `SentinelOnboardingStates_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all Sentinel onboarding states |
| `SentinelOnboardingStates_Create` | `INSERT` | `resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName` | Create Sentinel onboarding state |
| `SentinelOnboardingStates_Delete` | `DELETE` | `resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName` | Delete Sentinel onboarding state |
