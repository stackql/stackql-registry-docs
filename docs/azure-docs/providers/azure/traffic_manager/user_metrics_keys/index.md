---
title: user_metrics_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - user_metrics_keys
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>user_metrics_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_metrics_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.user_metrics_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_metrics_keys', value: 'view', },
        { label: 'user_metrics_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class representing a Traffic Manager Real User Metrics key response. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the subscription-level key used for Real User Metrics collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Create or update a subscription-level key used for Real User Metrics collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId" /> | Delete a subscription-level key used for Real User Metrics collection. |

## `SELECT` examples

Get the subscription-level key used for Real User Metrics collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_metrics_keys', value: 'view', },
        { label: 'user_metrics_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
key,
subscriptionId
FROM azure.traffic_manager.vw_user_metrics_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.traffic_manager.user_metrics_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_metrics_keys</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.traffic_manager.user_metrics_keys (
subscriptionId
)
SELECT 
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>user_metrics_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.traffic_manager.user_metrics_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```
