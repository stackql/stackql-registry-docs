---
title: quota_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_usages
  - postgresql
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
<tr><td><b>Name</b></td><td><code>quota_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.quota_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ARM resource Id |
| `name` | `object` | Name property for quota usage |
| `currentValue` | `integer` | Current Quota usage value |
| `limit` | `integer` | Quota limit |
| `unit` | `string` | Quota unit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationName, subscriptionId` |
| `_list` | `EXEC` | `locationName, subscriptionId` |
