---
title: location_based_recommended_action_sessions_result
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_recommended_action_sessions_result
  - maria_db
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
<tr><td><b>Name</b></td><td><code>location_based_recommended_action_sessions_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.location_based_recommended_action_sessions_result</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationName, operationId, subscriptionId` |
| `_list` | `EXEC` | `locationName, operationId, subscriptionId` |
