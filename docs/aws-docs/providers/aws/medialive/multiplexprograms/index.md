---
title: multiplexprograms
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplexprograms
  - medialive
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

Creates, updates, deletes or gets a <code>multiplexprogram</code> resource or lists <code>multiplexprograms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexprograms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplexprogram</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplexprograms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="channel_id" /></td><td><code>string</code></td><td>The MediaLive channel associated with the program.</td></tr>
<tr><td><CopyableCode code="multiplex_id" /></td><td><code>string</code></td><td>The ID of the multiplex that the program belongs to.</td></tr>
<tr><td><CopyableCode code="multiplex_program_settings" /></td><td><code>object</code></td><td>The settings for this multiplex program.</td></tr>
<tr><td><CopyableCode code="preferred_channel_pipeline" /></td><td><code>string</code></td><td>The settings for this multiplex program.</td></tr>
<tr><td><CopyableCode code="packet_identifiers_map" /></td><td><code>object</code></td><td>The packet identifier map for this multiplex program.</td></tr>
<tr><td><CopyableCode code="pipeline_details" /></td><td><code>array</code></td><td>Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time.</td></tr>
<tr><td><CopyableCode code="program_name" /></td><td><code>string</code></td><td>The name of the multiplex program.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>multiplexprograms</code> in a region.
```sql
SELECT
region,
program_name,
multiplex_id
FROM aws.medialive.multiplexprograms
WHERE region = 'us-east-1';
```
Gets all properties from a <code>multiplexprogram</code>.
```sql
SELECT
region,
channel_id,
multiplex_id,
multiplex_program_settings,
preferred_channel_pipeline,
packet_identifiers_map,
pipeline_details,
program_name
FROM aws.medialive.multiplexprograms
WHERE region = 'us-east-1' AND data__Identifier = '<ProgramName>|<MultiplexId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>multiplexprogram</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.multiplexprograms (
 ChannelId,
 MultiplexId,
 MultiplexProgramSettings,
 PreferredChannelPipeline,
 PacketIdentifiersMap,
 PipelineDetails,
 ProgramName,
 region
)
SELECT 
'{{ ChannelId }}',
 '{{ MultiplexId }}',
 '{{ MultiplexProgramSettings }}',
 '{{ PreferredChannelPipeline }}',
 '{{ PacketIdentifiersMap }}',
 '{{ PipelineDetails }}',
 '{{ ProgramName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.multiplexprograms (
 ChannelId,
 MultiplexId,
 MultiplexProgramSettings,
 PreferredChannelPipeline,
 PacketIdentifiersMap,
 PipelineDetails,
 ProgramName,
 region
)
SELECT 
 '{{ ChannelId }}',
 '{{ MultiplexId }}',
 '{{ MultiplexProgramSettings }}',
 '{{ PreferredChannelPipeline }}',
 '{{ PacketIdentifiersMap }}',
 '{{ PipelineDetails }}',
 '{{ ProgramName }}',
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
  - name: multiplexprogram
    props:
      - name: ChannelId
        value: '{{ ChannelId }}'
      - name: MultiplexId
        value: '{{ MultiplexId }}'
      - name: MultiplexProgramSettings
        value:
          PreferredChannelPipeline: '{{ PreferredChannelPipeline }}'
          ProgramNumber: '{{ ProgramNumber }}'
          ServiceDescriptor:
            ProviderName: '{{ ProviderName }}'
            ServiceName: '{{ ServiceName }}'
          VideoSettings: {}
      - name: PreferredChannelPipeline
        value: null
      - name: PacketIdentifiersMap
        value:
          AudioPids:
            - '{{ AudioPids[0] }}'
          DvbSubPids:
            - '{{ DvbSubPids[0] }}'
          DvbTeletextPid: '{{ DvbTeletextPid }}'
          EtvPlatformPid: '{{ EtvPlatformPid }}'
          EtvSignalPid: '{{ EtvSignalPid }}'
          KlvDataPids:
            - '{{ KlvDataPids[0] }}'
          PcrPid: '{{ PcrPid }}'
          PmtPid: '{{ PmtPid }}'
          PrivateMetadataPid: '{{ PrivateMetadataPid }}'
          Scte27Pids:
            - '{{ Scte27Pids[0] }}'
          Scte35Pid: '{{ Scte35Pid }}'
          TimedMetadataPid: '{{ TimedMetadataPid }}'
          VideoPid: '{{ VideoPid }}'
      - name: PipelineDetails
        value:
          - ActiveChannelPipeline: '{{ ActiveChannelPipeline }}'
            PipelineId: '{{ PipelineId }}'
      - name: ProgramName
        value: '{{ ProgramName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.medialive.multiplexprograms
WHERE data__Identifier = '<ProgramName|MultiplexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>multiplexprograms</code> resource, the following permissions are required:

### Create
```json
medialive:CreateMultiplexProgram,
medialive:DescribeMultiplexProgram
```

### Read
```json
medialive:DescribeMultiplexProgram
```

### Update
```json
medialive:UpdateMultiplexProgram,
medialive:DescribeMultiplexProgram
```

### Delete
```json
medialive:DeleteMultiplexProgram,
medialive:DescribeMultiplexProgram
```

### List
```json
medialive:ListMultiplexPrograms
```

