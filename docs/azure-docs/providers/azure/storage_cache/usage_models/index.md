---
title: usage_models
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_models
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
<tr><td><b>Name</b></td><td><code>usage_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.usage_models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `display` | `object` | Localized information describing this usage model. |
| `modelName` | `string` | Non-localized keyword name for this usage model. |
| `targetType` | `string` | The type of Storage Target to which this model is applicable (only nfs3 as of this version). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `UsageModels_List` | `SELECT` | `subscriptionId` |
