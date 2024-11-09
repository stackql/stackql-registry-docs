---
title: bms_prepare_data_move_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - bms_prepare_data_move_operation_results
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>bms_prepare_data_move_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bms_prepare_data_move_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.bms_prepare_data_move_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="objectType" /> | `string` | This property will be used as the discriminator for deciding the specific types in the polymorphic chain of types. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> | Fetches Operation Result for Prepare Data Move |

## `SELECT` examples

Fetches Operation Result for Prepare Data Move


```sql
SELECT
objectType
FROM azure.recovery_services_backup.bms_prepare_data_move_operation_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```