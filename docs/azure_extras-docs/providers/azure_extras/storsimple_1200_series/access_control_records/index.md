---
title: access_control_records
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_records
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>access_control_records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_control_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.access_control_records" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_control_records', value: 'view', },
        { label: 'access_control_records', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="accessControlRecordName" /> | `text` | field from the `properties` object |
| <CopyableCode code="initiator_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Properties of access control record |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified access control record name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the access control records in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or Updates an access control record. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId" /> | Deletes the access control record. |

## `SELECT` examples

Retrieves all the access control records in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_control_records', value: 'view', },
        { label: 'access_control_records', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accessControlRecordName,
initiator_name,
managerName,
resourceGroupName,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_access_control_records
WHERE managerName = '{{ managerName }}'
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
FROM azure_extras.storsimple_1200_series.access_control_records
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_control_records</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.access_control_records (
accessControlRecordName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accessControlRecordName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: initiatorName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>access_control_records</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.access_control_records
WHERE accessControlRecordName = '{{ accessControlRecordName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
