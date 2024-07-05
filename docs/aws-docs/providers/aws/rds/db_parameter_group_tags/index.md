---
title: db_parameter_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - db_parameter_group_tags
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

Expands all tag keys and values for <code>db_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBParameterGroup</code> resource creates a custom parameter group for an RDS database family.<br />This type can be declared in a template and referenced in the <code>DBParameterGroupName</code> property of an <code>AWS::RDS::DBInstance</code> resource.<br />For information about configuring parameters for Amazon RDS DB instances, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.<br />For information about configuring parameters for Amazon Aurora DB instances, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.<br />Applying a parameter group to a DB instance may require the DB instance to reboot, resulting in a database outage for the duration of the reboot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_parameter_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group.<br />Constraints:<br />+ Must be 1 to 255 letters, numbers, or hyphens.<br />+ First character must be a letter<br />+ Can't end with a hyphen or contain two consecutive hyphens<br /><br />If you don't specify a value for <code>DBParameterGroupName</code> property, a name is automatically created for the DB parameter group.<br />This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Provides the customer-specified description for this DB parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a DB engine and engine version compatible with that DB parameter group family.<br />The DB parameter group family can't be changed when updating a DB parameter group.<br />To list all of the available parameter group families, use the following command:<br /><code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily"</code> <br />The output contains duplicates.<br />For more information, see <code>CreateDBParameterGroup</code>.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An array of parameter names and values for the parameter update. At least one parameter name and value must be supplied. Subsequent arguments are optional.<br />RDS for Db2 requires you to bring your own Db2 license. You must enter your IBM customer ID (<code>rds.ibm_customer_id</code>) and site number (<code>rds.ibm_site_id</code>) before starting a Db2 instance.<br />For more information about DB parameters and DB parameter groups for Amazon RDS DB engines, see &#91;Working with DB Parameter Groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.<br />For more information about DB cluster and DB instance parameters and parameter groups for Amazon Aurora DB engines, see &#91;Working with DB Parameter Groups and DB Cluster Parameter Groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.<br />AWS CloudFormation doesn't support specifying an apply method for each individual parameter. The default apply method for each parameter is used.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>db_parameter_groups</code> in a region.
```sql
SELECT
region,
db_parameter_group_name,
description,
family,
parameters,
tag_key,
tag_value
FROM aws.rds.db_parameter_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_parameter_group_tags</code> resource, see <a href="/providers/aws/rds/db_parameter_groups/#permissions"><code>db_parameter_groups</code></a>


