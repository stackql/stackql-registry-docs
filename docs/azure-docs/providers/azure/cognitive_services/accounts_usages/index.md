---
title: accounts_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_usages
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>accounts_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.accounts_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A metric name. |
| `currentValue` | `number` | Current value for this metric. |
| `limit` | `number` | Maximum value for this metric. |
| `nextResetTime` | `string` | Next reset time for current quota. |
| `quotaPeriod` | `string` | The quota period used to summarize the usage values. |
| `status` | `string` | Cognitive Services account quota usage status. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
