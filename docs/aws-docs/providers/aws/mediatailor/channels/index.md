---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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

Creates, updates, deletes or gets a <code>channel</code> resource or lists <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::Channel Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the channel.</p></td></tr>
<tr><td><CopyableCode code="audiences" /></td><td><code>array</code></td><td><p>The list of audiences defined in channel.</p></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="filler_slate" /></td><td><code><p>Slate VOD source configuration.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code><p>The log configuration for the channel.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td><p>The channel's output properties.</p></td></tr>
<tr><td><CopyableCode code="playback_mode" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the channel.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="time_shift_configuration" /></td><td><code><p>The configuration for time-shifted viewing.</p></code></td><td></td></tr>
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
    <td><CopyableCode code="ChannelName, Outputs, PlaybackMode, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>channels</code> in a region.
```sql
SELECT
region,
channel_name
FROM aws.mediatailor.channels
WHERE region = 'us-east-1';
```
Gets all properties from a <code>channel</code>.
```sql
SELECT
region,
arn,
audiences,
channel_name,
filler_slate,
log_configuration,
outputs,
playback_mode,
tags,
tier,
time_shift_configuration
FROM aws.mediatailor.channels
WHERE region = 'us-east-1' AND data__Identifier = '<ChannelName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediatailor.channels (
 ChannelName,
 Outputs,
 PlaybackMode,
 region
)
SELECT 
'{{ ChannelName }}',
 '{{ Outputs }}',
 '{{ PlaybackMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediatailor.channels (
 Audiences,
 ChannelName,
 FillerSlate,
 LogConfiguration,
 Outputs,
 PlaybackMode,
 Tags,
 Tier,
 TimeShiftConfiguration,
 region
)
SELECT 
 '{{ Audiences }}',
 '{{ ChannelName }}',
 '{{ FillerSlate }}',
 '{{ LogConfiguration }}',
 '{{ Outputs }}',
 '{{ PlaybackMode }}',
 '{{ Tags }}',
 '{{ Tier }}',
 '{{ TimeShiftConfiguration }}',
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
  - name: channel
    props:
      - name: Audiences
        value:
          - '{{ Audiences[0] }}'
      - name: ChannelName
        value: '{{ ChannelName }}'
      - name: FillerSlate
        value:
          SourceLocationName: '{{ SourceLocationName }}'
          VodSourceName: '{{ VodSourceName }}'
      - name: LogConfiguration
        value:
          LogTypes:
            - '{{ LogTypes[0] }}'
      - name: Outputs
        value:
          - DashPlaylistSettings:
              ManifestWindowSeconds: null
              MinBufferTimeSeconds: null
              MinUpdatePeriodSeconds: null
              SuggestedPresentationDelaySeconds: null
            HlsPlaylistSettings:
              ManifestWindowSeconds: null
              AdMarkupType:
                - '{{ AdMarkupType[0] }}'
            ManifestName: '{{ ManifestName }}'
            SourceGroup: '{{ SourceGroup }}'
      - name: PlaybackMode
        value: '{{ PlaybackMode }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Tier
        value: '{{ Tier }}'
      - name: TimeShiftConfiguration
        value:
          MaxTimeDelaySeconds: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediatailor.channels
WHERE data__Identifier = '<ChannelName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateChannel,
mediatailor:TagResource,
mediatailor:ConfigureLogsForChannel,
iam:CreateServiceLinkedRole,
mediatailor:DescribeChannel
```

### Read
```json
mediatailor:DescribeChannel
```

### Update
```json
mediatailor:UpdateChannel,
mediatailor:TagResource,
mediatailor:UntagResource,
iam:CreateServiceLinkedRole,
mediatailor:ConfigureLogsForChannel,
mediatailor:DescribeChannel
```

### Delete
```json
mediatailor:DeleteChannel,
mediatailor:DescribeChannel
```

### List
```json
mediatailor:ListChannels
```

