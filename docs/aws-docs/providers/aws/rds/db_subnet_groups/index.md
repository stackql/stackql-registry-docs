---
title: db_subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_subnet_groups
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


Used to retrieve a list of <code>db_subnet_groups</code> in a region or to create or delete a <code>db_subnet_groups</code> resource, use <code>db_subnet_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::RDS::DBSubnetGroup`` resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region. &lt;br&#x2F;&gt; For more information, see &#91;Working with DB subnet groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_subnet_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>The name for the DB subnet group. This value is stored as a lowercase string.&lt;br&#x2F;&gt; Constraints: Must contain no more than 255 lowercase alphanumeric characters or hyphens. Must not be "Default".&lt;br&#x2F;&gt; Example: ``mysubnetgroup``</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
db_subnet_group_name
FROM aws.rds.db_subnet_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DBSubnetGroupDescription": "{{ DBSubnetGroupDescription }}",
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.rds.db_subnet_groups (
 DBSubnetGroupDescription,
 SubnetIds,
 region
)
SELECT 
{{ DBSubnetGroupDescription }},
 {{ SubnetIds }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DBSubnetGroupDescription": "{{ DBSubnetGroupDescription }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.rds.db_subnet_groups (
 DBSubnetGroupDescription,
 DBSubnetGroupName,
 SubnetIds,
 Tags,
 region
)
SELECT 
 {{ DBSubnetGroupDescription }},
 {{ DBSubnetGroupName }},
 {{ SubnetIds }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.db_subnet_groups
WHERE data__Identifier = '<DBSubnetGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_subnet_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:CreateDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
rds:ListTagsForResource
```

### Delete
```json
rds:DeleteDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:ListTagsForResource
```

### List
```json
rds:DescribeDBSubnetGroups
```

