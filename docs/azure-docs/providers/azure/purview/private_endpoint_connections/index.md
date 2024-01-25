---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - purview
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the identifier. |
| `name` | `string` | Gets or sets the name. |
| `properties` | `object` | A private endpoint connection properties class. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Get a private endpoint connection |
| `list_by_account` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get private endpoint connections for account |
| `create_or_update` | `INSERT` | `accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Create or update a private endpoint connection |
| `delete` | `DELETE` | `accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Delete a private endpoint connection |
| `_list_by_account` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Get private endpoint connections for account |
