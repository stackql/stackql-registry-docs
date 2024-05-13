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


Used to retrieve a list of <code>multiplexes</code> in a region or to create or delete a <code>multiplexes</code> resource, use <code>multiplex</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplex</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplexes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
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
    <td><CopyableCode code="AvailabilityZones, MultiplexSettings, Name, region" /></td>
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
FROM aws.medialive.multiplexes
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
medialive:DeleteMultiplex,
medialive:DescribeMultiplex
```

### List
```json
medialive:ListMultiplexes
```

