---
title: workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow
  - dev_hub
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
<tr><td><b>Name</b></td><td><code>workflow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_hub.workflow</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Workflow properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Workflow_Get` | `SELECT` | `resourceGroupName, subscriptionId, workflowName` |
| `Workflow_List` | `SELECT` | `subscriptionId` |
| `Workflow_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Workflow_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workflowName` |
| `Workflow_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workflowName` |
| `Workflow_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, workflowName` |
