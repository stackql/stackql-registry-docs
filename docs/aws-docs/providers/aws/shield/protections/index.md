---
title: protections
hide_title: false
hide_table_of_contents: false
keywords:
  - protections
  - shield
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


Used to retrieve a list of <code>protections</code> in a region or to create or delete a <code>protections</code> resource, use <code>protection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="protection_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
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
protection_arn
FROM aws.shield.protections
;
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
 "Name": "{{ Name }}",
 "ResourceArn": "{{ ResourceArn }}"
}
>>>
--required properties only
INSERT INTO aws.shield.protections (
 Name,
 ResourceArn,
 region
)
SELECT 
{{ Name }},
 {{ ResourceArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "ResourceArn": "{{ ResourceArn }}",
 "HealthCheckArns": [
  "{{ HealthCheckArns[0] }}"
 ],
 "ApplicationLayerAutomaticResponseConfiguration": {
  "Action": {},
  "Status": "{{ Status }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.shield.protections (
 Name,
 ResourceArn,
 HealthCheckArns,
 ApplicationLayerAutomaticResponseConfiguration,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ ResourceArn }},
 {{ HealthCheckArns }},
 {{ ApplicationLayerAutomaticResponseConfiguration }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.shield.protections
WHERE data__Identifier = '<ProtectionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>protections</code> resource, the following permissions are required:

### Create
```json
shield:CreateProtection,
shield:DeleteProtection,
shield:DescribeProtection,
shield:ListProtections,
shield:EnableApplicationLayerAutomaticResponse,
shield:AssociateHealthCheck,
shield:TagResource,
ec2:DescribeAddresses,
elasticloadbalancing:DescribeLoadBalancers,
route53:GetHealthCheck,
iam:GetRole,
iam:CreateServiceLinkedRole,
wafv2:GetWebACLForResource,
wafv2:GetWebACL
```

### Delete
```json
shield:DeleteProtection,
shield:UntagResource
```

### List
```json
shield:ListProtections
```

