---
title: packaging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_configurations
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

Creates, updates, deletes or gets a <code>packaging_configuration</code> resource or lists <code>packaging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::PackagingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.packaging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="packaging_group_id" /></td><td><code>string</code></td><td>The ID of a PackagingGroup.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="cmaf_package" /></td><td><code>object</code></td><td>A CMAF packaging configuration.</td></tr>
<tr><td><CopyableCode code="dash_package" /></td><td><code>object</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr>
<tr><td><CopyableCode code="hls_package" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr>
<tr><td><CopyableCode code="mss_package" /></td><td><code>object</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="PackagingGroupId, Id, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>packaging_configurations</code> in a region.
```sql
SELECT
region,
id,
packaging_group_id,
arn,
cmaf_package,
dash_package,
hls_package,
mss_package,
tags
FROM aws.mediapackage.packaging_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>packaging_configuration</code>.
```sql
SELECT
region,
id,
packaging_group_id,
arn,
cmaf_package,
dash_package,
hls_package,
mss_package,
tags
FROM aws.mediapackage.packaging_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packaging_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediapackage.packaging_configurations (
 Id,
 PackagingGroupId,
 region
)
SELECT 
'{{ Id }}',
 '{{ PackagingGroupId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackage.packaging_configurations (
 Id,
 PackagingGroupId,
 CmafPackage,
 DashPackage,
 HlsPackage,
 MssPackage,
 Tags,
 region
)
SELECT 
 '{{ Id }}',
 '{{ PackagingGroupId }}',
 '{{ CmafPackage }}',
 '{{ DashPackage }}',
 '{{ HlsPackage }}',
 '{{ MssPackage }}',
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
  - name: packaging_configuration
    props:
      - name: Id
        value: '{{ Id }}'
      - name: PackagingGroupId
        value: '{{ PackagingGroupId }}'
      - name: CmafPackage
        value:
          Encryption:
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
          SegmentDurationSeconds: '{{ SegmentDurationSeconds }}'
          IncludeEncoderConfigurationInSegments: '{{ IncludeEncoderConfigurationInSegments }}'
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
      - name: HlsPackage
        value:
          Encryption:
            ConstantInitializationVector: '{{ ConstantInitializationVector }}'
            EncryptionMethod: '{{ EncryptionMethod }}'
            SpekeKeyProvider: null
          HlsManifests:
            - null
          IncludeDvbSubtitles: '{{ IncludeDvbSubtitles }}'
          SegmentDurationSeconds: null
          UseAudioRenditionGroup: '{{ UseAudioRenditionGroup }}'
      - name: MssPackage
        value:
          Encryption:
            SpekeKeyProvider: null
          MssManifests:
            - ManifestName: null
              StreamSelection: null
          SegmentDurationSeconds: null
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
DELETE FROM aws.mediapackage.packaging_configurations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>packaging_configurations</code> resource, the following permissions are required:

### Create
```json
mediapackage-vod:CreatePackagingConfiguration,
mediapackage-vod:DescribePackagingConfiguration,
mediapackage-vod:TagResource,
iam:PassRole
```

### Read
```json
mediapackage-vod:DescribePackagingConfiguration
```

### Delete
```json
mediapackage-vod:DescribePackagingConfiguration,
mediapackage-vod:DeletePackagingConfiguration
```

### List
```json
mediapackage-vod:ListPackagingConfigurations,
mediapackage-vod:DescribePackagingGroup
```

