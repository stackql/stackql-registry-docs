---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - test_base
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (either system assigned, or none) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Test Base Account resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Gets a Test Base Account. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the Test Base Accounts in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the Test Base Accounts in a subscription. |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Create or replace (overwrite/recreate, with potential downtime) a Test Base Account in the specified subscription. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a Test Base Account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the Test Base Accounts in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the Test Base Accounts in a subscription. |
| `check_package_name_availability` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName, data__applicationName, data__name, data__version` | Checks that the Test Base Package name and version is valid and is not already in use. |
| `offboard` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Offboard a Test Base Account. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Update an existing Test Base Account. |
