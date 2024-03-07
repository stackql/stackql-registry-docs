---
title: multiplexprogram
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplexprogram
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
Gets an individual <code>multiplexprogram</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexprogram</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multiplexprogram</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.medialive.multiplexprogram</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>channel_id</code></td><td><code>string</code></td><td>The MediaLive channel associated with the program.</td></tr>
<tr><td><code>multiplex_id</code></td><td><code>string</code></td><td>The ID of the multiplex that the program belongs to.</td></tr>
<tr><td><code>multiplex_program_settings</code></td><td><code>object</code></td><td>The settings for this multiplex program.</td></tr>
<tr><td><code>preferred_channel_pipeline</code></td><td><code>string</code></td><td>The settings for this multiplex program.</td></tr>
<tr><td><code>packet_identifiers_map</code></td><td><code>object</code></td><td>The packet identifier map for this multiplex program.</td></tr>
<tr><td><code>pipeline_details</code></td><td><code>array</code></td><td>Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time.</td></tr>
<tr><td><code>program_name</code></td><td><code>string</code></td><td>The name of the multiplex program.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>multiplexprogram</code> resource, the following permissions are required:

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


## Example
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
FROM awscc.medialive.multiplexprogram
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ProgramName&gt;'
AND data__Identifier = '&lt;MultiplexId&gt;'
```
