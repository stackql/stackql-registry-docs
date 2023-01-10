---
title: controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - controllers
  - dev_spaces
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
<tr><td><b>Name</b></td><td><code>controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_spaces.controllers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Region where the Azure resource is located. |
| `properties` | `object` |  |
| `sku` | `object` | Model representing SKU for Azure Dev Spaces Controller. |
| `tags` | `object` | Tags for the Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Controllers_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the properties for an Azure Dev Spaces Controller. |
| `Controllers_List` | `SELECT` | `subscriptionId` | Lists all the Azure Dev Spaces Controllers with their properties in the subscription. |
| `Controllers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription. |
| `Controllers_Create` | `INSERT` | `name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku` | Creates an Azure Dev Spaces Controller with the specified create parameters. |
| `Controllers_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes an existing Azure Dev Spaces Controller. |
| `Controllers_ListConnectionDetails` | `EXEC` | `name, resourceGroupName, subscriptionId, data__targetContainerHostResourceId` | Lists connection details for the underlying container resources of an Azure Dev Spaces Controller. |
| `Controllers_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters. |
