---
title: connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connection
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
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.connection</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Connection_Get` | `SELECT` | `automationAccountName, connectionName, resourceGroupName, subscriptionId` | Retrieve the connection identified by connection name. |
| `Connection_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of connections. |
| `Connection_CreateOrUpdate` | `INSERT` | `automationAccountName, connectionName, resourceGroupName, subscriptionId, data__name, data__properties` | Create or update a connection. |
| `Connection_Delete` | `DELETE` | `automationAccountName, connectionName, resourceGroupName, subscriptionId` | Delete the connection. |
| `Connection_Update` | `EXEC` | `automationAccountName, connectionName, resourceGroupName, subscriptionId` | Update a connection. |
