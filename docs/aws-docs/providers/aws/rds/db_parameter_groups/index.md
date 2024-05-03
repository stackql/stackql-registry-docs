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

Used to retrieve a list of <code>db_parameter_groups</code> in a region or create a <code>db_parameter_groups</code> resource, use <code>db_parameter_group</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::RDS::DBParameterGroup`` resource creates a custom parameter group for an RDS database family.&lt;br&#x2F;&gt; This type can be declared in a template and referenced in the ``DBParameterGroupName`` property of an ``AWS::RDS::DBInstance`` resource.&lt;br&#x2F;&gt; For information about configuring parameters for Amazon RDS DB instances, see &#91;Working with parameter groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt; For information about configuring parameters for Amazon Aurora DB instances, see &#91;Working with parameter groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;AuroraUserGuide&#x2F;USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.&lt;br&#x2F;&gt;  Applying a parameter group to a DB instance may require the DB instance to reboot, resulting in a database outage for the duration of the reboot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group.&lt;br&#x2F;&gt; Constraints:&lt;br&#x2F;&gt;  +  Must be 1 to 255 letters, numbers, or hyphens.&lt;br&#x2F;&gt;  +  First character must be a letter&lt;br&#x2F;&gt;  +  Can't end with a hyphen or contain two consecutive hyphens&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If you don't specify a value for ``DBParameterGroupName`` property, a name is automatically created for the DB parameter group.&lt;br&#x2F;&gt;  This value is stored as a lowercase string.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
db_parameter_group_name
FROM aws.rds.db_parameter_groups
WHERE region = 'us-east-1'
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

### List
```json
rds:DescribeDBParameterGroups
```

