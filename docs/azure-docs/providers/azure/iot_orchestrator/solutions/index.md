---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - iot_orchestrator
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_orchestrator.solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Solution resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Get a Solution |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Solution resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Solution resources by subscription ID |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId, data__extendedLocation` | Create a Solution |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Delete a Solution |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Solution resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Solution resources by subscription ID |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a Solution |
