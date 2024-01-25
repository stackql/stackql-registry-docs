---
title: web_apps_triggered_web_job_history_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_triggered_web_job_history_slot
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_triggered_web_job_history_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_triggered_web_job_history_slot</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | TriggeredJobHistory resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot. |
| `list` | `SELECT` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for List a triggered web job's history for an app, or a deployment slot. |
| `_list` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for List a triggered web job's history for an app, or a deployment slot. |
