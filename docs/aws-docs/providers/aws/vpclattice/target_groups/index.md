---
title: target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - target_groups
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


Used to retrieve a list of <code>target_groups</code> in a region or to create or delete a <code>target_groups</code> resource, use <code>target_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.target_groups" /></td></tr>
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
FROM aws.vpclattice.target_groups
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
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.vpclattice.target_groups (
 Type,
 region
)
SELECT 
{{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Config": {
  "Port": "{{ Port }}",
  "Protocol": "{{ Protocol }}",
  "ProtocolVersion": "{{ ProtocolVersion }}",
  "IpAddressType": "{{ IpAddressType }}",
  "LambdaEventStructureVersion": "{{ LambdaEventStructureVersion }}",
  "VpcIdentifier": "{{ VpcIdentifier }}",
  "HealthCheck": {
   "Enabled": "{{ Enabled }}",
   "Protocol": "{{ Protocol }}",
   "ProtocolVersion": "{{ ProtocolVersion }}",
   "Port": "{{ Port }}",
   "Path": "{{ Path }}",
   "HealthCheckIntervalSeconds": "{{ HealthCheckIntervalSeconds }}",
   "HealthCheckTimeoutSeconds": "{{ HealthCheckTimeoutSeconds }}",
   "HealthyThresholdCount": "{{ HealthyThresholdCount }}",
   "UnhealthyThresholdCount": "{{ UnhealthyThresholdCount }}",
   "Matcher": {
    "HttpCode": "{{ HttpCode }}"
   }
  }
 },
 "Name": "{{ Name }}",
 "Type": "{{ Type }}",
 "Targets": [
  {
   "Id": "{{ Id }}",
   "Port": "{{ Port }}"
  }
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
INSERT INTO aws.vpclattice.target_groups (
 Config,
 Name,
 Type,
 Targets,
 Tags,
 region
)
SELECT 
 {{ .Config }},
 {{ .Name }},
 {{ .Type }},
 {{ .Targets }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.target_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>target_groups</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:RegisterTargets,
vpc-lattice:ListTargets,
vpc-lattice:ListTagsForResource,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
ec2:DescribeVpcs,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeAvailabilityZoneMappings,
lambda:Invoke,
lambda:AddPermission,
elasticloadbalancing:DescribeLoadBalancers,
iam:CreateServiceLinkedRole
```

### Delete
```json
vpc-lattice:DeleteTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:DeregisterTargets,
vpc-lattice:ListTargets,
lambda:RemovePermission
```

### List
```json
vpc-lattice:ListTargetGroups
```

