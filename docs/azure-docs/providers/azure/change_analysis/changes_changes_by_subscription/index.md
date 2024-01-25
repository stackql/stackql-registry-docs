---
title: changes_changes_by_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - changes_changes_by_subscription
  - change_analysis
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
<tr><td><b>Name</b></td><td><code>changes_changes_by_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.change_analysis.changes_changes_by_subscription</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `$endTime, $startTime, subscriptionId` |
| `_list` | `EXEC` | `$endTime, $startTime, subscriptionId` |
