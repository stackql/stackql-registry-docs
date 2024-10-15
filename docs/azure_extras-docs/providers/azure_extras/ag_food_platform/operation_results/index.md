---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` | Arm async operation error class.
Ref: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/async-api-reference.md#azure-asyncoperation-resource-format. |
| <CopyableCode code="status" /> | `string` | Status of the async operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locations, operationResultsId, subscriptionId" /> | Get operationResults for a Data Manager For Agriculture resource. |

## `SELECT` examples

Get operationResults for a Data Manager For Agriculture resource.


```sql
SELECT
error,
status
FROM azure_extras.ag_food_platform.operation_results
WHERE locations = '{{ locations }}'
AND operationResultsId = '{{ operationResultsId }}'
AND subscriptionId = '{{ subscriptionId }}';
```