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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.accounts_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Deployment model name. |
| <CopyableCode code="baseModel" /> | `object` | Properties of Cognitive Services account deployment model. |
| <CopyableCode code="callRateLimit" /> | `object` | The call rate limit Cognitive Services account. |
| <CopyableCode code="capabilities" /> | `object` | The capabilities. |
| <CopyableCode code="deprecation" /> | `object` | Cognitive Services account ModelDeprecationInfo. |
| <CopyableCode code="finetuneCapabilities" /> | `object` | The capabilities for finetune models. |
| <CopyableCode code="format" /> | `string` | Deployment model format. |
| <CopyableCode code="isDefaultVersion" /> | `boolean` | If the model is default version. |
| <CopyableCode code="lifecycleStatus" /> | `string` | Model lifecycle status. |
| <CopyableCode code="maxCapacity" /> | `integer` | The max capacity. |
| <CopyableCode code="skus" /> | `array` | The list of Model Sku. |
| <CopyableCode code="source" /> | `string` | Optional. Deployment model source ARM resource ID. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="version" /> | `string` | Optional. Deployment model version. If version is not specified, a default version will be assigned. The default version is different for different models and might change when there is new version available for a model. Default version for a model could be found from list models API. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> |
