---
title: sql_pool_replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_replication_links
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

Creates, updates, deletes, gets or lists a <code>sql_pool_replication_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_replication_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_replication_links', value: 'view', },
        { label: 'sql_pool_replication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="is_termination_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkId" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the workspace that contains this firewall rule. |
| <CopyableCode code="partner_database" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource this is. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Location of the workspace that contains this firewall rule. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a Sql pool replication link. |
| <CopyableCode code="type" /> | `string` | Type of resource this is. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_name" /> | `SELECT` | <CopyableCode code="linkId, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool replication link by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Lists a Sql pool's replication links. |

## `SELECT` examples

Lists a Sql pool's replication links.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_replication_links', value: 'view', },
        { label: 'sql_pool_replication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
is_termination_allowed,
linkId,
location,
partner_database,
partner_location,
partner_role,
partner_server,
percent_complete,
replication_mode,
replication_state,
resourceGroupName,
role,
sqlPoolName,
start_time,
subscriptionId,
type,
workspaceName
FROM azure.synapse.vw_sql_pool_replication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
type
FROM azure.synapse.sql_pool_replication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

