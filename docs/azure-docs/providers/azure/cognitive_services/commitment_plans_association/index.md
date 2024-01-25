---
title: commitment_plans_association
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_association
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
<tr><td><b>Name</b></td><td><code>commitment_plans_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.commitment_plans_association</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | The commitment plan account association properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId` | Gets the association of the Cognitive Services commitment plan. |
| `create_or_update` | `INSERT` | `commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId` | Create or update the association of the Cognitive Services commitment plan. |
| `delete` | `DELETE` | `commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId` | Deletes the association of the Cognitive Services commitment plan. |
