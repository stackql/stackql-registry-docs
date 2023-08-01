---
title: digital_twins
hide_title: false
hide_table_of_contents: false
keywords:
  - digital_twins
  - digital_twins
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
<tr><td><b>Name</b></td><td><code>digital_twins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.digital_twins.digital_twins</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `identity` | `object` | The managed identity for the DigitalTwinsInstance. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The properties of a DigitalTwinsInstance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DigitalTwins_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get DigitalTwinsInstances resource. |
| `DigitalTwins_List` | `SELECT` | `api-version, subscriptionId` | Get all the DigitalTwinsInstances in a subscription. |
| `DigitalTwins_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get all the DigitalTwinsInstances in a resource group. |
| `DigitalTwins_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a DigitalTwinsInstance. The usual pattern to modify a property is to retrieve the DigitalTwinsInstance and security metadata, and then combine them with the modified values in a new body to update the DigitalTwinsInstance. |
| `DigitalTwins_Delete` | `DELETE` | `api-version, resourceGroupName, resourceName, subscriptionId` | Delete a DigitalTwinsInstance. |
| `DigitalTwins_CheckNameAvailability` | `EXEC` | `api-version, location, subscriptionId, data__name, data__type` | Check if a DigitalTwinsInstance name is available. |
| `DigitalTwins_Update` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Update metadata of DigitalTwinsInstance. |
