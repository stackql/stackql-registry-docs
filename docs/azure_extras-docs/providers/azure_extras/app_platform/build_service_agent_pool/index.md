---
title: build_service_agent_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_agent_pool
  - app_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>build_service_agent_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.build_service_agent_pool</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BuildServiceAgentPool_Get` | `SELECT` | `agentPoolName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get build service agent pool. |
| `BuildServiceAgentPool_List` | `SELECT` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List build service agent pool. |
| `BuildServiceAgentPool_UpdatePut` | `EXEC` | `agentPoolName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Create or update build service agent pool. |
