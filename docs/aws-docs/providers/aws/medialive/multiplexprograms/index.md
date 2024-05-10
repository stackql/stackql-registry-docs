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


Used to retrieve a list of <code>multiplexprograms</code> in a region or to create or delete a <code>multiplexprograms</code> resource, use <code>multiplexprogram</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexprograms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplexprogram</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplexprograms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="program_name" /></td><td><code>string</code></td><td>The name of the multiplex program.</td></tr>
<tr><td><CopyableCode code="multiplex_id" /></td><td><code>string</code></td><td>The ID of the multiplex that the program belongs to.</td></tr>
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
program_name,
multiplex_id
FROM aws.medialive.multiplexprograms
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
 "ChannelId": "{{ ChannelId }}",
 "MultiplexId": "{{ MultiplexId }}",
 "MultiplexProgramSettings": {
  "PreferredChannelPipeline": "{{ PreferredChannelPipeline }}",
  "ProgramNumber": "{{ ProgramNumber }}",
  "ServiceDescriptor": {
   "ProviderName": "{{ ProviderName }}",
   "ServiceName": "{{ ServiceName }}"
  },
  "VideoSettings": {}
 },
 "PreferredChannelPipeline": null,
 "PacketIdentifiersMap": {
  "AudioPids": [
   "{{ AudioPids[0] }}"
  ],
  "DvbSubPids": [
   "{{ DvbSubPids[0] }}"
  ],
  "DvbTeletextPid": "{{ DvbTeletextPid }}",
  "EtvPlatformPid": "{{ EtvPlatformPid }}",
  "EtvSignalPid": "{{ EtvSignalPid }}",
  "KlvDataPids": [
   "{{ KlvDataPids[0] }}"
  ],
  "PcrPid": "{{ PcrPid }}",
  "PmtPid": "{{ PmtPid }}",
  "PrivateMetadataPid": "{{ PrivateMetadataPid }}",
  "Scte27Pids": [
   "{{ Scte27Pids[0] }}"
  ],
  "Scte35Pid": "{{ Scte35Pid }}",
  "TimedMetadataPid": "{{ TimedMetadataPid }}",
  "VideoPid": "{{ VideoPid }}"
 },
 "PipelineDetails": [
  {
   "ActiveChannelPipeline": "{{ ActiveChannelPipeline }}",
   "PipelineId": "{{ PipelineId }}"
  }
 ],
 "ProgramName": "{{ ProgramName }}"
}
>>>
--required properties only
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
{{ .ChannelId }},
 {{ .MultiplexId }},
 {{ .MultiplexProgramSettings }},
 {{ .PreferredChannelPipeline }},
 {{ .PacketIdentifiersMap }},
 {{ .PipelineDetails }},
 {{ .ProgramName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ChannelId": "{{ ChannelId }}",
 "MultiplexId": "{{ MultiplexId }}",
 "MultiplexProgramSettings": {
  "PreferredChannelPipeline": "{{ PreferredChannelPipeline }}",
  "ProgramNumber": "{{ ProgramNumber }}",
  "ServiceDescriptor": {
   "ProviderName": "{{ ProviderName }}",
   "ServiceName": "{{ ServiceName }}"
  },
  "VideoSettings": {}
 },
 "PreferredChannelPipeline": null,
 "PacketIdentifiersMap": {
  "AudioPids": [
   "{{ AudioPids[0] }}"
  ],
  "DvbSubPids": [
   "{{ DvbSubPids[0] }}"
  ],
  "DvbTeletextPid": "{{ DvbTeletextPid }}",
  "EtvPlatformPid": "{{ EtvPlatformPid }}",
  "EtvSignalPid": "{{ EtvSignalPid }}",
  "KlvDataPids": [
   "{{ KlvDataPids[0] }}"
  ],
  "PcrPid": "{{ PcrPid }}",
  "PmtPid": "{{ PmtPid }}",
  "PrivateMetadataPid": "{{ PrivateMetadataPid }}",
  "Scte27Pids": [
   "{{ Scte27Pids[0] }}"
  ],
  "Scte35Pid": "{{ Scte35Pid }}",
  "TimedMetadataPid": "{{ TimedMetadataPid }}",
  "VideoPid": "{{ VideoPid }}"
 },
 "PipelineDetails": [
  {
   "ActiveChannelPipeline": "{{ ActiveChannelPipeline }}",
   "PipelineId": "{{ PipelineId }}"
  }
 ],
 "ProgramName": "{{ ProgramName }}"
}
>>>
--all properties
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
 {{ .ChannelId }},
 {{ .MultiplexId }},
 {{ .MultiplexProgramSettings }},
 {{ .PreferredChannelPipeline }},
 {{ .PacketIdentifiersMap }},
 {{ .PipelineDetails }},
 {{ .ProgramName }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
medialive:DeleteMultiplexProgram,
medialive:DescribeMultiplexProgram
```

### List
```json
medialive:ListMultiplexPrograms
```

