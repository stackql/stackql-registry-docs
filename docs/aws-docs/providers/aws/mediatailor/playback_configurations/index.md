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
    <td><CopyableCode code="Name, VideoContentSourceUrl, AdDecisionServerUrl, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>playback_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediatailor.playback_configurations (
 AdDecisionServerUrl,
 Name,
 VideoContentSourceUrl,
 region
)
SELECT 
'{{ AdDecisionServerUrl }}',
 '{{ Name }}',
 '{{ VideoContentSourceUrl }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AdDecisionServerUrl }}',
 '{{ AvailSuppression }}',
 '{{ Bumper }}',
 '{{ CdnConfiguration }}',
 '{{ ConfigurationAliases }}',
 '{{ DashConfiguration }}',
 '{{ LivePreRollConfiguration }}',
 '{{ ManifestProcessingRules }}',
 '{{ Name }}',
 '{{ PersonalizationThresholdSeconds }}',
 '{{ HlsConfiguration }}',
 '{{ SlateAdUrl }}',
 '{{ Tags }}',
 '{{ TranscodeProfileName }}',
 '{{ VideoContentSourceUrl }}',
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
  - name: playback_configuration
    props:
      - name: AdDecisionServerUrl
        value: '{{ AdDecisionServerUrl }}'
      - name: AvailSuppression
        value:
          Mode: '{{ Mode }}'
          Value: '{{ Value }}'
      - name: Bumper
        value:
          StartUrl: '{{ StartUrl }}'
          EndUrl: '{{ EndUrl }}'
      - name: CdnConfiguration
        value:
          AdSegmentUrlPrefix: '{{ AdSegmentUrlPrefix }}'
          ContentSegmentUrlPrefix: '{{ ContentSegmentUrlPrefix }}'
      - name: ConfigurationAliases
        value: null
      - name: DashConfiguration
        value:
          MpdLocation: '{{ MpdLocation }}'
          OriginManifestType: '{{ OriginManifestType }}'
          ManifestEndpointPrefix: '{{ ManifestEndpointPrefix }}'
      - name: LivePreRollConfiguration
        value:
          AdDecisionServerUrl: '{{ AdDecisionServerUrl }}'
          MaxDurationSeconds: '{{ MaxDurationSeconds }}'
      - name: ManifestProcessingRules
        value:
          AdMarkerPassthrough:
            Enabled: '{{ Enabled }}'
      - name: Name
        value: '{{ Name }}'
      - name: PersonalizationThresholdSeconds
        value: '{{ PersonalizationThresholdSeconds }}'
      - name: HlsConfiguration
        value:
          ManifestEndpointPrefix: '{{ ManifestEndpointPrefix }}'
      - name: SlateAdUrl
        value: '{{ SlateAdUrl }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TranscodeProfileName
        value: '{{ TranscodeProfileName }}'
      - name: VideoContentSourceUrl
        value: '{{ VideoContentSourceUrl }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

