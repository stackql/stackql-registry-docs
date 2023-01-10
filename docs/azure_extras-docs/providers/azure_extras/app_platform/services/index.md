---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - app_platform
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The GEO location of the resource. |
| `properties` | `object` | Service properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
| `tags` | `object` | Tags of the service which is a list of key value pairs that describe the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get a Service and its properties. |
| `Services_List` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `Services_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `Services_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create a new Service or update an exiting Service. |
| `Services_Delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Operation to delete a Service. |
| `Services_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `Services_DisableTestEndpoint` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Disable test endpoint functionality for a Service. |
| `Services_EnableTestEndpoint` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Enable test endpoint functionality for a Service. |
| `Services_ListTestKeys` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | List test keys for a Service. |
| `Services_RegenerateTestKey` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__keyType` | Regenerate a test key for a Service. |
| `Services_Start` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Start a Service. |
| `Services_Stop` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Stop a Service. |
| `Services_Update` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Service. |
