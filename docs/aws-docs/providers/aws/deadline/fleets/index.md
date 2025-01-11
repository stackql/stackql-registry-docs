---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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

Creates, updates, deletes or gets a <code>fleet</code> resource or lists <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Fleet Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capabilities" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_worker_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="min_worker_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="worker_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html"><code>AWS::Deadline::Fleet</code></a>.

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
    <td><CopyableCode code="Configuration, DisplayName, FarmId, MaxWorkerCount, RoleArn, region" /></td>
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
Gets all <code>fleets</code> in a region.
```sql
SELECT
region,
capabilities,
configuration,
description,
display_name,
farm_id,
fleet_id,
max_worker_count,
min_worker_count,
role_arn,
status,
worker_count,
arn,
tags
FROM aws.deadline.fleets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>fleet</code>.
```sql
SELECT
region,
capabilities,
configuration,
description,
display_name,
farm_id,
fleet_id,
max_worker_count,
min_worker_count,
role_arn,
status,
worker_count,
arn,
tags
FROM aws.deadline.fleets
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.fleets (
 Configuration,
 DisplayName,
 FarmId,
 MaxWorkerCount,
 RoleArn,
 region
)
SELECT 
'{{ Configuration }}',
 '{{ DisplayName }}',
 '{{ FarmId }}',
 '{{ MaxWorkerCount }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.fleets (
 Configuration,
 Description,
 DisplayName,
 FarmId,
 MaxWorkerCount,
 MinWorkerCount,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ FarmId }}',
 '{{ MaxWorkerCount }}',
 '{{ MinWorkerCount }}',
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
  - name: fleet
    props:
      - name: Configuration
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: FarmId
        value: '{{ FarmId }}'
      - name: MaxWorkerCount
        value: '{{ MaxWorkerCount }}'
      - name: MinWorkerCount
        value: '{{ MinWorkerCount }}'
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
DELETE FROM aws.deadline.fleets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fleets</code> resource, the following permissions are required:

### Create
```json
deadline:CreateFleet,
deadline:GetFleet,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
logs:CreateLogGroup,
deadline:TagResource,
deadline:ListTagsForResource
```

### Read
```json
deadline:GetFleet,
identitystore:ListGroupMembershipsForMember,
deadline:ListTagsForResource
```

### Update
```json
deadline:UpdateFleet,
deadline:GetFleet,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
deadline:TagResource,
deadline:UntagResource,
deadline:ListTagsForResource
```

### Delete
```json
deadline:DeleteFleet,
deadline:GetFleet,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListFleets,
identitystore:DescribeGroup,
identitystore:DescribeUser,
identitystore:ListGroupMembershipsForMember
```
