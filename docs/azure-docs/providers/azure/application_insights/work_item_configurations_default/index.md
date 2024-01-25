---
title: work_item_configurations_default
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations_default
  - application_insights
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
<tr><td><b>Name</b></td><td><code>work_item_configurations_default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.work_item_configurations_default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ConfigDisplayName` | `string` | Configuration friendly name |
| `ConfigProperties` | `string` | Serialized JSON object for detailed properties |
| `ConnectorId` | `string` | Connector identifier where work item is created |
| `Id` | `string` | Unique Id for work item |
| `IsDefault` | `boolean` | Boolean value indicating whether configuration is default |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
