---
title: database_accounts_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_usages
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>database_accounts_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_accounts_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_accounts_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="currentValue" /> | `integer` | Current value for this metric |
| <CopyableCode code="limit" /> | `integer` | Maximum value for this metric |
| <CopyableCode code="quotaPeriod" /> | `string` | The quota period used to summarize the usage values. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the usages (most recent data) for the given database account. |

## `SELECT` examples

Retrieves the usages (most recent data) for the given database account.


```sql
SELECT
name,
currentValue,
limit,
quotaPeriod,
unit
FROM azure.cosmos_db.database_accounts_usages
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```