---
title: db_cluster_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster_parameter_groups
  - rds
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

Creates, updates, deletes or gets a <code>db_cluster_parameter_group</code> resource or lists <code>db_cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_cluster_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A friendly description for this DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
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
    <td><CopyableCode code="Description, Family, Parameters, region" /></td>
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
Gets all <code>db_cluster_parameter_groups</code> in a region.
```sql
SELECT
region,
description,
family,
parameters,
db_cluster_parameter_group_name,
tags
FROM aws.rds.db_cluster_parameter_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_cluster_parameter_group</code>.
```sql
SELECT
region,
description,
family,
parameters,
db_cluster_parameter_group_name,
tags
FROM aws.rds.db_cluster_parameter_groups
WHERE region = 'us-east-1' AND data__Identifier = '<DBClusterParameterGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_cluster_parameter_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_cluster_parameter_groups (
 Description,
 Family,
 Parameters,
 region
)
SELECT 
'{{ Description }}',
 '{{ Family }}',
 '{{ Parameters }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_cluster_parameter_groups (
 Description,
 Family,
 Parameters,
 DBClusterParameterGroupName,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Family }}',
 '{{ Parameters }}',
 '{{ DBClusterParameterGroupName }}',
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
  - name: db_cluster_parameter_group
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Family
        value: '{{ Family }}'
      - name: Parameters
        value: {}
      - name: DBClusterParameterGroupName
        value: '{{ DBClusterParameterGroupName }}'
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
DELETE FROM aws.rds.db_cluster_parameter_groups
WHERE data__Identifier = '<DBClusterParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_cluster_parameter_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:AddTagsToResource,
rds:CreateDBClusterParameterGroup,
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeDBClusters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource,
rds:ModifyDBClusterParameterGroup,
rds:RemoveTagsFromResource
```

### Read
```json
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource
```

### Update
```json
rds:AddTagsToResource,
rds:DescribeDBClusterParameterGroups,
rds:DescribeDBClusterParameters,
rds:DescribeDBClusters,
rds:DescribeEngineDefaultClusterParameters,
rds:ListTagsForResource,
rds:ModifyDBClusterParameterGroup,
rds:RemoveTagsFromResource,
rds:ResetDBClusterParameterGroup
```

### Delete
```json
rds:DeleteDBClusterParameterGroup
```

### List
```json
rds:DescribeDBClusterParameterGroups
```

