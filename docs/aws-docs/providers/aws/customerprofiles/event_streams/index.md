---
title: event_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - event_streams
  - customerprofiles
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


Used to retrieve a list of <code>event_streams</code> in a region or to create or delete a <code>event_streams</code> resource, use <code>event_stream</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Event Stream resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.event_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="event_stream_name" /></td><td><code>string</code></td><td>The name of the event stream.</td></tr>
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
domain_name,
event_stream_name
FROM aws.customerprofiles.event_streams
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>event_stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- event_stream.iql (required properties only)
INSERT INTO aws.customerprofiles.event_streams (
 DomainName,
 EventStreamName,
 Uri,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ EventStreamName }}',
 '{{ Uri }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- event_stream.iql (all properties)
INSERT INTO aws.customerprofiles.event_streams (
 DomainName,
 EventStreamName,
 Uri,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ EventStreamName }}',
 '{{ Uri }}',
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
  - name: event_stream
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: EventStreamName
        value: '{{ EventStreamName }}'
      - name: Uri
        value: '{{ Uri }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.customerprofiles.event_streams
WHERE data__Identifier = '<DomainName|EventStreamName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_streams</code> resource, the following permissions are required:

### Create
```json
profile:CreateEventStream,
iam:PutRolePolicy,
kinesis:DescribeStreamSummary,
profile:TagResource
```

### Delete
```json
profile:DeleteEventStream,
iam:DeleteRolePolicy
```

### List
```json
profile:ListEventStreams
```

