---
title: schema
hide_title: false
hide_table_of_contents: false
keywords:
  - schema
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | Metadata for search results. |
| `value` | `array` | The array of result values. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Schema_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
