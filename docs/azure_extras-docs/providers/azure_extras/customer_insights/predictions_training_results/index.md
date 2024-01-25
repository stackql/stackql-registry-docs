---
title: predictions_training_results
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions_training_results
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>predictions_training_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.predictions_training_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `canonicalProfiles` | `array` | Canonical profiles. |
| `predictionDistribution` | `object` | The definition of the prediction distribution. |
| `primaryProfileInstanceCount` | `integer` | Instance count of the primary profile. |
| `scoreName` | `string` | Score name. |
| `tenantId` | `string` | The hub name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `hubName, predictionName, resourceGroupName, subscriptionId` |
