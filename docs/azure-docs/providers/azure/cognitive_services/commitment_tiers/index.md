---
title: commitment_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_tiers
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>commitment_tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.commitment_tiers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `planType` | `string` | Commitment plan type. |
| `quota` | `object` | Cognitive Services account commitment quota. |
| `skuName` | `string` | The name of the SKU. Ex - P3. It is typically a letter+number code |
| `tier` | `string` | Commitment period commitment tier. |
| `cost` | `object` | Cognitive Services account commitment cost. |
| `hostingModel` | `string` | Account hosting model. |
| `kind` | `string` | The kind (type) of cognitive service account. |
| `maxCount` | `integer` | Commitment period commitment max count. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `CommitmentTiers_List` | `SELECT` | `location, subscriptionId` |
