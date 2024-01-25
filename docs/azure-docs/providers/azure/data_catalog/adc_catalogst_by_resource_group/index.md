---
title: adc_catalogst_by_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - adc_catalogst_by_resource_group
  - data_catalog
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
<tr><td><b>Name</b></td><td><code>adc_catalogst_by_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_catalog.adc_catalogst_by_resource_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `etag` | `string` | Resource etag |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the data catalog. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` |
