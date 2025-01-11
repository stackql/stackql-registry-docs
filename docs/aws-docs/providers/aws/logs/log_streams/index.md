---
title: log_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - log_streams
  - logs
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

Creates, updates, deletes or gets a <code>log_stream</code> resource or lists <code>log_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Logs::LogStream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.log_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="log_stream_name" /></td><td><code>string</code></td><td>The name of the log stream. The name must be unique wihtin the log group.</td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of the log group where the log stream is created.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html"><code>AWS::Logs::LogStream</code></a>.

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
    <td><CopyableCode code="LogGroupName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>log_streams</code> in a region.
```sql
SELECT
region,
log_stream_name,
log_group_name
FROM aws.logs.log_streams
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>log_stream</code>.
```sql
SELECT
region,
log_stream_name,
log_group_name
FROM aws.logs.log_streams
WHERE region = 'us-east-1' AND data__Identifier = '<LogGroupName>|<LogStreamName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.log_streams (
 LogGroupName,
 region
)
SELECT 
'{{ LogGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.log_streams (
 LogStreamName,
 LogGroupName,
 region
)
SELECT 
 '{{ LogStreamName }}',
 '{{ LogGroupName }}',
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
  - name: log_stream
    props:
      - name: LogStreamName
        value: '{{ LogStreamName }}'
      - name: LogGroupName
        value: '{{ LogGroupName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.log_streams
WHERE data__Identifier = '<LogGroupName|LogStreamName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>log_streams</code> resource, the following permissions are required:

### Read
```json
logs:DescribeLogStreams
```

### Create
```json
logs:CreateLogStream,
logs:DescribeLogStreams
```

### List
```json
logs:DescribeLogStreams
```

### Delete
```json
logs:DeleteLogStream
```
