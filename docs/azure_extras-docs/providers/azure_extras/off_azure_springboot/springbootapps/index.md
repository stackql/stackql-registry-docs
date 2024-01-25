---
title: springbootapps
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootapps
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
<tr><td><b>Name</b></td><td><code>springbootapps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.off_azure_springboot.springbootapps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The springbootapps resource definition. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, siteName, springbootappsName, subscriptionId` | Get a springbootapps resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, siteName, subscriptionId` | List springbootapps resource by resourceGroup |
| `list_by_subscription` | `SELECT` | `siteName, subscriptionId` | List springbootapps resource by subscription |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | List springbootapps resource by resourceGroup |
| `_list_by_subscription` | `EXEC` | `siteName, subscriptionId` | List springbootapps resource by subscription |
| `update` | `EXEC` | `resourceGroupName, siteName, springbootappsName, subscriptionId` | Update a springbootapps resource. |
