---
title: sql_pool_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_usages
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the usage metric. |
| <CopyableCode code="currentValue" /> | `number` | The current value of the usage metric. |
| <CopyableCode code="displayName" /> | `string` | The usage metric display name. |
| <CopyableCode code="limit" /> | `number` | The current limit of the usage metric. |
| <CopyableCode code="nextResetTime" /> | `string` | The next reset time for the usage metric (ISO8601 format). |
| <CopyableCode code="resourceName" /> | `string` | The name of the resource. |
| <CopyableCode code="unit" /> | `string` | The units of the usage metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets SQL pool usages. |

## `SELECT` examples

Gets SQL pool usages.


```sql
SELECT
name,
currentValue,
displayName,
limit,
nextResetTime,
resourceName,
unit
FROM azure.synapse.sql_pool_usages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```