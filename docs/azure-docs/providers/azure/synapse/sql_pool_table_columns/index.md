---
title: sql_pool_table_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_table_columns
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

Creates, updates, deletes, gets or lists a <code>sql_pool_table_columns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_table_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_table_columns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Sql pool column properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_table_name" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Gets columns in a given table in a SQL pool. |

## `SELECT` examples

Gets columns in a given table in a SQL pool.


```sql
SELECT
properties
FROM azure.synapse.sql_pool_table_columns
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```