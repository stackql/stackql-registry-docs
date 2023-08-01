---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
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
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the account property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets or sets the etag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutomationAccount_Get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Get information about an Automation Account. |
| `AutomationAccount_List` | `SELECT` | `subscriptionId` | Retrieve a list of accounts within a given subscription. |
| `AutomationAccount_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `AutomationAccount_CreateOrUpdate` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId` | Create or update automation account. |
| `AutomationAccount_Delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId` | Delete an automation account. |
| `AutomationAccount_Update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Update an automation account. |
