---
title: widget_types
hide_title: false
hide_table_of_contents: false
keywords:
  - widget_types
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>widget_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.widget_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | Definition of WidgetType. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WidgetTypes_Get` | `SELECT` | `hubName, resourceGroupName, subscriptionId, widgetTypeName` | Gets a widget type in the specified hub. |
| `WidgetTypes_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all available widget types in the specified hub. |
