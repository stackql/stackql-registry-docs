---
title: customization_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - customization_tasks
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>customization_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customization_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.customization_tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customization_tasks', value: 'view', },
        { label: 'customization_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="inputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="taskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a Task. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId, taskName" /> | Gets a Task from the catalog |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | List Tasks in the catalog. |

## `SELECT` examples

List Tasks in the catalog.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customization_tasks', value: 'view', },
        { label: 'customization_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
catalogName,
devCenterName,
inputs,
resourceGroupName,
subscriptionId,
taskName,
timeout,
validation_status
FROM azure.dev_center.vw_customization_tasks
WHERE catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.dev_center.customization_tasks
WHERE catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

