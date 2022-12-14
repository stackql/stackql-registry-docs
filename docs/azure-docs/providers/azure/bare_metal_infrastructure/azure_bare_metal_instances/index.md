---
title: azure_bare_metal_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_instances
  - bare_metal_infrastructure
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
<tr><td><b>Name</b></td><td><code>azure_bare_metal_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bare_metal_infrastructure.azure_bare_metal_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an AzureBareMetal instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AzureBareMetalInstances_Get` | `SELECT` | `azureBareMetalInstanceName, resourceGroupName, subscriptionId` | Gets an Azure BareMetal instance for the specified subscription, resource group, and instance name. |
| `AzureBareMetalInstances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of AzureBareMetal instances in the specified subscription and resource group. The operations returns various properties of each Azure BareMetal instance. |
| `AzureBareMetalInstances_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of AzureBareMetal instances in the specified subscription. The operations returns various properties of each Azure BareMetal instance. |
| `AzureBareMetalInstances_Update` | `EXEC` | `azureBareMetalInstanceName, resourceGroupName, subscriptionId` | Patches the Tags field of a Azure BareMetal instance for the specified subscription, resource group, and instance name. |
