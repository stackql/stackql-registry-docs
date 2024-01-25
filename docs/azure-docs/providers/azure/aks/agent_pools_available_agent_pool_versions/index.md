---
title: agent_pools_available_agent_pool_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_available_agent_pool_versions
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
<tr><td><b>Name</b></td><td><code>agent_pools_available_agent_pool_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aks.agent_pools_available_agent_pool_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the agent pool version list. |
| `name` | `string` | The name of the agent pool version list. |
| `properties` | `object` | The list of available agent pool versions. |
| `type` | `string` | Type of the agent pool version list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
