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

Creates, updates, deletes or gets a <code>queue</code> resource or lists <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Queue Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allowed_storage_profile_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_budget_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_attachment_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="job_run_as_user" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="required_file_system_location_names" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html"><code>AWS::Deadline::Queue</code></a>.

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
    <td><CopyableCode code="DisplayName, FarmId, region" /></td>
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
Gets all <code>queues</code> in a region.
```sql
SELECT
region,
allowed_storage_profile_ids,
default_budget_action,
description,
display_name,
farm_id,
job_attachment_settings,
job_run_as_user,
queue_id,
required_file_system_location_names,
role_arn,
arn,
tags
FROM aws.deadline.queues
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>queue</code>.
```sql
SELECT
region,
allowed_storage_profile_ids,
default_budget_action,
description,
display_name,
farm_id,
job_attachment_settings,
job_run_as_user,
queue_id,
required_file_system_location_names,
role_arn,
arn,
tags
FROM aws.deadline.queues
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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
/*+ create */
INSERT INTO aws.deadline.queues (
 DisplayName,
 FarmId,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ FarmId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 Tags,
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
s3:ListBucket,
deadline:TagResource,
deadline:ListTagsForResource
```

### Read
```json
deadline:GetQueue,
identitystore:ListGroupMembershipsForMember,
deadline:ListTagsForResource
```

### Update
```json
deadline:UpdateQueue,
deadline:GetQueue,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
logs:CreateLogGroup,
s3:ListBucket,
deadline:TagResource,
deadline:UntagResource,
deadline:ListTagsForResource
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
