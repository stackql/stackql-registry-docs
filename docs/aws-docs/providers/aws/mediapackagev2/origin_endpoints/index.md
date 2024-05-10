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


Used to retrieve a list of <code>origin_endpoints</code> in a region or to create or delete a <code>origin_endpoints</code> resource, use <code>origin_endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.mediapackagev2.origin_endpoints
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>origin_endpoint</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- origin_endpoint.iql (required properties only)
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
-- origin_endpoint.iql (all properties)
INSERT INTO aws.mediapackagev2.origin_endpoints (
 ChannelGroupName,
 ChannelName,
 ContainerType,
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
            FilterConfiguration:
              ManifestFilter: '{{ ManifestFilter }}'
              Start: '{{ Start }}'
              End: '{{ End }}'
              TimeDelaySeconds: '{{ TimeDelaySeconds }}'
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

## `DELETE` Example

```sql
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

### Delete
```json
mediapackagev2:GetOriginEndpoint,
mediapackagev2:DeleteOriginEndpoint
```

### List
```json
mediapackagev2:ListOriginEndpoints
```

