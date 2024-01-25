---
title: springbootsites
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootsites
  - off_azure_springboot
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
<tr><td><b>Name</b></td><td><code>springbootsites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.off_azure_springboot.springbootsites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location definition. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The springbootsites resource definition. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, springbootsitesName, subscriptionId` | Get a springbootsites resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List springbootsites resource by resourceGroup. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List springbootsites resource by subscription |
| `create_or_update` | `INSERT` | `resourceGroupName, springbootsitesName, subscriptionId, data__location` | Create a springbootsites resource. |
| `delete` | `DELETE` | `resourceGroupName, springbootsitesName, subscriptionId` | Delete a springbootsites resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List springbootsites resource by resourceGroup. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List springbootsites resource by subscription |
| `trigger_refresh_site` | `EXEC` | `resourceGroupName, springbootsitesName, subscriptionId` | Trigger refresh springbootsites action |
| `update` | `EXEC` | `resourceGroupName, springbootsitesName, subscriptionId` | Update a springbootsites resource. |
