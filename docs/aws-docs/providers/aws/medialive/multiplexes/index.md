---
title: multiplexes
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplexes
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

Creates, updates, deletes or gets a <code>multiplex</code> resource or lists <code>multiplexes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplex</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplexes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique arn of the multiplex.</td></tr>
<tr><td><CopyableCode code="availability_zones" /></td><td><code>array</code></td><td>A list of availability zones for the multiplex.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>A list of the multiplex output destinations.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
<tr><td><CopyableCode code="multiplex_settings" /></td><td><code>object</code></td><td>Configuration for a multiplex event.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of multiplex.</td></tr>
<tr><td><CopyableCode code="pipelines_running_count" /></td><td><code>integer</code></td><td>The number of currently healthy pipelines.</td></tr>
<tr><td><CopyableCode code="program_count" /></td><td><code>integer</code></td><td>The number of programs in the multiplex.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-multiplex.html"><code>AWS::MediaLive::Multiplex</code></a>.

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
    <td><CopyableCode code="AvailabilityZones, MultiplexSettings, Name, region" /></td>
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
Gets all <code>multiplexes</code> in a region.
```sql
SELECT
region,
arn,
availability_zones,
destinations,
id,
multiplex_settings,
name,
pipelines_running_count,
program_count,
state,
tags
FROM aws.medialive.multiplexes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>multiplex</code>.
```sql
SELECT
region,
arn,
availability_zones,
destinations,
id,
multiplex_settings,
name,
pipelines_running_count,
program_count,
state,
tags
FROM aws.medialive.multiplexes
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>multiplex</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.multiplexes (
 AvailabilityZones,
 MultiplexSettings,
 Name,
 region
)
SELECT 
'{{ AvailabilityZones }}',
 '{{ MultiplexSettings }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.multiplexes (
 AvailabilityZones,
 Destinations,
 MultiplexSettings,
 Name,
 Tags,
 region
)
SELECT 
 '{{ AvailabilityZones }}',
 '{{ Destinations }}',
 '{{ MultiplexSettings }}',
 '{{ Name }}',
 '{{ Tags }}',
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
  - name: multiplex
    props:
      - name: AvailabilityZones
        value:
          - '{{ AvailabilityZones[0] }}'
      - name: Destinations
        value:
          - MultiplexMediaConnectOutputDestinationSettings: null
      - name: MultiplexSettings
        value:
          MaximumVideoBufferDelayMilliseconds: '{{ MaximumVideoBufferDelayMilliseconds }}'
          TransportStreamBitrate: '{{ TransportStreamBitrate }}'
          TransportStreamId: '{{ TransportStreamId }}'
          TransportStreamReservedBitrate: '{{ TransportStreamReservedBitrate }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.medialive.multiplexes
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>multiplexes</code> resource, the following permissions are required:

### Create
```json
medialive:CreateMultiplex,
medialive:DescribeMultiplex,
medialive:CreateTags
```

### Read
```json
medialive:DescribeMultiplex
```

### Update
```json
medialive:UpdateMultiplex,
medialive:DescribeMultiplex,
medialive:CreateTags,
medialive:DeleteTags
```

### Delete
```json
medialive:DeleteMultiplex,
medialive:DescribeMultiplex
```

### List
```json
medialive:ListMultiplexes
```
