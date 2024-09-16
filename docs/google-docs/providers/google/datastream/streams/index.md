---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - datastream
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

Creates, updates, deletes, gets or lists a <code>streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The stream's name. |
| <CopyableCode code="backfillAll" /> | `object` | Backfill strategy to automatically backfill the Stream's objects. Specific objects can be excluded. |
| <CopyableCode code="backfillNone" /> | `object` | Backfill strategy to disable automatic backfill for the Stream's objects. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the stream. |
| <CopyableCode code="customerManagedEncryptionKey" /> | `string` | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |
| <CopyableCode code="destinationConfig" /> | `object` | The configuration of the stream destination. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="errors" /> | `array` | Output only. Errors on the Stream. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="lastRecoveryTime" /> | `string` | Output only. If the stream was recovered, the time of the last recovery. Note: This field is currently experimental. |
| <CopyableCode code="sourceConfig" /> | `object` | The configuration of the stream source. |
| <CopyableCode code="state" /> | `string` | The state of the stream. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time of the stream. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to get details about a stream. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list streams in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to create a stream. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to delete a stream. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to update the configuration of a stream. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to start, resume or recover a stream with a non default CDC strategy. |

## `SELECT` examples

Use this method to list streams in a project and location.

```sql
SELECT
name,
backfillAll,
backfillNone,
createTime,
customerManagedEncryptionKey,
destinationConfig,
displayName,
errors,
labels,
lastRecoveryTime,
sourceConfig,
state,
updateTime
FROM google.datastream.streams
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streams</code> resource.

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
INSERT INTO google.datastream.streams (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
displayName,
sourceConfig,
destinationConfig,
state,
backfillAll,
backfillNone,
errors,
customerManagedEncryptionKey,
lastRecoveryTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ displayName }}',
'{{ sourceConfig }}',
'{{ destinationConfig }}',
'{{ state }}',
'{{ backfillAll }}',
'{{ backfillNone }}',
'{{ errors }}',
'{{ customerManagedEncryptionKey }}',
'{{ lastRecoveryTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: sourceConfig
      value: '{{ sourceConfig }}'
    - name: destinationConfig
      value: '{{ destinationConfig }}'
    - name: state
      value: '{{ state }}'
    - name: backfillAll
      value: '{{ backfillAll }}'
    - name: backfillNone
      value: '{{ backfillNone }}'
    - name: errors
      value: '{{ errors }}'
    - name: customerManagedEncryptionKey
      value: '{{ customerManagedEncryptionKey }}'
    - name: lastRecoveryTime
      value: '{{ lastRecoveryTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>streams</code> resource.

```sql
/*+ update */
UPDATE google.datastream.streams
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
sourceConfig = '{{ sourceConfig }}',
destinationConfig = '{{ destinationConfig }}',
state = '{{ state }}',
backfillAll = '{{ backfillAll }}',
backfillNone = '{{ backfillNone }}',
errors = '{{ errors }}',
customerManagedEncryptionKey = '{{ customerManagedEncryptionKey }}',
lastRecoveryTime = '{{ lastRecoveryTime }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND streamsId = '{{ streamsId }}';
```

## `DELETE` example

Deletes the specified <code>streams</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastream.streams
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND streamsId = '{{ streamsId }}';
```
