---
title: cluster_links
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_links
  - kafka
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cluster_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.cluster_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_link_id" /> | `string` |  |
| <CopyableCode code="destination_cluster_id" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="link_error" /> | `string` |  |
| <CopyableCode code="link_error_message" /> | `string` |  |
| <CopyableCode code="link_id" /> | `string` |  |
| <CopyableCode code="link_name" /> | `string` |  |
| <CopyableCode code="link_state" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="remote_cluster_id" /> | `string` |  |
| <CopyableCode code="source_cluster_id" /> | `string` |  |
| <CopyableCode code="tasks" /> | `array` |  |
| <CopyableCode code="topic_names" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_link" /> | `SELECT` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead. |
| <CopyableCode code="list_kafka_links" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead. |
| <CopyableCode code="create_kafka_link" /> | `INSERT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Cluster link creation requires source cluster security configurations in the configs JSON section of the data request payload. |
| <CopyableCode code="delete_kafka_link" /> | `DELETE` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead.


```sql
SELECT
cluster_link_id,
destination_cluster_id,
kind,
link_error,
link_error_message,
link_id,
link_name,
link_state,
metadata,
remote_cluster_id,
source_cluster_id,
tasks,
topic_names
FROM confluent.kafka.cluster_links
WHERE cluster_id = '{{ cluster_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_links</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO confluent.kafka.cluster_links (
data__source_cluster_id,
data__destination_cluster_id,
data__remote_cluster_id,
data__cluster_link_id,
data__configs,
cluster_id
)
SELECT 
'{{ source_cluster_id }}',
'{{ destination_cluster_id }}',
'{{ remote_cluster_id }}',
'{{ cluster_link_id }}',
'{{ configs }}',
'{{ cluster_id }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO confluent.kafka.cluster_links (
    cluster_id
    )
    SELECT 
    '{{ cluster_id }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: cluster_links
  props:
    - name: cluster_id
      value: string
    - name: source_cluster_id
      value: string
    - name: destination_cluster_id
      value: string
    - name: remote_cluster_id
      value: string
    - name: cluster_link_id
      value: string
    - name: configs
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cluster_links</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.kafka.cluster_links
WHERE cluster_id = '{{ cluster_id }}'
AND link_name = '{{ link_name }}';
```
