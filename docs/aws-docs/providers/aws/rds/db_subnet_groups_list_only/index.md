---
title: db_subnet_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_subnet_groups_list_only
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

Lists <code>db_subnet_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_subnet_groups/"><code>db_subnet_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_subnet_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBSubnetGroup</code> resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region. <br />For more information, see &#91;Working with DB subnet groups&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_subnet_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>The name for the DB subnet group. This value is stored as a lowercase string.<br />Constraints:<br />+ Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens.<br />+ Must not be default.<br />+ First character must be a letter.<br /><br />Example: <code>mydbsubnetgroup</code></td></tr>
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
Lists all <code>db_subnet_groups</code> in a region.
```sql
SELECT
region,
db_subnet_group_name
FROM aws.rds.db_subnet_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_subnet_groups_list_only</code> resource, see <a href="/providers/aws/rds/db_subnet_groups/#permissions"><code>db_subnet_groups</code></a>

