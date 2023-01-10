---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `object` | The Resource Name. |
| `unit` | `string` | An enum describing the unit of quota measurement. |
| `amlWorkspaceLocation` | `string` | Region of the AML workspace in the id. |
| `limit` | `integer` | The maximum permitted quota of the resource. |
| `type` | `string` | Specifies the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Quotas_List` | `SELECT` | `location, subscriptionId` | Gets the currently assigned Workspace Quotas based on VMFamily. |
| `Quotas_Update` | `EXEC` | `location, subscriptionId` | Update quota for each VM family in workspace. |
