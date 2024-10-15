---
title: recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_actions
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>recommended_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.recommended_actions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommended_actions', value: 'view', },
        { label: 'recommended_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="action_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="advisorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="advisor_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendedActionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a recommendation action. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advisorName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> | Retrieve recommended actions from the advisor. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="advisorName, resourceGroupName, serverName, subscriptionId" /> | Retrieve recommended actions from the advisor. |

## `SELECT` examples

Retrieve recommended actions from the advisor.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommended_actions', value: 'view', },
        { label: 'recommended_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
action_id,
advisorName,
advisor_name,
created_time,
details,
expiration_time,
reason,
recommendation_type,
recommendedActionName,
resourceGroupName,
serverName,
session_id,
subscriptionId
FROM azure.maria_db.vw_recommended_actions
WHERE advisorName = '{{ advisorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.maria_db.recommended_actions
WHERE advisorName = '{{ advisorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

