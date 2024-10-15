---
title: monitored_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_subscriptions
  - datadog
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

Creates, updates, deletes, gets or lists a <code>monitored_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitored_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitored_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitored_subscriptions', value: 'view', },
        { label: 'monitored_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The id of the monitored subscription resource. |
| <CopyableCode code="name" /> | `text` | Name of the monitored subscription resource. |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitored_subscription_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the monitored subscription resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the monitored subscription resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitored subscription resource. |
| <CopyableCode code="properties" /> | `object` | The request to update subscriptions needed to be monitored by the Datadog monitor resource. |
| <CopyableCode code="type" /> | `string` | The type of the monitored subscription resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="createor_update" /> | `EXEC` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitored_subscriptions', value: 'view', },
        { label: 'monitored_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configurationName,
monitorName,
monitored_subscription_list,
operation,
resourceGroupName,
subscriptionId,
type
FROM azure_isv.datadog.vw_monitored_subscriptions
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_isv.datadog.monitored_subscriptions
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>monitored_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure_isv.datadog.monitored_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
configurationName = '{{ configurationName }}'
AND monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>monitored_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.datadog.monitored_subscriptions
WHERE configurationName = '{{ configurationName }}'
AND monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
