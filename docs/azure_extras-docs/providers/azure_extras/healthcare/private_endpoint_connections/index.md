---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - healthcare
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Gets the specified private endpoint connection associated with the service. |
| `list_by_service` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Lists all private endpoint connections for a service. |
| `create_or_update` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update the state of the specified private endpoint connection associated with the service. |
| `delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a private endpoint connection. |
| `_list_by_service` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Lists all private endpoint connections for a service. |