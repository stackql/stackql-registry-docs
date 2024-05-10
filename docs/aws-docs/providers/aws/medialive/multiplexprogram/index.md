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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>multiplexprogram</code> resource, use <code>multiplexprograms</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexprogram</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplexprogram</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplexprogram" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="channel_id" /></td><td><code>string</code></td><td>The MediaLive channel associated with the program.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.medialive.multiplexprogram
WHERE region = 'us-east-1' AND data__Identifier = '<ProgramName>|<MultiplexId>';
```


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

