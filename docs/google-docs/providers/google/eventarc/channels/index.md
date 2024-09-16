---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - eventarc
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

Creates, updates, deletes, gets or lists a <code>channels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.eventarc.channels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the channel. Must be unique within the location on the project and must be in `projects/{project}/locations/{location}/channels/{channel_id}` format. |
| <CopyableCode code="activationToken" /> | `string` | Output only. The activation token for the channel. The token must be used by the provider to register the channel for publishing. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="cryptoKeyName" /> | `string` | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| <CopyableCode code="provider" /> | `string` | The name of the event provider (e.g. Eventarc SaaS partner) associated with the channel. This provider will be granted permissions to publish events to the channel. Format: `projects/{project}/locations/{location}/providers/{provider_id}`. |
| <CopyableCode code="pubsubTopic" /> | `string` | Output only. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{project}/topics/{topic_id}`. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Whether or not this Channel satisfies the requirements of physical zone separation |
| <CopyableCode code="state" /> | `string` | Output only. The state of a Channel. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Get a single Channel. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List channels. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new channel in a particular project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Delete a single channel. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Update a single channel. |

## `SELECT` examples

List channels.

```sql
SELECT
name,
activationToken,
createTime,
cryptoKeyName,
provider,
pubsubTopic,
satisfiesPzs,
state,
uid,
updateTime
FROM google.eventarc.channels
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channels</code> resource.

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
INSERT INTO google.eventarc.channels (
locationsId,
projectsId,
name,
uid,
createTime,
updateTime,
provider,
pubsubTopic,
state,
activationToken,
cryptoKeyName,
satisfiesPzs
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ provider }}',
'{{ pubsubTopic }}',
'{{ state }}',
'{{ activationToken }}',
'{{ cryptoKeyName }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: uid
      value: '{{ uid }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: provider
      value: '{{ provider }}'
    - name: pubsubTopic
      value: '{{ pubsubTopic }}'
    - name: state
      value: '{{ state }}'
    - name: activationToken
      value: '{{ activationToken }}'
    - name: cryptoKeyName
      value: '{{ cryptoKeyName }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>channels</code> resource.

```sql
/*+ update */
UPDATE google.eventarc.channels
SET 
name = '{{ name }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
provider = '{{ provider }}',
pubsubTopic = '{{ pubsubTopic }}',
state = '{{ state }}',
activationToken = '{{ activationToken }}',
cryptoKeyName = '{{ cryptoKeyName }}',
satisfiesPzs = true|false
WHERE 
channelsId = '{{ channelsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>channels</code> resource.

```sql
/*+ delete */
DELETE FROM google.eventarc.channels
WHERE channelsId = '{{ channelsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
