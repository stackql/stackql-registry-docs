---
title: user_hierarchy_structures
hide_title: false
hide_table_of_contents: false
keywords:
  - user_hierarchy_structures
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

Creates, updates, deletes or gets an <code>user_hierarchy_structure</code> resource or lists <code>user_hierarchy_structures</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_hierarchy_structures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::UserHierarchyStructure</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.user_hierarchy_structures" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="user_hierarchy_structure_arn" /></td><td><code>string</code></td><td>The identifier of the User Hierarchy Structure.</td></tr>
<tr><td><CopyableCode code="user_hierarchy_structure" /></td><td><code>object</code></td><td>Information about the hierarchy structure.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchystructure.html"><code>AWS::Connect::UserHierarchyStructure</code></a>.

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
    <td><CopyableCode code="InstanceArn, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>user_hierarchy_structure</code>.
```sql
SELECT
region,
instance_arn,
user_hierarchy_structure_arn,
user_hierarchy_structure
FROM aws.connect.user_hierarchy_structures
WHERE region = 'us-east-1' AND data__Identifier = '<UserHierarchyStructureArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_hierarchy_structure</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.user_hierarchy_structures (
 InstanceArn,
 region
)
SELECT 
'{{ InstanceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.user_hierarchy_structures (
 InstanceArn,
 UserHierarchyStructure,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ UserHierarchyStructure }}',
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
  - name: user_hierarchy_structure
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: UserHierarchyStructure
        value:
          LevelOne:
            HierarchyLevelArn: '{{ HierarchyLevelArn }}'
            HierarchyLevelId: '{{ HierarchyLevelId }}'
            Name: '{{ Name }}'
          LevelTwo:
            HierarchyLevelArn: null
            HierarchyLevelId: null
            Name: null
          LevelThree:
            HierarchyLevelArn: null
            HierarchyLevelId: null
            Name: null
          LevelFour:
            HierarchyLevelArn: null
            HierarchyLevelId: null
            Name: null
          LevelFive:
            HierarchyLevelArn: null
            HierarchyLevelId: null
            Name: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.user_hierarchy_structures
WHERE data__Identifier = '<UserHierarchyStructureArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_hierarchy_structures</code> resource, the following permissions are required:

### Create
```json
connect:UpdateUserHierarchyStructure
```

### Read
```json
connect:DescribeUserHierarchyStructure
```

### Delete
```json
connect:UpdateUserHierarchyStructure
```

### Update
```json
connect:UpdateUserHierarchyStructure
```
