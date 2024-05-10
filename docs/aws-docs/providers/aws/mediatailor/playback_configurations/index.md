---
title: playback_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_configurations
  - mediatailor
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


Used to retrieve a list of <code>playback_configurations</code> in a region or to create or delete a <code>playback_configurations</code> resource, use <code>playback_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaTailor::PlaybackConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.playback_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The identifier for the playback configuration.</td></tr>
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
name
FROM aws.mediatailor.playback_configurations
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
 "AdDecisionServerUrl": "{{ AdDecisionServerUrl }}",
 "Name": "{{ Name }}",
 "VideoContentSourceUrl": "{{ VideoContentSourceUrl }}"
}
>>>
--required properties only
INSERT INTO aws.mediatailor.playback_configurations (
 AdDecisionServerUrl,
 Name,
 VideoContentSourceUrl,
 region
)
SELECT 
{{ AdDecisionServerUrl }},
 {{ Name }},
 {{ VideoContentSourceUrl }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AdDecisionServerUrl": "{{ AdDecisionServerUrl }}",
 "AvailSuppression": {
  "Mode": "{{ Mode }}",
  "Value": "{{ Value }}"
 },
 "Bumper": {
  "StartUrl": "{{ StartUrl }}",
  "EndUrl": "{{ EndUrl }}"
 },
 "CdnConfiguration": {
  "AdSegmentUrlPrefix": "{{ AdSegmentUrlPrefix }}",
  "ContentSegmentUrlPrefix": "{{ ContentSegmentUrlPrefix }}"
 },
 "ConfigurationAliases": null,
 "DashConfiguration": {
  "MpdLocation": "{{ MpdLocation }}",
  "OriginManifestType": "{{ OriginManifestType }}",
  "ManifestEndpointPrefix": "{{ ManifestEndpointPrefix }}"
 },
 "LivePreRollConfiguration": {
  "AdDecisionServerUrl": "{{ AdDecisionServerUrl }}",
  "MaxDurationSeconds": "{{ MaxDurationSeconds }}"
 },
 "ManifestProcessingRules": {
  "AdMarkerPassthrough": {
   "Enabled": "{{ Enabled }}"
  }
 },
 "Name": "{{ Name }}",
 "PersonalizationThresholdSeconds": "{{ PersonalizationThresholdSeconds }}",
 "HlsConfiguration": {
  "ManifestEndpointPrefix": "{{ ManifestEndpointPrefix }}"
 },
 "SlateAdUrl": "{{ SlateAdUrl }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TranscodeProfileName": "{{ TranscodeProfileName }}",
 "VideoContentSourceUrl": "{{ VideoContentSourceUrl }}"
}
>>>
--all properties
INSERT INTO aws.mediatailor.playback_configurations (
 AdDecisionServerUrl,
 AvailSuppression,
 Bumper,
 CdnConfiguration,
 ConfigurationAliases,
 DashConfiguration,
 LivePreRollConfiguration,
 ManifestProcessingRules,
 Name,
 PersonalizationThresholdSeconds,
 HlsConfiguration,
 SlateAdUrl,
 Tags,
 TranscodeProfileName,
 VideoContentSourceUrl,
 region
)
SELECT 
 {{ AdDecisionServerUrl }},
 {{ AvailSuppression }},
 {{ Bumper }},
 {{ CdnConfiguration }},
 {{ ConfigurationAliases }},
 {{ DashConfiguration }},
 {{ LivePreRollConfiguration }},
 {{ ManifestProcessingRules }},
 {{ Name }},
 {{ PersonalizationThresholdSeconds }},
 {{ HlsConfiguration }},
 {{ SlateAdUrl }},
 {{ Tags }},
 {{ TranscodeProfileName }},
 {{ VideoContentSourceUrl }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediatailor.playback_configurations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>playback_configurations</code> resource, the following permissions are required:

### Create
```json
mediatailor:PutPlaybackConfiguration,
mediatailor:ConfigureLogsForPlaybackConfiguration,
iam:CreateServiceLinkedRole,
mediatailor:UntagResource,
mediatailor:TagResource
```

### Delete
```json
mediatailor:DeletePlaybackConfiguration
```

### List
```json
mediatailor:ListPlaybackConfigurations
```

