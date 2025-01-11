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
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBClusterParameterGroup</code> resource creates a new Amazon RDS DB cluster parameter group.<br />For information about configuring parameters for Amazon Aurora DB clusters, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.<br />If you apply a parameter group to a DB cluster, then its DB instances might need to reboot. This can result in an outage while the DB instances are rebooting.<br />If you apply a change to parameter group associated with a stopped DB cluster, then the updated stack waits until the DB cluster is started.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_cluster_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.<br />*Aurora MySQL* <br />Example: <code>aurora-mysql5.7</code>, <code>aurora-mysql8.0</code> <br />*Aurora PostgreSQL* <br />Example: <code>aurora-postgresql14</code> <br />*RDS for MySQL* <br />Example: <code>mysql8.0</code> <br />*RDS for PostgreSQL* <br />Example: <code>postgres13</code> <br />To list all of the available parameter group families for a DB engine, use the following command:<br /><code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily" --engine &lt;engine&gt;</code> <br />For example, to list all of the available parameter group families for the Aurora PostgreSQL DB engine, use the following command:<br /><code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily" --engine aurora-postgresql</code> <br />The output contains duplicates.<br />The following are the valid DB engine values:<br />+ <code>aurora-mysql</code> <br />+ <code>aurora-postgresql</code> <br />+ <code>mysql</code> <br />+ <code>postgres</code></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Provides a list of parameters for the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB cluster parameter group.<br />Constraints:<br />+ Must not match the name of an existing DB cluster parameter group.<br /><br />This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags to assign to the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html"><code>AWS::RDS::DBClusterParameterGroup</code></a>.

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
