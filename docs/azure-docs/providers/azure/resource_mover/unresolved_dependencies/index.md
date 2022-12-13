---
title: unresolved_dependencies
hide_title: false
hide_table_of_contents: false
keywords:
  - unresolved_dependencies
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>unresolved_dependencies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.unresolved_dependencies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Gets or sets the value of  next link. |
| `summaryCollection` | `object` | Summary Collection. |
| `totalCount` | `integer` | Gets the total count. |
| `value` | `array` | Gets or sets the list of unresolved dependencies. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `UnresolvedDependencies_Get` | `SELECT` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` |
