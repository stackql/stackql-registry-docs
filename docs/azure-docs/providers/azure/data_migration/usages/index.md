---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - data_migration
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
<tr><td><b>Id</b></td><td><code>azure.data_migration.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID of the quota object |
| `name` | `object` | The name of the quota |
| `currentValue` | `number` | The current value of the quota. If null or missing, the current value cannot be determined in the context of the request. |
| `limit` | `number` | The maximum value of the quota. If null or missing, the quota has no maximum, in which case it merely tracks usage. |
| `unit` | `string` | The unit for the quota, such as Count, Bytes, BytesPerSecond, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_List` | `SELECT` | `api-version, location, subscriptionId` |
