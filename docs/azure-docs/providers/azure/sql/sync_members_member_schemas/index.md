---
title: sync_members_member_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members_member_schemas
  - sql
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

Creates, updates, deletes, gets or lists a <code>sync_members_member_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_members_member_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_members_member_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="lastUpdateTime" /> | `string` | Last update time of the database schema. |
| <CopyableCode code="tables" /> | `array` | List of tables in the database full schema. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Gets a sync member database schema. |

## `SELECT` examples

Gets a sync member database schema.


```sql
SELECT
lastUpdateTime,
tables
FROM azure.sql.sync_members_member_schemas
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}'
AND syncMemberName = '{{ syncMemberName }}';
```