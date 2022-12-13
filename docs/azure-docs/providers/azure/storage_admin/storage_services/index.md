---
title: storage_services
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_services
  - storage_admin
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
<tr><td><b>Name</b></td><td><code>storage_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_admin.storage_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource Name. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | The properties for service name. |
| `type` | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageServices_Get` | `SELECT` | `resourceGroup, serviceName, subscriptionId` | Returns the specified storage service. |
| `StorageServices_Create` | `INSERT` | `resourceGroup, serviceName, subscriptionId` | Create the specified storage resource. |
| `StorageServices_ListRG` | `EXEC` | `resourceGroup, subscriptionId` | Returns the storage services list under the specified resource group and subscription. |
| `StorageServices_ListSub` | `EXEC` | `subscriptionId` | Returns the storage services list under the specified subscription. |
