---
title: db_subnet_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_subnet_group
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


Gets or updates an individual <code>db_subnet_group</code> resource, use <code>db_subnet_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::RDS::DBSubnetGroup`` resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region. &lt;br&#x2F;&gt; For more information, see &#91;Working with DB subnet groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_subnet_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_subnet_group_description" /></td><td><code>string</code></td><td>The description for the DB subnet group.</td></tr>
<tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>The name for the DB subnet group. This value is stored as a lowercase string.&lt;br&#x2F;&gt; Constraints: Must contain no more than 255 lowercase alphanumeric characters or hyphens. Must not be "Default".&lt;br&#x2F;&gt; Example: ``mysubnetgroup``</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The EC2 Subnet IDs for the DB subnet group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional array of key-value pairs to apply to this DB subnet group.</td></tr>
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
db_subnet_group_description,
db_subnet_group_name,
subnet_ids,
tags
FROM aws.rds.db_subnet_group
WHERE region = 'us-east-1' AND data__Identifier = '<DBSubnetGroupName>';
```


## Permissions

To operate on the <code>db_subnet_group</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBSubnetGroups,
rds:ListTagsForResource
```

### Update
```json
rds:ModifyDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
rds:ListTagsForResource
```

