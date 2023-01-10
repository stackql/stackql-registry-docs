---
title: recommendation_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendation_metadata
  - advisor
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
<tr><td><b>Name</b></td><td><code>recommendation_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.advisor.recommendation_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource Id of the metadata entity. |
| `name` | `string` | The name of the metadata entity. |
| `properties` | `object` | The metadata entity properties |
| `type` | `string` | The type of the metadata entity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RecommendationMetadata_Get` | `SELECT` | `name` |
| `RecommendationMetadata_List` | `SELECT` |  |
