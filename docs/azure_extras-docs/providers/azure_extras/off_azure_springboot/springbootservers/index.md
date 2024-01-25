---
title: springbootservers
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootservers
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
<tr><td><b>Name</b></td><td><code>springbootservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.off_azure_springboot.springbootservers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The springbootservers resource definition. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, siteName, springbootserversName, subscriptionId` | List springbootservers resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, siteName, subscriptionId` | List springbootservers resource by resourceGroup |
| `list_by_subscription` | `SELECT` | `siteName, subscriptionId` | List springbootservers resource by subscription |
| `create_or_update` | `INSERT` | `resourceGroupName, siteName, springbootserversName, subscriptionId` | Create springbootservers resource. |
| `delete` | `DELETE` | `resourceGroupName, siteName, springbootserversName, subscriptionId` | Delete springbootservers resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | List springbootservers resource by resourceGroup |
| `_list_by_subscription` | `EXEC` | `siteName, subscriptionId` | List springbootservers resource by subscription |
| `update` | `EXEC` | `resourceGroupName, siteName, springbootserversName, subscriptionId` | Update springbootservers resource. |
