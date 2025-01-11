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

Creates, updates, deletes or gets a <code>quick_connect</code> resource or lists <code>quick_connects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quick_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::QuickConnect</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.quick_connects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the quick connect.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the quick connect.</td></tr>
<tr><td><CopyableCode code="quick_connect_config" /></td><td><code>object</code></td><td>Configuration settings for the quick connect.</td></tr>
<tr><td><CopyableCode code="quick_connect_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the quick connect.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="quick_connect_type" /></td><td><code>string</code></td><td>The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html"><code>AWS::Connect::QuickConnect</code></a>.

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
    <td><CopyableCode code="Name, InstanceArn, QuickConnectConfig, region" /></td>
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
Gets all <code>quick_connects</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
quick_connect_config,
quick_connect_arn,
tags,
quick_connect_type
FROM aws.connect.quick_connects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>quick_connect</code>.
```sql
SELECT
region,
instance_arn,
name,
description,
quick_connect_config,
quick_connect_arn,
tags,
quick_connect_type
FROM aws.connect.quick_connects
WHERE region = 'us-east-1' AND data__Identifier = '<QuickConnectArn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
connect:DescribeQuickConnect
```

### Delete
```json
connect:DeleteQuickConnect,
connect:UntagResource
```

### Update
```json
connect:UpdateQuickConnectName,
connect:UpdateQuickConnectConfig,
connect:TagResource,
connect:UntagResource
```

### List
```json
connect:ListQuickConnects
```
