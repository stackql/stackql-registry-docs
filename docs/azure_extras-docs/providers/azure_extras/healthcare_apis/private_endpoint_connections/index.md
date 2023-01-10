---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - healthcare_apis
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
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Gets the specified private endpoint connection associated with the service. |
| `PrivateEndpointConnections_ListByService` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Lists all private endpoint connections for a service. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update the state of the specified private endpoint connection associated with the service. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a private endpoint connection. |
