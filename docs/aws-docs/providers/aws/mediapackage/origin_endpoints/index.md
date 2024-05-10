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


Used to retrieve a list of <code>origin_endpoints</code> in a region or to create or delete a <code>origin_endpoints</code> resource, use <code>origin_endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::OriginEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.origin_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr>
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
FROM aws.mediapackage.origin_endpoints
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
 "ChannelId": "{{ ChannelId }}"
}
>>>
--required properties only
INSERT INTO aws.mediapackage.origin_endpoints (
 Id,
 ChannelId,
 region
)
SELECT 
{{ .Id }},
 {{ .ChannelId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Id": "{{ Id }}",
 "ChannelId": "{{ ChannelId }}",
 "Description": "{{ Description }}",
 "Whitelist": [
  "{{ Whitelist[0] }}"
 ],
 "StartoverWindowSeconds": "{{ StartoverWindowSeconds }}",
 "TimeDelaySeconds": "{{ TimeDelaySeconds }}",
 "ManifestName": "{{ ManifestName }}",
 "Origination": "{{ Origination }}",
 "Authorization": {
  "CdnIdentifierSecret": "{{ CdnIdentifierSecret }}",
  "SecretsRoleArn": "{{ SecretsRoleArn }}"
 },
 "HlsPackage": {
  "Encryption": {
   "ConstantInitializationVector": "{{ ConstantInitializationVector }}",
   "EncryptionMethod": "{{ EncryptionMethod }}",
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
  "IncludeDvbSubtitles": "{{ IncludeDvbSubtitles }}",
  "SegmentDurationSeconds": "{{ SegmentDurationSeconds }}",
  "UseAudioRenditionGroup": "{{ UseAudioRenditionGroup }}"
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
 "CmafPackage": {
  "Encryption": {
   "SpekeKeyProvider": null
  },
  "HlsManifests": [
   null
  ],
  "SegmentDurationSeconds": null,
  "IncludeEncoderConfigurationInSegments": "{{ IncludeEncoderConfigurationInSegments }}"
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
 {{ .Id }},
 {{ .ChannelId }},
 {{ .Description }},
 {{ .Whitelist }},
 {{ .StartoverWindowSeconds }},
 {{ .TimeDelaySeconds }},
 {{ .ManifestName }},
 {{ .Origination }},
 {{ .Authorization }},
 {{ .HlsPackage }},
 {{ .DashPackage }},
 {{ .MssPackage }},
 {{ .CmafPackage }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
mediapackage:DeleteOriginEndpoint
```

### List
```json
mediapackage:ListOriginEndpoints
```

