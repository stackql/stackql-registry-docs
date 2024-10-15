---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.triggers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_triggers', value: 'view', },
        { label: 'triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotations" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Azure data factory nested object which contains information about creating pipeline run |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Gets a trigger. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists triggers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName, data__properties" /> | Creates or updates a trigger. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Deletes a trigger. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Query triggers. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Starts a trigger. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Stops a trigger. |
| <CopyableCode code="subscribe_to_events" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Subscribe event trigger to events. |
| <CopyableCode code="unsubscribe_from_events" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Unsubscribe event trigger from events. |

## `SELECT` examples

Lists triggers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_triggers', value: 'view', },
        { label: 'triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
annotations,
etag,
factoryName,
resourceGroupName,
runtime_state,
subscriptionId,
triggerName,
type
FROM azure.data_factory.vw_triggers
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.data_factory.triggers
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>triggers</code> resource.

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
INSERT INTO azure.data_factory.triggers (
factoryName,
resourceGroupName,
subscriptionId,
triggerName,
data__properties,
properties
)
SELECT 
'{{ factoryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ triggerName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: type
          value: string
        - name: description
          value: string
        - name: runtimeState
          value: []
        - name: annotations
          value:
            - object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>triggers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.triggers
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}';
```
