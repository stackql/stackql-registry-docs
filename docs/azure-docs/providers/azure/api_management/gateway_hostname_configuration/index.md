---
title: gateway_hostname_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_hostname_configuration
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
<tr><td><b>Name</b></td><td><code>gateway_hostname_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway_hostname_configuration</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Get details of a hostname configuration |
| `list_by_service` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of hostname configurations for the specified gateway. |
| `create_or_update` | `INSERT` | `gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Creates of updates hostname configuration for a Gateway. |
| `delete` | `DELETE` | `If-Match, gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified hostname configuration from the specified Gateway. |
| `_list_by_service` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of hostname configurations for the specified gateway. |
