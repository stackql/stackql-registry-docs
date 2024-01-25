---
title: gateway_route_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_configs
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
<tr><td><b>Name</b></td><td><code>gateway_route_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.gateway_route_configs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId` | Get the Spring Cloud Gateway route configs. |
| `list` | `SELECT` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all Spring Cloud Gateway route configs. |
| `create_or_update` | `INSERT` | `gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId` | Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs. |
| `delete` | `DELETE` | `gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId` | Delete the Spring Cloud Gateway route config. |
| `_list` | `EXEC` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all Spring Cloud Gateway route configs. |
