---
title: deleted_automation_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_automation_accounts
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
<tr><td><b>Name</b></td><td><code>deleted_automation_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.deleted_automation_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets or sets name of the resource. |
| `location` | `string` | Gets or sets the location of the resource. |
| `properties` | `object` | Definition of the deleted automation account properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
