---
title: commitment_plans_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_plan
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
<tr><td><b>Name</b></td><td><code>commitment_plans_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.commitment_plans_plan</code></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commitmentPlanName, resourceGroupName, subscriptionId` | Returns a Cognitive Services commitment plan specified by the parameters. |
| `create_or_update` | `INSERT` | `commitmentPlanName, resourceGroupName, subscriptionId` | Create Cognitive Services commitment plan. |
| `delete` | `DELETE` | `commitmentPlanName, resourceGroupName, subscriptionId` | Deletes a Cognitive Services commitment plan from the resource group.  |
| `update` | `EXEC` | `commitmentPlanName, resourceGroupName, subscriptionId` | Create Cognitive Services commitment plan. |
