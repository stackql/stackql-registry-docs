---
title: parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter_groups
  - memorydb
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

Creates, updates, deletes or gets a <code>parameter_group</code> resource or lists <code>parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The name of the parameter group family that this parameter group is compatible with.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this parameter group.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parameter group.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html"><code>AWS::MemoryDB::ParameterGroup</code></a>.

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
    <td><CopyableCode code="ParameterGroupName, Family, region" /></td>
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
Gets all <code>parameter_groups</code> in a region.
```sql
SELECT
region,
parameter_group_name,
family,
description,
tags,
parameters,
arn
FROM aws.memorydb.parameter_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>parameter_group</code>.
```sql
SELECT
region,
parameter_group_name,
family,
description,
tags,
parameters,
arn
FROM aws.memorydb.parameter_groups
WHERE region = 'us-east-1' AND data__Identifier = '<ParameterGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>parameter_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.memorydb.parameter_groups (
 ParameterGroupName,
 Family,
 region
)
SELECT 
'{{ ParameterGroupName }}',
 '{{ Family }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.memorydb.parameter_groups (
 ParameterGroupName,
 Family,
 Description,
 Tags,
 Parameters,
 region
)
SELECT 
 '{{ ParameterGroupName }}',
 '{{ Family }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ Parameters }}',
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
  - name: parameter_group
    props:
      - name: ParameterGroupName
        value: '{{ ParameterGroupName }}'
      - name: Family
        value: '{{ Family }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Parameters
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.memorydb.parameter_groups
WHERE data__Identifier = '<ParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>parameter_groups</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateParameterGroup,
memorydb:DescribeParameterGroups,
memorydb:TagResource,
memorydb:ListTags
```

### Read
```json
memorydb:DescribeParameterGroups,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateParameterGroup,
memorydb:DescribeParameterGroups,
memorydb:DescribeParameters,
memorydb:DescribeClusters,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:DeleteParameterGroup
```

### List
```json
memorydb:DescribeParameterGroups
```
