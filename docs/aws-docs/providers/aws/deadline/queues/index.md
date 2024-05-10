---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
  - deadline
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


Used to retrieve a list of <code>queues</code> in a region or to create or delete a <code>queues</code> resource, use <code>queue</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Queue Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.deadline.queues
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>queue</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- queue.iql (required properties only)
INSERT INTO aws.deadline.queues (
 DisplayName,
 region
)
SELECT 
'{{ DisplayName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- queue.iql (all properties)
INSERT INTO aws.deadline.queues (
 AllowedStorageProfileIds,
 DefaultBudgetAction,
 Description,
 DisplayName,
 FarmId,
 JobAttachmentSettings,
 JobRunAsUser,
 RequiredFileSystemLocationNames,
 RoleArn,
 region
)
SELECT 
 '{{ AllowedStorageProfileIds }}',
 '{{ DefaultBudgetAction }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ FarmId }}',
 '{{ JobAttachmentSettings }}',
 '{{ JobRunAsUser }}',
 '{{ RequiredFileSystemLocationNames }}',
 '{{ RoleArn }}',
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
  - name: queue
    props:
      - name: AllowedStorageProfileIds
        value:
          - '{{ AllowedStorageProfileIds[0] }}'
      - name: DefaultBudgetAction
        value: '{{ DefaultBudgetAction }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: FarmId
        value: '{{ FarmId }}'
      - name: JobAttachmentSettings
        value:
          S3BucketName: '{{ S3BucketName }}'
          RootPrefix: '{{ RootPrefix }}'
      - name: JobRunAsUser
        value:
          Posix:
            User: '{{ User }}'
            Group: '{{ Group }}'
          Windows:
            User: '{{ User }}'
            PasswordArn: '{{ PasswordArn }}'
          RunAs: '{{ RunAs }}'
      - name: RequiredFileSystemLocationNames
        value:
          - '{{ RequiredFileSystemLocationNames[0] }}'
      - name: RoleArn
        value: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.deadline.queues
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queues</code> resource, the following permissions are required:

### Create
```json
deadline:CreateQueue,
deadline:GetQueue,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
logs:CreateLogGroup,
s3:ListBucket
```

### Delete
```json
deadline:DeleteQueue,
deadline:GetQueue,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListQueues,
identitystore:DescribeGroup,
identitystore:DescribeUser,
identitystore:ListGroupMembershipsForMember
```

