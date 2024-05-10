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


Used to retrieve a list of <code>log_streams</code> in a region or to create or delete a <code>log_streams</code> resource, use <code>log_stream</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Logs::LogStream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.log_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of the log group where the log stream is created.</td></tr>
<tr><td><CopyableCode code="log_stream_name" /></td><td><code>string</code></td><td>The name of the log stream. The name must be unique wihtin the log group.</td></tr>
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
log_group_name,
log_stream_name
FROM aws.logs.log_streams
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>log_stream</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- log_stream.iql (required properties only)
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
-- log_stream.iql (all properties)
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

## `DELETE` Example

```sql
DELETE FROM aws.logs.log_streams
WHERE data__Identifier = '<LogGroupName|LogStreamName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>log_streams</code> resource, the following permissions are required:

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

