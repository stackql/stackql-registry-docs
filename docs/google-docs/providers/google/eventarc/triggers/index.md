---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.eventarc.triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the trigger. Must be unique within the location of the project and must be in `projects/{project}/locations/{location}/triggers/{trigger}` format. |
| <CopyableCode code="channel" /> | `string` | Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners. |
| <CopyableCode code="conditions" /> | `object` | Output only. The reason(s) why a trigger is in FAILED state. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="destination" /> | `object` | Represents a target of an invocation over HTTP. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on create requests to ensure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="eventDataContentType" /> | `string` | Optional. EventDataContentType specifies the type of payload in MIME format that is expected from the CloudEvent data field. This is set to `application/json` if the value is not defined. |
| <CopyableCode code="eventFilters" /> | `array` | Required. Unordered list. The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination. |
| <CopyableCode code="labels" /> | `object` | Optional. User labels attached to the triggers that can be used to group resources. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Whether or not this Trigger satisfies the requirements of physical zone separation |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The `iam.serviceAccounts.actAs` permission must be granted on the service account to allow a principal to impersonate the service account. For more information, see the [Roles and permissions](/eventarc/docs/all-roles-permissions) page specific to the trigger destination. |
| <CopyableCode code="transport" /> | `object` | Represents the transport intermediaries created for the trigger to deliver events. |
| <CopyableCode code="uid" /> | `string` | Output only. Server-assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Get a single trigger. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List triggers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new trigger in a particular project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Delete a single trigger. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Update a single trigger. |

## `SELECT` examples

List triggers.

```sql
SELECT
name,
channel,
conditions,
createTime,
destination,
etag,
eventDataContentType,
eventFilters,
labels,
satisfiesPzs,
serviceAccount,
transport,
uid,
updateTime
FROM google.eventarc.triggers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

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
INSERT INTO google.eventarc.triggers (
locationsId,
projectsId,
name,
eventFilters,
serviceAccount,
destination,
transport,
labels,
channel,
eventDataContentType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ eventFilters }}',
'{{ serviceAccount }}',
'{{ destination }}',
'{{ transport }}',
'{{ labels }}',
'{{ channel }}',
'{{ eventDataContentType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: eventFilters
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: serviceAccount
      value: '{{ serviceAccount }}'
    - name: destination
      value:
        - name: cloudRun
          value:
            - name: service
              value: '{{ service }}'
            - name: path
              value: '{{ path }}'
            - name: region
              value: '{{ region }}'
        - name: cloudFunction
          value: '{{ cloudFunction }}'
        - name: gke
          value:
            - name: cluster
              value: '{{ cluster }}'
            - name: location
              value: '{{ location }}'
            - name: namespace
              value: '{{ namespace }}'
            - name: service
              value: '{{ service }}'
            - name: path
              value: '{{ path }}'
        - name: workflow
          value: '{{ workflow }}'
        - name: httpEndpoint
          value:
            - name: uri
              value: '{{ uri }}'
        - name: networkConfig
          value:
            - name: networkAttachment
              value: '{{ networkAttachment }}'
    - name: transport
      value:
        - name: pubsub
          value:
            - name: topic
              value: '{{ topic }}'
    - name: labels
      value: '{{ labels }}'
    - name: channel
      value: '{{ channel }}'
    - name: eventDataContentType
      value: '{{ eventDataContentType }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>triggers</code> resource.

```sql
/*+ update */
UPDATE google.eventarc.triggers
SET 
name = '{{ name }}',
eventFilters = '{{ eventFilters }}',
serviceAccount = '{{ serviceAccount }}',
destination = '{{ destination }}',
transport = '{{ transport }}',
labels = '{{ labels }}',
channel = '{{ channel }}',
eventDataContentType = '{{ eventDataContentType }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND triggersId = '{{ triggersId }}';
```

## `DELETE` example

Deletes the specified <code>triggers</code> resource.

```sql
/*+ delete */
DELETE FROM google.eventarc.triggers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND triggersId = '{{ triggersId }}';
```
