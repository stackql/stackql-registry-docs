---
title: partner_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_registrations
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
<tr><td><b>Name</b></td><td><code>partner_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the partner registration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Gets a partner registration with the specified parameters. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner registrations under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the partner registrations under an Azure subscription. |
| `create_or_update` | `INSERT` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Creates a new partner registration with the specified parameters. |
| `delete` | `DELETE` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Deletes a partner registration with the specified parameters. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the partner registrations under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the partner registrations under an Azure subscription. |
| `update` | `EXEC` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Updates a partner registration with the specified parameters. |
