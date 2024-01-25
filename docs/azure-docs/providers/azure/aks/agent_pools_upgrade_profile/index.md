---
title: agent_pools_upgrade_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_upgrade_profile
  - aks
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
<tr><td><b>Name</b></td><td><code>agent_pools_upgrade_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aks.agent_pools_upgrade_profile</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the agent pool upgrade profile. |
| `name` | `string` | The name of the agent pool upgrade profile. |
| `properties` | `object` | The list of available upgrade versions. |
| `type` | `string` | The type of the agent pool upgrade profile. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |
