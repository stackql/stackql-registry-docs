---
title: database_accounts_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_usages
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>database_accounts_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.database_accounts_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A metric name. |
| `currentValue` | `integer` | Current value for this metric |
| `limit` | `integer` | Maximum value for this metric |
| `quotaPeriod` | `string` | The quota period used to summarize the usage values. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
