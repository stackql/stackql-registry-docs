---
title: disk_pools_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pools_outbound_network_dependencies_endpoints
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>disk_pools_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.disk_pools_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The type of service accessed by the App Service Environment, e.g., Azure Storage, Azure SQL Database, and Azure Active Directory. |
| `endpoints` | `array` | The endpoints that the App Service Environment reaches the service at. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `diskPoolName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` |
