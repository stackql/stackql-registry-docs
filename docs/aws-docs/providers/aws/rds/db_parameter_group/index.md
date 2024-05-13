---
title: db_parameter_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_parameter_group
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


Gets or updates an individual <code>db_parameter_group</code> resource, use <code>db_parameter_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBParameterGroup</code> resource creates a custom parameter group for an RDS database family.&lt;br&#x2F;&gt; This type can be declared in a template and referenced in the <code>DBParameterGroupName</code> property of an <code>AWS::RDS::DBInstance</code> resource.&lt;br&#x2F;&gt; For information about configuring parameters for Amazon RDS DB instances, see &#91;Working with parameter groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt; For information about configuring parameters for Amazon Aurora DB instances, see &#91;Working with parameter groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;AuroraUserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.&lt;br&#x2F;&gt;  Applying a parameter group to a DB instance may require the DB instance to reboot, resulting in a database outage for the duration of the reboot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_parameter_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group.&lt;br&#x2F;&gt; Constraints:&lt;br&#x2F;&gt;  +  Must be 1 to 255 letters, numbers, or hyphens.&lt;br&#x2F;&gt;  +  First character must be a letter&lt;br&#x2F;&gt;  +  Can't end with a hyphen or contain two consecutive hyphens&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If you don't specify a value for <code>DBParameterGroupName</code> property, a name is automatically created for the DB parameter group.&lt;br&#x2F;&gt;  This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Provides the customer-specified description for this DB parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a DB engine and engine version compatible with that DB parameter group family.&lt;br&#x2F;&gt;  The DB parameter group family can't be changed when updating a DB parameter group.&lt;br&#x2F;&gt;  To list all of the available parameter group families, use the following command:&lt;br&#x2F;&gt; <code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily"</code>&lt;br&#x2F;&gt; The output contains duplicates.&lt;br&#x2F;&gt; For more information, see <code>CreateDBParameterGroup</code>.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An array of parameter names and values for the parameter update. At least one parameter name and value must be supplied. Subsequent arguments are optional.&lt;br&#x2F;&gt; RDS for Db2 requires you to bring your own Db2 license. You must enter your IBM customer ID (<code>rds.ibm_customer_id</code>) and site number (<code>rds.ibm_site_id</code>) before starting a Db2 instance.&lt;br&#x2F;&gt; For more information about DB parameters and DB parameter groups for Amazon RDS DB engines, see &#91;Working with DB Parameter Groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt; For more information about DB cluster and DB instance parameters and parameter groups for Amazon Aurora DB engines, see &#91;Working with DB Parameter Groups and DB Cluster Parameter Groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;AuroraUserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.&lt;br&#x2F;&gt;  AWS CloudFormation doesn't support specifying an apply method for each individual </td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional array of key-value pairs to apply to this DB parameter group.&lt;br&#x2F;&gt;  Currently, this is the only property that supports drift detection.</td></tr>
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

## `SELECT` Example
```sql
SELECT
region,
db_parameter_group_name,
description,
family,
parameters,
tags
FROM aws.rds.db_parameter_group
WHERE region = 'us-east-1' AND data__Identifier = '<DBParameterGroupName>';
```


## Permissions

To operate on the <code>db_parameter_group</code> resource, the following permissions are required:

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

