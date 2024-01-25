---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - power_platform
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
<tr><td><b>Id</b></td><td><code>azure_extras.power_platform.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define configuration for the account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get information about an account. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve a list of accounts within a subscription. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates an account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete an account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve a list of accounts within a subscription. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates an account. |
