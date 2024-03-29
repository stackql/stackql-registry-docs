---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - autonomous_dev_platform
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.autonomous_dev_platform.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | ADP account properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of an ADP account |
| `list` | `SELECT` | `subscriptionId` | List all ADP accounts available under the subscription |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all ADP accounts available under the resource group |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates an ADP account |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes an ADP account |
| `_list` | `EXEC` | `subscriptionId` | List all ADP accounts available under the subscription |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all ADP accounts available under the resource group |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the account name is valid and is not already in use |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing ADP account |
