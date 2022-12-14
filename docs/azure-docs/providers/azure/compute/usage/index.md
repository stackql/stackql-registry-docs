---
title: usage
hide_title: false
hide_table_of_contents: false
keywords:
  - usage
  - compute
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
<tr><td><b>Name</b></td><td><code>usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The Usage Names. |
| `unit` | `string` | An enum describing the unit of usage measurement. |
| `currentValue` | `integer` | The current usage of the resource. |
| `limit` | `integer` | The maximum permitted usage of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usage_List` | `SELECT` | `location, subscriptionId` |
