---
title: queue_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_environments
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

Creates, updates, deletes or gets a <code>queue_environment</code> resource or lists <code>queue_environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::QueueEnvironment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queue_environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_environment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html"><code>AWS::Deadline::QueueEnvironment</code></a>.

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
    <td><CopyableCode code="FarmId, QueueId, Priority, Template, TemplateType, region" /></td>
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
Gets all <code>queue_environments</code> in a region.
```sql
SELECT
region,
farm_id,
name,
priority,
queue_environment_id,
queue_id,
template,
template_type
FROM aws.deadline.queue_environments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>queue_environment</code>.
```sql
SELECT
region,
farm_id,
name,
priority,
queue_environment_id,
queue_id,
template,
template_type
FROM aws.deadline.queue_environments
WHERE region = 'us-east-1' AND data__Identifier = '<FarmId>|<QueueId>|<QueueEnvironmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queue_environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.queue_environments (
 FarmId,
 Priority,
 QueueId,
 Template,
 TemplateType,
 region
)
SELECT 
'{{ FarmId }}',
 '{{ Priority }}',
 '{{ QueueId }}',
 '{{ Template }}',
 '{{ TemplateType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.queue_environments (
 FarmId,
 Priority,
 QueueId,
 Template,
 TemplateType,
 region
)
SELECT 
 '{{ FarmId }}',
 '{{ Priority }}',
 '{{ QueueId }}',
 '{{ Template }}',
 '{{ TemplateType }}',
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
  - name: queue_environment
    props:
      - name: FarmId
        value: '{{ FarmId }}'
      - name: Priority
        value: '{{ Priority }}'
      - name: QueueId
        value: '{{ QueueId }}'
      - name: Template
        value: '{{ Template }}'
      - name: TemplateType
        value: '{{ TemplateType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.queue_environments
WHERE data__Identifier = '<FarmId|QueueId|QueueEnvironmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queue_environments</code> resource, the following permissions are required:

### Create
```json
deadline:CreateQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Read
```json
deadline:GetQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Update
```json
deadline:UpdateQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteQueueEnvironment,
deadline:GetQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListQueueEnvironments,
identitystore:ListGroupMembershipsForMember
```
