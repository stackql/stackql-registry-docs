---
title: environments_inbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_inbound_network_dependencies_endpoints
  - app_service
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
<tr><td><b>Name</b></td><td><code>environments_inbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.environments_inbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Short text describing the purpose of the network traffic. |
| `endpoints` | `array` | The IP addresses that network traffic will originate from in cidr notation. |
| `ports` | `array` | The ports that network traffic will arrive to the App Service Environment at. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `name, resourceGroupName, subscriptionId` |
