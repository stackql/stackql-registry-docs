---
title: entities_get_timeline
hide_title: false
hide_table_of_contents: false
keywords:
  - entities_get_timeline
  - security_insights
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
<tr><td><b>Name</b></td><td><code>entities_get_timeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.entities_get_timeline</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | The timeline result values. |
| `metaData` | `object` | Expansion result metadata. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `EntitiesGetTimeline_list` | `SELECT` | `entityId, resourceGroupName, subscriptionId, workspaceName, data__endTime, data__startTime` |
