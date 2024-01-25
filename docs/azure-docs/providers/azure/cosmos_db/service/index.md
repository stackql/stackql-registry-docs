---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the database account. |
| `name` | `string` | The name of the database account. |
| `properties` | `object` | Services response resource. |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, serviceName, subscriptionId` | Gets the status of service. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the status of service. |
| `create` | `INSERT` | `accountName, resourceGroupName, serviceName, subscriptionId` | Creates a service. |
| `delete` | `DELETE` | `accountName, resourceGroupName, serviceName, subscriptionId` | Deletes service with the given serviceName. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the status of service. |
