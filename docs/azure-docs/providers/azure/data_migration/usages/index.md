---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID of the quota object |
| <CopyableCode code="name" /> | `object` | The name of the quota |
| <CopyableCode code="currentValue" /> | `number` | The current value of the quota. If null or missing, the current value cannot be determined in the context of the request. |
| <CopyableCode code="limit" /> | `number` | The maximum value of the quota. If null or missing, the quota has no maximum, in which case it merely tracks usage. |
| <CopyableCode code="unit" /> | `string` | The unit for the quota, such as Count, Bytes, BytesPerSecond, etc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | This method returns region-specific quotas and resource usage information for the Azure Database Migration Service (classic). |

## `SELECT` examples

This method returns region-specific quotas and resource usage information for the Azure Database Migration Service (classic).


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.data_migration.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```