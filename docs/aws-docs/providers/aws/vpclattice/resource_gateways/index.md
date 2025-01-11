---
title: resource_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_gateways
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

Creates, updates, deletes or gets a <code>resource_gateway</code> resource or lists <code>resource_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a resource gateway for a service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.resource_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcegateway.html"><code>AWS::VpcLattice::ResourceGateway</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>resource_gateways</code> in a region.
```sql
SELECT
region,
ip_address_type,
vpc_identifier,
id,
arn,
subnet_ids,
security_group_ids,
tags,
name
FROM aws.vpclattice.resource_gateways
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_gateway</code>.
```sql
SELECT
region,
ip_address_type,
vpc_identifier,
id,
arn,
subnet_ids,
security_group_ids,
tags,
name
FROM aws.vpclattice.resource_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.vpclattice.resource_gateways (
 IpAddressType,
 VpcIdentifier,
 SubnetIds,
 SecurityGroupIds,
 Tags,
 Name,
 region
)
SELECT 
'{{ IpAddressType }}',
 '{{ VpcIdentifier }}',
 '{{ SubnetIds }}',
 '{{ SecurityGroupIds }}',
 '{{ Tags }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.resource_gateways (
 IpAddressType,
 VpcIdentifier,
 SubnetIds,
 SecurityGroupIds,
 Tags,
 Name,
 region
)
SELECT 
 '{{ IpAddressType }}',
 '{{ VpcIdentifier }}',
 '{{ SubnetIds }}',
 '{{ SecurityGroupIds }}',
 '{{ Tags }}',
 '{{ Name }}',
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
  - name: resource_gateway
    props:
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: VpcIdentifier
        value: '{{ VpcIdentifier }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.resource_gateways
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_gateways</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetResourceGateway,
vpc-lattice:ListTagsForResource
```

### Create
```json
vpc-lattice:CreateResourceGateway,
vpc-lattice:GetResourceGateway,
vpc-lattice:TagResource,
vpc-lattice:ListTagsForResource,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### Update
```json
vpc-lattice:UpdateResourceGateway,
vpc-lattice:GetResourceGateway,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### List
```json
vpc-lattice:ListResourceGateways
```

### Delete
```json
vpc-lattice:DeleteResourceGateway,
vpc-lattice:GetResourceGateway
```
