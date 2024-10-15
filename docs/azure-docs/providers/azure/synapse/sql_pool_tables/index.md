---
title: sql_pool_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_tables
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

Creates, updates, deletes, gets or lists a <code>sql_pool_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_tables" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Get Sql pool table |
| <CopyableCode code="list_by_schema" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, sqlPoolName, subscriptionId, workspaceName" /> | Gets tables of a given schema in a SQL pool. |

## `SELECT` examples

Gets tables of a given schema in a SQL pool.


```sql
SELECT

FROM azure.synapse.sql_pool_tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```