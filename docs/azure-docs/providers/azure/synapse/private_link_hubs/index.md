---
title: private_link_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hubs
  - synapse
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
<tr><td><b>Name</b></td><td><code>private_link_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.private_link_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | PrivateLinkHub properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkHubs_Get` | `SELECT` |  | Gets a privateLinkHub |
| `PrivateLinkHubs_List` | `SELECT` | `subscriptionId` | Returns a list of privateLinkHubs in a subscription |
| `PrivateLinkHubs_ListByResourceGroup` | `SELECT` |  | Returns a list of privateLinkHubs in a resource group |
| `PrivateLinkHubs_CreateOrUpdate` | `INSERT` |  | Creates or updates a privateLinkHub |
| `PrivateLinkHubs_Delete` | `DELETE` |  | Deletes a privateLinkHub |
| `PrivateLinkHubs_Update` | `EXEC` |  | Updates a privateLinkHub |
