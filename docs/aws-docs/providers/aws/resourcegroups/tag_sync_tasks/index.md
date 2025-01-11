---
title: tag_sync_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_sync_tasks
  - resourcegroups
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

Creates, updates, deletes or gets a <code>tag_sync_task</code> resource or lists <code>tag_sync_tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_sync_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ResourceGroups::TagSyncTask</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourcegroups.tag_sync_tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task</td></tr>
<tr><td><CopyableCode code="group_arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the ApplicationGroup for which the TagSyncTask is created</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The Name of the application group for which the TagSyncTask is created</td></tr>
<tr><td><CopyableCode code="task_arn" /></td><td><code>string</code></td><td>The ARN of the TagSyncTask resource</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the TagSyncTask</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-tagsynctask.html"><code>AWS::ResourceGroups::TagSyncTask</code></a>.

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
    <td><CopyableCode code="Group, TagKey, TagValue, RoleArn, region" /></td>
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
Gets all <code>tag_sync_tasks</code> in a region.
```sql
SELECT
region,
group,
group_arn,
group_name,
task_arn,
tag_key,
tag_value,
role_arn,
status
FROM aws.resourcegroups.tag_sync_tasks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>tag_sync_task</code>.
```sql
SELECT
region,
group,
group_arn,
group_name,
task_arn,
tag_key,
tag_value,
role_arn,
status
FROM aws.resourcegroups.tag_sync_tasks
WHERE region = 'us-east-1' AND data__Identifier = '<TaskArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_sync_task</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.resourcegroups.tag_sync_tasks (
 Group,
 TagKey,
 TagValue,
 RoleArn,
 region
)
SELECT 
'{{ Group }}',
 '{{ TagKey }}',
 '{{ TagValue }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.resourcegroups.tag_sync_tasks (
 Group,
 TagKey,
 TagValue,
 RoleArn,
 region
)
SELECT 
 '{{ Group }}',
 '{{ TagKey }}',
 '{{ TagValue }}',
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
  - name: tag_sync_task
    props:
      - name: Group
        value: '{{ Group }}'
      - name: TagKey
        value: '{{ TagKey }}'
      - name: TagValue
        value: '{{ TagValue }}'
      - name: RoleArn
        value: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.resourcegroups.tag_sync_tasks
WHERE data__Identifier = '<TaskArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tag_sync_tasks</code> resource, the following permissions are required:

### Create
```json
resource-groups:StartTagSyncTask,
resource-groups:CreateGroup,
iam:PassRole
```

### Read
```json
resource-groups:GetTagSyncTask
```

### Delete
```json
resource-groups:CancelTagSyncTask,
resource-groups:DeleteGroup
```

### List
```json
resource-groups:ListTagSyncTasks
```
