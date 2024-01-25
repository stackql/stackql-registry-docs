---
title: accounts_models
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_models
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
<tr><td><b>Name</b></td><td><code>accounts_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.accounts_models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Deployment model name. |
| `baseModel` | `object` | Properties of Cognitive Services account deployment model. |
| `callRateLimit` | `object` | The call rate limit Cognitive Services account. |
| `capabilities` | `object` | The capabilities. |
| `deprecation` | `object` | Cognitive Services account ModelDeprecationInfo. |
| `finetuneCapabilities` | `object` | The capabilities for finetune models. |
| `format` | `string` | Deployment model format. |
| `isDefaultVersion` | `boolean` | If the model is default version. |
| `lifecycleStatus` | `string` | Model lifecycle status. |
| `maxCapacity` | `integer` | The max capacity. |
| `skus` | `array` | The list of Model Sku. |
| `source` | `string` | Optional. Deployment model source ARM resource ID. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `version` | `string` | Optional. Deployment model version. If version is not specified, a default version will be assigned. The default version is different for different models and might change when there is new version available for a model. Default version for a model could be found from list models API. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
