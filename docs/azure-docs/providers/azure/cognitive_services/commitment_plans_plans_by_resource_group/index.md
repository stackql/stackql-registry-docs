---
title: commitment_plans_plans_by_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_plans_by_resource_group
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
<tr><td><b>Name</b></td><td><code>commitment_plans_plans_by_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.commitment_plans_plans_by_resource_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `kind` | `string` | The kind (type) of cognitive service account. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of Cognitive Services account commitment plan. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` |
