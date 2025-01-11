---
title: origin_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoints
  - mediapackage
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::OriginEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.origin_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The URL of the packaged OriginEndpoint for consumption.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="channel_id" /></td><td><code>string</code></td><td>The ID of the Channel the OriginEndpoint is associated with.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A short text description of the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="whitelist" /></td><td><code>array</code></td><td>A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td>Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="time_delay_seconds" /></td><td><code>integer</code></td><td>Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="manifest_name" /></td><td><code>string</code></td><td>A short string appended to the end of the OriginEndpoint URL.</td></tr>
<tr><td><CopyableCode code="origination" /></td><td><code>string</code></td><td>Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination</td></tr>
<tr><td><CopyableCode code="authorization" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="hls_package" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr>
<tr><td><CopyableCode code="dash_package" /></td><td><code>object</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr>
<tr><td><CopyableCode code="mss_package" /></td><td><code>object</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="cmaf_package" /></td><td><code>object</code></td><td>A CMAF packaging configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html"><code>AWS::MediaPackage::OriginEndpoint</code></a>.

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
    <td><CopyableCode code="Id, ChannelId, region" /></td>
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
url,
id,
channel_id,
description,
whitelist,
startover_window_seconds,
time_delay_seconds,
manifest_name,
origination,
authorization,
hls_package,
dash_package,
mss_package,
cmaf_package,
tags
FROM aws.mediapackage.origin_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>origin_endpoint</code>.
```sql
SELECT
region,
arn,
url,
id,
channel_id,
description,
whitelist,
startover_window_seconds,
time_delay_seconds,
manifest_name,
origination,
authorization,
hls_package,
dash_package,
mss_package,
cmaf_package,
tags
FROM aws.mediapackage.origin_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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
INSERT INTO aws.mediapackage.origin_endpoints (
 Id,
 ChannelId,
 region
)
SELECT 
'{{ Id }}',
 '{{ ChannelId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackage.origin_endpoints (
 Id,
 ChannelId,
 Description,
 Whitelist,
 StartoverWindowSeconds,
 TimeDelaySeconds,
 ManifestName,
 Origination,
 Authorization,
 HlsPackage,
 DashPackage,
 MssPackage,
 CmafPackage,
 Tags,
 region
)
SELECT 
 '{{ Id }}',
 '{{ ChannelId }}',
 '{{ Description }}',
 '{{ Whitelist }}',
 '{{ StartoverWindowSeconds }}',
 '{{ TimeDelaySeconds }}',
 '{{ ManifestName }}',
 '{{ Origination }}',
 '{{ Authorization }}',
 '{{ HlsPackage }}',
 '{{ DashPackage }}',
 '{{ MssPackage }}',
 '{{ CmafPackage }}',
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
      - name: Id
        value: '{{ Id }}'
      - name: ChannelId
        value: '{{ ChannelId }}'
      - name: Description
        value: '{{ Description }}'
      - name: Whitelist
        value:
          - '{{ Whitelist[0] }}'
      - name: StartoverWindowSeconds
        value: '{{ StartoverWindowSeconds }}'
      - name: TimeDelaySeconds
        value: '{{ TimeDelaySeconds }}'
      - name: ManifestName
        value: '{{ ManifestName }}'
      - name: Origination
        value: '{{ Origination }}'
      - name: Authorization
        value:
          CdnIdentifierSecret: '{{ CdnIdentifierSecret }}'
          SecretsRoleArn: '{{ SecretsRoleArn }}'
      - name: HlsPackage
        value:
          Encryption:
            ConstantInitializationVector: '{{ ConstantInitializationVector }}'
            EncryptionMethod: '{{ EncryptionMethod }}'
            SpekeKeyProvider:
              EncryptionContractConfiguration:
                PresetSpeke20Audio: '{{ PresetSpeke20Audio }}'
                PresetSpeke20Video: '{{ PresetSpeke20Video }}'
              RoleArn: '{{ RoleArn }}'
              SystemIds:
                - '{{ SystemIds[0] }}'
              Url: '{{ Url }}'
          HlsManifests:
            - AdMarkers: '{{ AdMarkers }}'
              IncludeIframeOnlyStream: '{{ IncludeIframeOnlyStream }}'
              ManifestName: '{{ ManifestName }}'
              ProgramDateTimeIntervalSeconds: '{{ ProgramDateTimeIntervalSeconds }}'
              RepeatExtXKey: '{{ RepeatExtXKey }}'
              StreamSelection:
                MaxVideoBitsPerSecond: '{{ MaxVideoBitsPerSecond }}'
                MinVideoBitsPerSecond: '{{ MinVideoBitsPerSecond }}'
                StreamOrder: '{{ StreamOrder }}'
          IncludeDvbSubtitles: '{{ IncludeDvbSubtitles }}'
          SegmentDurationSeconds: '{{ SegmentDurationSeconds }}'
          UseAudioRenditionGroup: '{{ UseAudioRenditionGroup }}'
      - name: DashPackage
        value:
          DashManifests:
            - ManifestLayout: '{{ ManifestLayout }}'
              ManifestName: null
              MinBufferTimeSeconds: '{{ MinBufferTimeSeconds }}'
              Profile: '{{ Profile }}'
              ScteMarkersSource: '{{ ScteMarkersSource }}'
              StreamSelection: null
          Encryption:
            SpekeKeyProvider: null
          PeriodTriggers:
            - '{{ PeriodTriggers[0] }}'
          SegmentDurationSeconds: null
          SegmentTemplateFormat: '{{ SegmentTemplateFormat }}'
          IncludeEncoderConfigurationInSegments: '{{ IncludeEncoderConfigurationInSegments }}'
          IncludeIframeOnlyStream: '{{ IncludeIframeOnlyStream }}'
      - name: MssPackage
        value:
          Encryption:
            SpekeKeyProvider: null
          MssManifests:
            - ManifestName: null
              StreamSelection: null
          SegmentDurationSeconds: null
      - name: CmafPackage
        value:
          Encryption:
            SpekeKeyProvider: null
          HlsManifests:
            - null
          SegmentDurationSeconds: null
          IncludeEncoderConfigurationInSegments: '{{ IncludeEncoderConfigurationInSegments }}'
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
DELETE FROM aws.mediapackage.origin_endpoints
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>origin_endpoints</code> resource, the following permissions are required:

### Create
```json
mediapackage:CreateOriginEndpoint,
mediapackage:DescribeOriginEndpoint,
mediapackage:DescribeChannel,
mediapackage:TagResource,
iam:PassRole,
acm:DescribeCertificate
```

### Read
```json
mediapackage:DescribeOriginEndpoint
```

### Update
```json
mediapackage:UpdateOriginEndpoint,
mediapackage:TagResource,
mediapackage:ListTagsForResource,
mediapackage:UntagResource,
mediapackage:DescribeOriginEndpoint,
iam:PassRole
```

### Delete
```json
mediapackage:DeleteOriginEndpoint
```

### List
```json
mediapackage:ListOriginEndpoints
```
