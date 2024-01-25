---
title: build_service_agent_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_agent_pool
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>build_service_agent_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.build_service_agent_pool</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `agentPoolName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get build service agent pool. |
| `list` | `SELECT` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List build service agent pool. |
| `_list` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List build service agent pool. |
