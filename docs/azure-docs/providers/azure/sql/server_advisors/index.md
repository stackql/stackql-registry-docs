---
title: server_advisors
hide_title: false
hide_table_of_contents: false
keywords:
  - server_advisors
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

Creates, updates, deletes, gets or lists a <code>server_advisors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_advisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_advisors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_advisors', value: 'view', },
        { label: 'server_advisors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advisorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="advisor_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_execute_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_execute_status_inherited_from" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Resource kind. |
| <CopyableCode code="last_checked" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="recommendations_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommended_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for a Database, Server or Elastic Pool Advisor. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advisorName, resourceGroupName, serverName, subscriptionId" /> | Gets a server advisor. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="advisorName, resourceGroupName, serverName, subscriptionId" /> | Updates a server advisor. |
| <CopyableCode code="list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server advisors. |

## `SELECT` examples

Gets a server advisor.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_advisors', value: 'view', },
        { label: 'server_advisors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
advisorName,
advisor_status,
auto_execute_status,
auto_execute_status_inherited_from,
kind,
last_checked,
location,
recommendations_status,
recommended_actions,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_server_advisors
WHERE advisorName = '{{ advisorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.server_advisors
WHERE advisorName = '{{ advisorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>server_advisors</code> resource.

```sql
/*+ update */
UPDATE azure.sql.server_advisors
SET 
properties = '{{ properties }}'
WHERE 
advisorName = '{{ advisorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
