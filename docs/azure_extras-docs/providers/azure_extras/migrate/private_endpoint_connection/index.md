---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
  - migrate
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this private endpoint endpoint connection. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/privateEndpointConnections/&#123;privateEndpointConnectionName&#125; |
| `name` | `string` | Name of the private endpoint endpoint connection. |
| `eTag` | `string` | For optimistic concurrency control. |
| `properties` | `object` | Private endpoint connection properties. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/privateEndpointConnections]. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnection_Get` | `SELECT` | `api-version, privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId` | Get information related to a specific private endpoint connection in the project. Returns a json object of type 'privateEndpointConnections' as specified in the models section. |
| `PrivateEndpointConnection_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get all private endpoint connections in the project. Returns a json array of objects of type 'privateEndpointConnections' as specified in the Models section. |
| `PrivateEndpointConnection_Delete` | `DELETE` | `api-version, privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId` | Delete the private endpoint connection from the project. T.<br /> |
| `PrivateEndpointConnection_Update` | `EXEC` | `api-version, privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId, data__properties` | Update a specific private endpoint connection in the project. |
