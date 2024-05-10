---
title: quick_connects
hide_title: false
hide_table_of_contents: false
keywords:
  - quick_connects
  - connect
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


Used to retrieve a list of <code>quick_connects</code> in a region or to create or delete a <code>quick_connects</code> resource, use <code>quick_connect</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quick_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::QuickConnect</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.quick_connects" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="quick_connect_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the quick connect.</td></tr>
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
quick_connect_arn
FROM aws.connect.quick_connects
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>quick_connect</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- quick_connect.iql (required properties only)
INSERT INTO aws.connect.quick_connects (
 InstanceArn,
 Name,
 QuickConnectConfig,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ QuickConnectConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- quick_connect.iql (all properties)
INSERT INTO aws.connect.quick_connects (
 InstanceArn,
 Name,
 Description,
 QuickConnectConfig,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ QuickConnectConfig }}',
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
  - name: quick_connect
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: QuickConnectConfig
        value:
          QuickConnectType: '{{ QuickConnectType }}'
          PhoneConfig:
            PhoneNumber: '{{ PhoneNumber }}'
          QueueConfig:
            ContactFlowArn: '{{ ContactFlowArn }}'
            QueueArn: '{{ QueueArn }}'
          UserConfig:
            ContactFlowArn: null
            UserArn: '{{ UserArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.quick_connects
WHERE data__Identifier = '<QuickConnectArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>quick_connects</code> resource, the following permissions are required:

### Create
```json
connect:CreateQuickConnect,
connect:TagResource
```

### Delete
```json
connect:DeleteQuickConnect,
connect:UntagResource
```

### List
```json
connect:ListQuickConnects
```

