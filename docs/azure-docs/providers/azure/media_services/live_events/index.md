---
title: live_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events
  - media_services
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

Creates, updates, deletes, gets or lists a <code>live_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_events" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_events', value: 'view', },
        { label: 'live_events', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="cross_site_access_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="encoding" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="input" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="liveEventName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="preview" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="stream_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="transcriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_static_hostname" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The live event properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Gets properties of a live event. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all the live events in the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Creates a new live event. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Deletes a live event. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Updates settings on an existing live event. |
| <CopyableCode code="allocate" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | A live event is in StandBy state after allocation completes, and is ready to start. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, operationId, resourceGroupName, subscriptionId" /> | Get a live event operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, operationId, resourceGroupName, subscriptionId" /> | Get a live event operation status. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Resets an existing live event. All live outputs for the live event are deleted and the live event is stopped and will be started again. All assets used by the live outputs and streaming locators created on these assets are unaffected.  |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | A live event in Stopped or StandBy state will be in Running state after the start operation completes. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Stops a running live event. |

## `SELECT` examples

Lists all the live events in the account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_events', value: 'view', },
        { label: 'live_events', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
created,
cross_site_access_policies,
encoding,
hostname_prefix,
input,
last_modified,
liveEventName,
location,
preview,
provisioning_state,
resourceGroupName,
resource_state,
stream_options,
subscriptionId,
system_data,
tags,
transcriptions,
use_static_hostname
FROM azure.media_services.vw_live_events
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.media_services.live_events
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>live_events</code> resource.

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
INSERT INTO azure.media_services.live_events (
accountName,
liveEventName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ accountName }}',
'{{ liveEventName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: input
          value:
            - name: streamingProtocol
              value: string
            - name: accessControl
              value:
                - name: ip
                  value:
                    - name: allow
                      value:
                        - - name: name
                            value: string
                          - name: address
                            value: string
                          - name: subnetPrefixLength
                            value: integer
            - name: keyFrameIntervalDuration
              value: string
            - name: accessToken
              value: string
            - name: endpoints
              value:
                - - name: protocol
                    value: string
                  - name: url
                    value: string
            - name: timedMetadataEndpoints
              value:
                - - name: url
                    value: string
        - name: preview
          value:
            - name: endpoints
              value:
                - - name: protocol
                    value: string
                  - name: url
                    value: string
            - name: accessControl
              value: []
            - name: previewLocator
              value: string
            - name: streamingPolicyName
              value: string
            - name: alternativeMediaId
              value: string
        - name: encoding
          value:
            - name: encodingType
              value: string
            - name: presetName
              value: string
            - name: stretchMode
              value: string
            - name: keyFrameInterval
              value: string
        - name: transcriptions
          value:
            - - name: language
                value: string
              - name: inputTrackSelection
                value:
                  - - name: property
                      value: string
                    - name: operation
                      value: string
                    - name: value
                      value: string
              - name: outputTranscriptionTrack
                value:
                  - name: trackName
                    value: string
        - name: provisioningState
          value: string
        - name: resourceState
          value: string
        - name: crossSiteAccessPolicies
          value:
            - name: clientAccessPolicy
              value: string
            - name: crossDomainPolicy
              value: string
        - name: useStaticHostname
          value: boolean
        - name: hostnamePrefix
          value: string
        - name: streamOptions
          value:
            - string
        - name: created
          value: string
        - name: lastModified
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>live_events</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.live_events
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>live_events</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.live_events
WHERE accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
