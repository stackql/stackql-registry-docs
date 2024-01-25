---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - automation
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
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Gets or sets the etag of the resource. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the account property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Get information about an Automation Account. |
| `list` | `SELECT` | `subscriptionId` | Retrieve a list of accounts within a given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `create_or_update` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId` | Create or update automation account. |
| `delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId` | Delete an automation account. |
| `_list` | `EXEC` | `subscriptionId` | Retrieve a list of accounts within a given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Update an automation account. |
