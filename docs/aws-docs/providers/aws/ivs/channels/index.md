---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - ivs
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Channel</td></tr>
<tr><td><CopyableCode code="authorized" /></td><td><code>boolean</code></td><td>Whether the channel is authorized.</td></tr>
<tr><td><CopyableCode code="insecure_ingest" /></td><td><code>boolean</code></td><td>Whether the channel allows insecure ingest.</td></tr>
<tr><td><CopyableCode code="latency_mode" /></td><td><code>string</code></td><td>Channel latency mode.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="playback_url" /></td><td><code>string</code></td><td>Channel Playback URL.</td></tr>
<tr><td><CopyableCode code="ingest_endpoint" /></td><td><code>string</code></td><td>Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.</td></tr>
<tr><td><CopyableCode code="recording_configuration_arn" /></td><td><code>string</code></td><td>Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).</td></tr>
<tr><td><CopyableCode code="preset" /></td><td><code>string</code></td><td>Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>channels</code> in a region.
```sql
SELECT
region,
arn,
name,
authorized,
insecure_ingest,
latency_mode,
type,
tags,
playback_url,
ingest_endpoint,
recording_configuration_arn,
preset
FROM aws.ivs.channels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel</code>.
```sql
SELECT
region,
arn,
name,
authorized,
insecure_ingest,
latency_mode,
type,
tags,
playback_url,
ingest_endpoint,
recording_configuration_arn,
preset
FROM aws.ivs.channels
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.ivs.channels (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ivs.channels (
 Name,
 Authorized,
 InsecureIngest,
 LatencyMode,
 Type,
 Tags,
 RecordingConfigurationArn,
 Preset,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Authorized }}',
 '{{ InsecureIngest }}',
 '{{ LatencyMode }}',
 '{{ Type }}',
 '{{ Tags }}',
 '{{ RecordingConfigurationArn }}',
 '{{ Preset }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: Authorized
        value: '{{ Authorized }}'
      - name: InsecureIngest
        value: '{{ InsecureIngest }}'
      - name: LatencyMode
        value: '{{ LatencyMode }}'
      - name: Type
        value: '{{ Type }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: RecordingConfigurationArn
        value: '{{ RecordingConfigurationArn }}'
      - name: Preset
        value: '{{ Preset }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ivs.channels
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
ivs:CreateChannel,
ivs:TagResource
```

### Read
```json
ivs:GetChannel,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetChannel,
ivs:UpdateChannel,
ivs:TagResource,
ivs:UnTagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteChannel,
ivs:UnTagResource
```

### List
```json
ivs:ListChannels,
ivs:ListTagsForResource
```

