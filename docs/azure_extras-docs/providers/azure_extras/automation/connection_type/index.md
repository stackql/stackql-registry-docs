---
title: connection_type
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_type
  - automation
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
<tr><td><b>Name</b></td><td><code>connection_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.connection_type</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the id of the resource. |
| `name` | `string` | Gets the name of the connection type. |
| `properties` | `object` | Properties of the connection type. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectionType_Get` | `SELECT` | `automationAccountName, connectionTypeName, resourceGroupName, subscriptionId` | Retrieve the connection type identified by connection type name. |
| `ConnectionType_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of connection types. |
| `ConnectionType_CreateOrUpdate` | `INSERT` | `automationAccountName, connectionTypeName, resourceGroupName, subscriptionId, data__name, data__properties` | Create a connection type. |
| `ConnectionType_Delete` | `DELETE` | `automationAccountName, connectionTypeName, resourceGroupName, subscriptionId` | Delete the connection type. |
