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

Creates, updates, deletes or gets an <code>event_stream</code> resource or lists <code>event_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Event Stream resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.event_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="event_stream_name" /></td><td><code>string</code></td><td>The name of the event stream.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name</td></tr>
<tr><td><CopyableCode code="event_stream_arn" /></td><td><code>string</code></td><td>A unique identifier for the event stream.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the export was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The operational state of destination stream for export.</td></tr>
<tr><td><CopyableCode code="destination_details" /></td><td><code>object</code></td><td>Details regarding the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html"><code>AWS::CustomerProfiles::EventStream</code></a>.

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
    <td><CopyableCode code="DomainName, EventStreamName, Uri, region" /></td>
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
Gets all <code>event_streams</code> in a region.
```sql
SELECT
region,
domain_name,
event_stream_name,
uri,
event_stream_arn,
tags,
created_at,
state,
destination_details
FROM aws.customerprofiles.event_streams
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>event_stream</code>.
```sql
SELECT
region,
domain_name,
event_stream_name,
uri,
event_stream_arn,
tags,
created_at,
state,
destination_details
FROM aws.customerprofiles.event_streams
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<EventStreamName>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
profile:GetEventStream,
kinesis:DescribeStreamSummary
```

### Update
```json
kinesis:DescribeStreamSummary,
profile:GetEventStream,
profile:UntagResource,
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
