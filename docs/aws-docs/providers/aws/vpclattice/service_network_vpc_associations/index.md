---
title: service_network_vpc_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_vpc_associations
  - vpclattice
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


Used to retrieve a list of <code>service_network_vpc_associations</code> in a region or to create or delete a <code>service_network_vpc_associations</code> resource, use <code>service_network_vpc_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a VPC with a service network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_network_vpc_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.vpclattice.service_network_vpc_associations
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
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "ServiceNetworkIdentifier": "{{ ServiceNetworkIdentifier }}",
 "VpcIdentifier": "{{ VpcIdentifier }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.vpclattice.service_network_vpc_associations (
 SecurityGroupIds,
 ServiceNetworkIdentifier,
 VpcIdentifier,
 Tags,
 region
)
SELECT 
{{ SecurityGroupIds }},
 {{ ServiceNetworkIdentifier }},
 {{ VpcIdentifier }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "ServiceNetworkIdentifier": "{{ ServiceNetworkIdentifier }}",
 "VpcIdentifier": "{{ VpcIdentifier }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.vpclattice.service_network_vpc_associations (
 SecurityGroupIds,
 ServiceNetworkIdentifier,
 VpcIdentifier,
 Tags,
 region
)
SELECT 
 {{ SecurityGroupIds }},
 {{ ServiceNetworkIdentifier }},
 {{ VpcIdentifier }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.service_network_vpc_associations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_network_vpc_associations</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateServiceNetworkVpcAssociation,
vpc-lattice:GetServiceNetworkVpcAssociation,
vpc-lattice:ListServiceNetworkVpcAssociations,
vpc-lattice:ListTagsForResource,
ec2:DescribeSecurityGroups,
ec2:DescribeVpcs,
vpc-lattice:TagResource
```

### Delete
```json
vpc-lattice:DeleteServiceNetworkVpcAssociation,
vpc-lattice:GetServiceNetworkVpcAssociation
```

### List
```json
vpc-lattice:ListServiceNetworkVpcAssociations
```

