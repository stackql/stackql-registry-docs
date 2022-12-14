---
title: asc_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - asc_usages
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>asc_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.asc_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | Naming information for this resource type. |
| `unit` | `string` | Unit that the limit and usages are expressed in, such as 'Count'. |
| `currentValue` | `integer` | The current usage of this resource. |
| `limit` | `integer` | The limit (quota) for this resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AscUsages_List` | `SELECT` | `location, subscriptionId` |
