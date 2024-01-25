---
title: portal_config
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_config
  - api_management
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
<tr><td><b>Name</b></td><td><code>portal_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.portal_config</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `portalConfigId, resourceGroupName, serviceName, subscriptionId` | Get the developer portal configuration. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists the developer portal configurations. |
| `create_or_update` | `INSERT` | `If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId` | Create or update the developer portal configuration. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists the developer portal configurations. |
| `update` | `EXEC` | `If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId` | Update the developer portal configuration. |
