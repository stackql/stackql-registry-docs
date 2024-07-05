---
title: origin_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoints
  - mediapackagev2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>origin_endpoint</code> resource or lists <code>origin_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td><p>Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) associated with the resource.</p></td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was created.</p></td></tr>
<tr><td><CopyableCode code="dash_manifests" /></td><td><code>array</code></td><td><p>A DASH manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>Enter any descriptive text that helps you to identify the origin endpoint.</p></td></tr>
<tr><td><CopyableCode code="hls_manifests" /></td><td><code>array</code></td><td><p>An HTTP live streaming (HLS) manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="low_latency_hls_manifests" /></td><td><code>array</code></td><td><p>A low-latency HLS manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was modified.</p></td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>object</code></td><td><p>The segment configuration, including the segment name, duration, and other configuration values.</p></td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td><p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ChannelGroupName, ChannelName, OriginEndpointName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>origin_endpoints</code> in a region.
```sql
SELECT
region,
arn,
channel_group_name,
channel_name,
container_type,
created_at,
dash_manifests,
description,
hls_manifests,
low_latency_hls_manifests,
modified_at,
origin_endpoint_name,
segment,
startover_window_seconds,
tags
FROM aws.mediapackagev2.origin_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>origin_endpoint</code>.
```sql
SELECT
region,
arn,
channel_group_name,
channel_name,
container_type,
created_at,
dash_manifests,
description,
hls_manifests,
low_latency_hls_manifests,
modified_at,
origin_endpoint_name,
segment,
startover_window_seconds,
tags
FROM aws.mediapackagev2.origin_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>origin_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.mediapackagev2.origin_endpoints (
 ChannelGroupName,
 ChannelName,
 OriginEndpointName,
 region
)
SELECT 
'{{ ChannelGroupName }}',
 '{{ ChannelName }}',
 '{{ OriginEndpointName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackagev2.origin_endpoints (
 ChannelGroupName,
 ChannelName,
 ContainerType,
 DashManifests,
 Description,
 HlsManifests,
 LowLatencyHlsManifests,
 OriginEndpointName,
 Segment,
 StartoverWindowSeconds,
 Tags,
 region
)
SELECT 
 '{{ ChannelGroupName }}',
 '{{ ChannelName }}',
 '{{ ContainerType }}',
 '{{ DashManifests }}',
 '{{ Description }}',
 '{{ HlsManifests }}',
 '{{ LowLatencyHlsManifests }}',
 '{{ OriginEndpointName }}',
 '{{ Segment }}',
 '{{ StartoverWindowSeconds }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: origin_endpoint
    props:
      - name: ChannelGroupName
        value: '{{ ChannelGroupName }}'
      - name: ChannelName
        value: '{{ ChannelName }}'
      - name: ContainerType
        value: '{{ ContainerType }}'
      - name: DashManifests
        value:
          - ManifestName: '{{ ManifestName }}'
            ManifestWindowSeconds: '{{ ManifestWindowSeconds }}'
            FilterConfiguration:
              ManifestFilter: '{{ ManifestFilter }}'
              Start: '{{ Start }}'
              End: '{{ End }}'
              TimeDelaySeconds: '{{ TimeDelaySeconds }}'
            MinUpdatePeriodSeconds: '{{ MinUpdatePeriodSeconds }}'
            MinBufferTimeSeconds: '{{ MinBufferTimeSeconds }}'
            SuggestedPresentationDelaySeconds: '{{ SuggestedPresentationDelaySeconds }}'
            SegmentTemplateFormat: '{{ SegmentTemplateFormat }}'
            PeriodTriggers:
              - '{{ PeriodTriggers[0] }}'
            ScteDash:
              AdMarkerDash: '{{ AdMarkerDash }}'
            DrmSignaling: '{{ DrmSignaling }}'
            UtcTiming:
              TimingMode: '{{ TimingMode }}'
              TimingSource: '{{ TimingSource }}'
      - name: Description
        value: '{{ Description }}'
      - name: HlsManifests
        value:
          - ManifestName: '{{ ManifestName }}'
            Url: '{{ Url }}'
            ChildManifestName: '{{ ChildManifestName }}'
            ManifestWindowSeconds: '{{ ManifestWindowSeconds }}'
            ProgramDateTimeIntervalSeconds: '{{ ProgramDateTimeIntervalSeconds }}'
            ScteHls:
              AdMarkerHls: '{{ AdMarkerHls }}'
            FilterConfiguration: null
      - name: LowLatencyHlsManifests
        value:
          - ManifestName: '{{ ManifestName }}'
            Url: '{{ Url }}'
            ChildManifestName: '{{ ChildManifestName }}'
            ManifestWindowSeconds: '{{ ManifestWindowSeconds }}'
            ProgramDateTimeIntervalSeconds: '{{ ProgramDateTimeIntervalSeconds }}'
            ScteHls: null
            FilterConfiguration: null
      - name: OriginEndpointName
        value: '{{ OriginEndpointName }}'
      - name: Segment
        value:
          SegmentDurationSeconds: '{{ SegmentDurationSeconds }}'
          SegmentName: '{{ SegmentName }}'
          TsUseAudioRenditionGroup: '{{ TsUseAudioRenditionGroup }}'
          IncludeIframeOnlyStreams: '{{ IncludeIframeOnlyStreams }}'
          TsIncludeDvbSubtitles: '{{ TsIncludeDvbSubtitles }}'
          Scte:
            ScteFilter:
              - '{{ ScteFilter[0] }}'
          Encryption:
            ConstantInitializationVector: '{{ ConstantInitializationVector }}'
            EncryptionMethod:
              TsEncryptionMethod: '{{ TsEncryptionMethod }}'
              CmafEncryptionMethod: '{{ CmafEncryptionMethod }}'
            KeyRotationIntervalSeconds: '{{ KeyRotationIntervalSeconds }}'
            SpekeKeyProvider:
              EncryptionContractConfiguration:
                PresetSpeke20Audio: '{{ PresetSpeke20Audio }}'
                PresetSpeke20Video: '{{ PresetSpeke20Video }}'
              ResourceId: '{{ ResourceId }}'
              DrmSystems:
                - '{{ DrmSystems[0] }}'
              RoleArn: '{{ RoleArn }}'
              Url: '{{ Url }}'
      - name: StartoverWindowSeconds
        value: '{{ StartoverWindowSeconds }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediapackagev2.origin_endpoints
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>origin_endpoints</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:TagResource,
mediapackagev2:CreateOriginEndpoint,
iam:PassRole
```

### Read
```json
mediapackagev2:GetOriginEndpoint
```

### Update
```json
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateOriginEndpoint,
iam:PassRole
```

### Delete
```json
mediapackagev2:GetOriginEndpoint,
mediapackagev2:DeleteOriginEndpoint
```

### List
```json
mediapackagev2:ListOriginEndpoints
```

