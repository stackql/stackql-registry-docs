---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - powerbi_embedded
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_embedded.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Workspace id |
| `name` | `string` | Workspace name |
| `properties` | `object` | Property bag |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Workspaces_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceCollectionName` |
