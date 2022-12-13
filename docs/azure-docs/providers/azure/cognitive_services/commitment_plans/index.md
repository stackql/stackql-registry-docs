---
title: commitment_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans
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
<tr><td><b>Name</b></td><td><code>commitment_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.commitment_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | Properties of Cognitive Services account commitment plan. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CommitmentPlans_Get` | `SELECT` | `accountName, commitmentPlanName, resourceGroupName, subscriptionId` | Gets the specified commitmentPlans associated with the Cognitive Services account. |
| `CommitmentPlans_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the commitmentPlans associated with the Cognitive Services account. |
| `CommitmentPlans_CreateOrUpdate` | `INSERT` | `accountName, commitmentPlanName, resourceGroupName, subscriptionId` | Update the state of specified commitmentPlans associated with the Cognitive Services account. |
| `CommitmentPlans_Delete` | `DELETE` | `accountName, commitmentPlanName, resourceGroupName, subscriptionId` | Deletes the specified commitmentPlan associated with the Cognitive Services account. |
