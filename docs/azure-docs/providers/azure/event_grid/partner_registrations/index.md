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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the partner registration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerRegistrations_Get` | `SELECT` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Gets a partner registration with the specified parameters. |
| `PartnerRegistrations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner registrations under a resource group. |
| `PartnerRegistrations_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner registrations under an Azure subscription. |
| `PartnerRegistrations_CreateOrUpdate` | `INSERT` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Creates a new partner registration with the specified parameters. |
| `PartnerRegistrations_Delete` | `DELETE` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Deletes a partner registration with the specified parameters. |
| `PartnerRegistrations_Update` | `EXEC` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Updates a partner registration with the specified parameters. |
