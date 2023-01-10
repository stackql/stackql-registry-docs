---
title: usage_aggregates
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_aggregates
  - commerce
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>usage_aggregates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.commerce.usage_aggregates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique Id for the usage aggregate. |
| `name` | `string` | Name of the usage aggregate. |
| `properties` | `object` | Describes a sample of the usageAggregation. |
| `type` | `string` | Type of the resource being returned. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `UsageAggregates_List` | `SELECT` | `reportedEndTime, reportedStartTime, subscriptionId` |
