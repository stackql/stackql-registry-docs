---
title: endpoint_models
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_models
  - ml_services
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>endpoint_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.endpoint_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Deployment model name. |
| <CopyableCode code="capabilities" /> | `object` | The capabilities. |
| <CopyableCode code="deprecation" /> | `object` |  |
| <CopyableCode code="finetuneCapabilities" /> | `object` | The capabilities for finetune models. |
| <CopyableCode code="format" /> | `string` | Deployment model format. |
| <CopyableCode code="isDefaultVersion" /> | `boolean` | If the model is default version. |
| <CopyableCode code="lifecycleStatus" /> | `string` | Model lifecycle status. |
| <CopyableCode code="maxCapacity" /> | `integer` | The max capacity. |
| <CopyableCode code="skus" /> | `array` | The list of Model Sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="version" /> | `string` | Optional. Deployment model version. If version is not specified, a default version will be assigned. The default version is different for different models and might change when there is new version available for a model. Default version for a model could be found from list models API. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples




```sql
SELECT
name,
capabilities,
deprecation,
finetuneCapabilities,
format,
isDefaultVersion,
lifecycleStatus,
maxCapacity,
skus,
systemData,
version
FROM azure.ml_services.endpoint_models
WHERE endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```