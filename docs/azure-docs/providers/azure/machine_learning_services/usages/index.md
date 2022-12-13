---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `object` | The Usage Names. |
| `limit` | `integer` | The maximum permitted usage of the resource. |
| `type` | `string` | Specifies the resource type. |
| `unit` | `string` | An enum describing the unit of usage measurement. |
| `amlWorkspaceLocation` | `string` | Region of the AML workspace in the id. |
| `currentValue` | `integer` | The current usage of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_List` | `SELECT` | `location, subscriptionId` |
