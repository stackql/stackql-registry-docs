---
title: racks
hide_title: false
hide_table_of_contents: false
keywords:
  - racks
  - nexus
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
<tr><td><b>Name</b></td><td><code>racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.racks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `rackName, resourceGroupName, subscriptionId` | Get properties of the provided rack. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of racks in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of racks in the provided subscription. |
| `create_or_update` | `INSERT` | `rackName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new rack or update properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `delete` | `DELETE` | `rackName, resourceGroupName, subscriptionId` | Delete the provided rack.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of racks in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of racks in the provided subscription. |
| `update` | `EXEC` | `rackName, resourceGroupName, subscriptionId` | Patch properties of the provided rack, or update the tags associated with the rack. Properties and tag updates can be done independently. |
