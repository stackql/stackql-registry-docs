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


Used to retrieve a list of <code>packaging_configurations</code> in a region or to create or delete a <code>packaging_configurations</code> resource, use <code>packaging_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::PackagingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.packaging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr>
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
id
FROM aws.mediapackage.packaging_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Id": "{{ Id }}",
 "PackagingGroupId": "{{ PackagingGroupId }}"
}
>>>
--required properties only
INSERT INTO aws.mediapackage.packaging_configurations (
 Id,
 PackagingGroupId,
 region
)
SELECT 
{{ .Id }},
 {{ .PackagingGroupId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Id": "{{ Id }}",
 "PackagingGroupId": "{{ PackagingGroupId }}",
 "CmafPackage": {
  "Encryption": {
   "SpekeKeyProvider": {
    "EncryptionContractConfiguration": {
     "PresetSpeke20Audio": "{{ PresetSpeke20Audio }}",
     "PresetSpeke20Video": "{{ PresetSpeke20Video }}"
    },
    "RoleArn": "{{ RoleArn }}",
    "SystemIds": [
     "{{ SystemIds[0] }}"
    ],
    "Url": "{{ Url }}"
   }
  },
  "HlsManifests": [
   {
    "AdMarkers": "{{ AdMarkers }}",
    "IncludeIframeOnlyStream": "{{ IncludeIframeOnlyStream }}",
    "ManifestName": "{{ ManifestName }}",
    "ProgramDateTimeIntervalSeconds": "{{ ProgramDateTimeIntervalSeconds }}",
    "RepeatExtXKey": "{{ RepeatExtXKey }}",
    "StreamSelection": {
     "MaxVideoBitsPerSecond": "{{ MaxVideoBitsPerSecond }}",
     "MinVideoBitsPerSecond": "{{ MinVideoBitsPerSecond }}",
     "StreamOrder": "{{ StreamOrder }}"
    }
   }
  ],
  "SegmentDurationSeconds": "{{ SegmentDurationSeconds }}",
  "IncludeEncoderConfigurationInSegments": "{{ IncludeEncoderConfigurationInSegments }}"
 },
 "DashPackage": {
  "DashManifests": [
   {
    "ManifestLayout": "{{ ManifestLayout }}",
    "ManifestName": null,
    "MinBufferTimeSeconds": "{{ MinBufferTimeSeconds }}",
    "Profile": "{{ Profile }}",
    "ScteMarkersSource": "{{ ScteMarkersSource }}",
    "StreamSelection": null
   }
  ],
  "Encryption": {
   "SpekeKeyProvider": null
  },
  "PeriodTriggers": [
   "{{ PeriodTriggers[0] }}"
  ],
  "SegmentDurationSeconds": null,
  "SegmentTemplateFormat": "{{ SegmentTemplateFormat }}",
  "IncludeEncoderConfigurationInSegments": "{{ IncludeEncoderConfigurationInSegments }}",
  "IncludeIframeOnlyStream": "{{ IncludeIframeOnlyStream }}"
 },
 "HlsPackage": {
  "Encryption": {
   "ConstantInitializationVector": "{{ ConstantInitializationVector }}",
   "EncryptionMethod": "{{ EncryptionMethod }}",
   "SpekeKeyProvider": null
  },
  "HlsManifests": [
   null
  ],
  "IncludeDvbSubtitles": "{{ IncludeDvbSubtitles }}",
  "SegmentDurationSeconds": null,
  "UseAudioRenditionGroup": "{{ UseAudioRenditionGroup }}"
 },
 "MssPackage": {
  "Encryption": {
   "SpekeKeyProvider": null
  },
  "MssManifests": [
   {
    "ManifestName": null,
    "StreamSelection": null
   }
  ],
  "SegmentDurationSeconds": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .Id }},
 {{ .PackagingGroupId }},
 {{ .CmafPackage }},
 {{ .DashPackage }},
 {{ .HlsPackage }},
 {{ .MssPackage }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

