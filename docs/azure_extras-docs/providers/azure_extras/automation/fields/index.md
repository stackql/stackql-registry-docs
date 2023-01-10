---
title: fields
hide_title: false
hide_table_of_contents: false
keywords:
  - fields
  - automation
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
<tr><td><b>Name</b></td><td><code>fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.fields</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets the name of the field. |
| `type` | `string` | Gets or sets the type of the field. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Fields_ListByType` | `SELECT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName` |
