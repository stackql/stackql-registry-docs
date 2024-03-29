---
title: workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - workbooks
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
<tr><td><b>Name</b></td><td><code>workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.workbooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource etag |
| `identity` | `object` | Identity used for BYOS |
| `kind` | `string` | The kind of workbook. Only valid value is shared. |
| `properties` | `object` | Properties that contain a workbook. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get a single workbook by its resourceName. |
| `list_by_resource_group` | `SELECT` | `category, resourceGroupName, subscriptionId` | Get all Workbooks defined within a specified resource group and category. |
| `list_by_subscription` | `SELECT` | `category, subscriptionId` | Get all Workbooks defined within a specified subscription and category. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a new workbook. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a workbook. |
| `_list_by_resource_group` | `EXEC` | `category, resourceGroupName, subscriptionId` | Get all Workbooks defined within a specified resource group and category. |
| `_list_by_subscription` | `EXEC` | `category, subscriptionId` | Get all Workbooks defined within a specified subscription and category. |
| `_revisions_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the revisions for the workbook defined by its resourceName. |
| `revision_get` | `EXEC` | `resourceGroupName, resourceName, revisionId, subscriptionId` | Get a single workbook revision defined by its revisionId. |
| `revisions_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the revisions for the workbook defined by its resourceName. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a workbook that has already been added. |
