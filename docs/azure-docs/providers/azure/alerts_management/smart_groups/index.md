---
title: smart_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - smart_groups
  - alerts_management
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
<tr><td><b>Name</b></td><td><code>smart_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.alerts_management.smart_groups</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `change_state` | `EXEC` | `api-version, newState, smartGroupId, subscriptionId` | Change the state of a Smart Group. |
| `get_by_id` | `EXEC` | `api-version, smartGroupId, subscriptionId` | Get information related to a specific Smart Group. |
