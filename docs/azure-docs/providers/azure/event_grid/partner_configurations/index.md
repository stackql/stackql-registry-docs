---
title: partner_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_configurations
  - event_grid
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
<tr><td><b>Name</b></td><td><code>partner_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `type` | `string` | Type of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the partner configuration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerConfigurations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner configurations under a resource group. |
| `PartnerConfigurations_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner configurations under an Azure subscription. |
| `PartnerConfigurations_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId` | Synchronously creates or updates a partner configuration with the specified parameters. |
| `PartnerConfigurations_Delete` | `DELETE` | `resourceGroupName, subscriptionId` | Delete existing partner configuration. |
| `PartnerConfigurations_AuthorizePartner` | `EXEC` | `resourceGroupName, subscriptionId` | Authorize a single partner either by partner registration immutable Id or by partner name. |
| `PartnerConfigurations_Get` | `EXEC` | `resourceGroupName, subscriptionId` | Get properties of a partner configuration. |
| `PartnerConfigurations_UnauthorizePartner` | `EXEC` | `resourceGroupName, subscriptionId` | Unauthorize a single partner either by partner registration immutable Id or by partner name. |
| `PartnerConfigurations_Update` | `EXEC` | `resourceGroupName, subscriptionId` | Synchronously updates a partner configuration with the specified parameters. |
