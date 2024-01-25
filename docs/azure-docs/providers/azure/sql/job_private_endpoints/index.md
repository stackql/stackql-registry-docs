---
title: job_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - job_private_endpoints
  - sql
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
<tr><td><b>Name</b></td><td><code>job_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_private_endpoints</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId` | Gets a private endpoint. |
| `list_by_agent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of job agent private endpoints. |
| `create_or_update` | `INSERT` | `jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId` | Creates or updates a private endpoint. |
| `delete` | `DELETE` | `jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId` | Deletes a private endpoint. |
| `_list_by_agent` | `EXEC` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of job agent private endpoints. |
