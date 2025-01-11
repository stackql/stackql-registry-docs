---
title: db_cluster_parameter_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster_parameter_group_tags
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

Expands all tag keys and values for <code>db_cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster_parameter_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBClusterParameterGroup</code> resource creates a new Amazon RDS DB cluster parameter group.<br />For information about configuring parameters for Amazon Aurora DB clusters, see &#91;Working with parameter groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.<br />If you apply a parameter group to a DB cluster, then its DB instances might need to reboot. This can result in an outage while the DB instances are rebooting.<br />If you apply a change to parameter group associated with a stopped DB cluster, then the updated stack waits until the DB cluster is started.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_cluster_parameter_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.<br />*Aurora MySQL* <br />Example: <code>aurora-mysql5.7</code>, <code>aurora-mysql8.0</code> <br />*Aurora PostgreSQL* <br />Example: <code>aurora-postgresql14</code> <br />*RDS for MySQL* <br />Example: <code>mysql8.0</code> <br />*RDS for PostgreSQL* <br />Example: <code>postgres13</code> <br />To list all of the available parameter group families for a DB engine, use the following command:<br /><code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily" --engine &lt;engine&gt;</code> <br />For example, to list all of the available parameter group families for the Aurora PostgreSQL DB engine, use the following command:<br /><code>aws rds describe-db-engine-versions --query "DBEngineVersions&#91;&#93;.DBParameterGroupFamily" --engine aurora-postgresql</code> <br />The output contains duplicates.<br />The following are the valid DB engine values:<br />+ <code>aurora-mysql</code> <br />+ <code>aurora-postgresql</code> <br />+ <code>mysql</code> <br />+ <code>postgres</code></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Provides a list of parameters for the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB cluster parameter group.<br />Constraints:<br />+ Must not match the name of an existing DB cluster parameter group.<br /><br />This value is stored as a lowercase string.</td></tr>
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
Expands tags for all <code>db_cluster_parameter_groups</code> in a region.
```sql
SELECT
region,
description,
family,
parameters,
db_cluster_parameter_group_name,
tag_key,
tag_value
FROM aws.rds.db_cluster_parameter_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_cluster_parameter_group_tags</code> resource, see <a href="/providers/aws/rds/db_cluster_parameter_groups/#permissions"><code>db_cluster_parameter_groups</code></a>

