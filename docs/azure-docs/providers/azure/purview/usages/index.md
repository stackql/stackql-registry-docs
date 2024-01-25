---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - purview
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id |
| `name` | `object` | Quota name |
| `currentValue` | `integer` | Current usage quota value |
| `limit` | `integer` | Usage quota limit |
| `unit` | `string` | Quota usage unit. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, location, subscriptionId` |
| `_get` | `EXEC` | `api-version, location, subscriptionId` |
