---
title: db_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_parameter_groups
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

Creates, updates, deletes or gets a <code>db_parameter_group</code> resource or lists <code>db_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBParameterGroup</code> resource creates a custom parameter group for an RDS database family. This type can be declared in a template and referenced in the <code>DBParameterGroupName</code> property of an <code>AWS::RDS::DBInstance</code> resource. For information about configuring parameters for Amazon RDS DB instances, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*. For information about configuring parameters for Amazon Aurora DB instances, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*. Applying a parameter group to a DB instance may require the DB instance to reboot, resulting in a database outage for the duration of the reboot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group. Constraints: + Must be 1 to 255 letters, numbers, or hyphens. + First character must be a letter + Can't end with a hyphen or contain two consecutive hyphens If you don't specify a value for <code>DBParameterGroupName</code> property, a name is automatically created for the DB parameter group. This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Provides the customer-specified description for this DB parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a DB engine and engine version compatible with that DB parameter group family. The DB parameter group family can't be changed when updating a DB parameter group. To list all of the available parameter group families, use the following command: <code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily"</code> The output contains duplicates. For more information, see <code>CreateDBParameterGroup</code>.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An array of parameter names and values for the parameter update. At least one parameter name and value must be supplied. Subsequent arguments are optional. RDS for Db2 requires you to bring your own Db2 license. You must enter your IBM customer ID (<code>rds.ibm_customer_id</code>) and site number (<code>rds.ibm_site_id</code>) before starting a Db2 instance. For more information about DB parameters and DB parameter groups for Amazon RDS DB engines, see &#91;Working with DB Parameter Groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*. For more information about DB cluster and DB instance parameters and parameter groups for Amazon Aurora DB engines, see &#91;Working with DB Parameter Groups and DB Cluster Parameter Groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*. AWS CloudFormation doesn't support specifying an apply method for each individual parameter. The default apply method for each parameter is used.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional array of key-value pairs to apply to this DB parameter group. Currently, this is the only property that supports drift detection.</td></tr>
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
    <td><CopyableCode code="Family, Description, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>db_parameter_groups</code> in a region.
```sql
SELECT
region,
db_parameter_group_name
FROM aws.rds.db_parameter_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>db_parameter_group</code>.
```sql
SELECT
region,
db_parameter_group_name,
description,
family,
parameters,
tags
FROM aws.rds.db_parameter_groups
WHERE region = 'us-east-1' AND data__Identifier = '<DBParameterGroupName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_parameter_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_parameter_groups (
 Description,
 Family,
 region
)
SELECT 
'{{ Description }}',
 '{{ Family }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_parameter_groups (
 DBParameterGroupName,
 Description,
 Family,
 Parameters,
 Tags,
 region
)
SELECT 
 '{{ DBParameterGroupName }}',
 '{{ Description }}',
 '{{ Family }}',
 '{{ Parameters }}',
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
  - name: db_parameter_group
    props:
      - name: DBParameterGroupName
        value: '{{ DBParameterGroupName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Family
        value: '{{ Family }}'
      - name: Parameters
        value: {}
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
DELETE FROM aws.rds.db_parameter_groups
WHERE data__Identifier = '<DBParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_parameter_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:AddTagsToResource,
rds:CreateDBParameterGroup,
rds:DescribeDBParameterGroups,
rds:DescribeDBParameters,
rds:DescribeEngineDefaultParameters,
rds:ListTagsForResource,
rds:ModifyDBParameterGroup,
rds:RemoveTagsFromResource
```

### Read
```json
rds:DescribeDBParameterGroups,
rds:DescribeDBParameters,
rds:DescribeEngineDefaultParameters,
rds:ListTagsForResource
```

### Update
```json
rds:AddTagsToResource,
rds:DescribeDBParameterGroups,
rds:DescribeDBParameters,
rds:DescribeEngineDefaultParameters,
rds:ListTagsForResource,
rds:ModifyDBParameterGroup,
rds:ResetDBParameterGroup,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DeleteDBParameterGroup
```

### List
```json
rds:DescribeDBParameterGroups
```

