---
title: smart_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - smart_groups
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>smart_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>smart_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.smart_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_smart_groups', value: 'view', },
        { label: 'smart_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="alert_severities" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_states" /> | `text` | field from the `properties` object |
| <CopyableCode code="alerts_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_user_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_conditions" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_services" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="smartGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="smart_group_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties of smart group. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Smart Groups within a specified subscription. |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="smartGroupId, subscriptionId" /> | Get information related to a specific Smart Group. |
| <CopyableCode code="change_state" /> | `EXEC` | <CopyableCode code="newState, smartGroupId, subscriptionId" /> | Change the state of a Smart Group. |

## `SELECT` examples

List all the Smart Groups within a specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_smart_groups', value: 'view', },
        { label: 'smart_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alert_severities,
alert_states,
alerts_count,
last_modified_date_time,
last_modified_user_name,
monitor_conditions,
monitor_services,
next_link,
resource_groups,
resource_types,
resources,
severity,
smartGroupId,
smart_group_state,
start_date_time,
subscriptionId,
type
FROM azure.alerts_management.vw_smart_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.alerts_management.smart_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

