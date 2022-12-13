---
title: my_workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - my_workbooks
  - application_insights
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
<tr><td><b>Name</b></td><td><code>my_workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.my_workbooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `type` | `string` | Azure resource type |
| `etag` | `` | Resource etag |
| `identity` | `object` | Customer Managed Identity |
| `location` | `string` | Resource location |
| `kind` | `string` | The kind of workbook. Choices are user and shared. |
| `properties` | `object` | Properties that contain a private workbook. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MyWorkbooks_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get a single private workbook by its resourceName. |
| `MyWorkbooks_ListByResourceGroup` | `SELECT` | `category, resourceGroupName, subscriptionId` | Get all private workbooks defined within a specified resource group and category. |
| `MyWorkbooks_ListBySubscription` | `SELECT` | `category, subscriptionId` | Get all private workbooks defined within a specified subscription and category. |
| `MyWorkbooks_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a new private workbook. |
| `MyWorkbooks_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a private workbook. |
| `MyWorkbooks_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a private workbook that has already been added. |
