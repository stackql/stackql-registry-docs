---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - m2
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


Used to retrieve a list of <code>environments</code> in a region or to create or delete a <code>environments</code> resource, use <code>environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a runtime environment that can run migrated mainframe applications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.m2.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
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
environment_arn
FROM aws.m2.environments
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
 "EngineType": "{{ EngineType }}",
 "InstanceType": "{{ InstanceType }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.m2.environments (
 EngineType,
 InstanceType,
 Name,
 region
)
SELECT 
{{ EngineType }},
 {{ InstanceType }},
 {{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "EngineType": "{{ EngineType }}",
 "EngineVersion": "{{ EngineVersion }}",
 "HighAvailabilityConfig": {
  "DesiredCapacity": "{{ DesiredCapacity }}"
 },
 "InstanceType": "{{ InstanceType }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "Name": "{{ Name }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "StorageConfigurations": [
  {}
 ],
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.m2.environments (
 Description,
 EngineType,
 EngineVersion,
 HighAvailabilityConfig,
 InstanceType,
 KmsKeyId,
 Name,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 SecurityGroupIds,
 StorageConfigurations,
 SubnetIds,
 Tags,
 region
)
SELECT 
 {{ Description }},
 {{ EngineType }},
 {{ EngineVersion }},
 {{ HighAvailabilityConfig }},
 {{ InstanceType }},
 {{ KmsKeyId }},
 {{ Name }},
 {{ PreferredMaintenanceWindow }},
 {{ PubliclyAccessible }},
 {{ SecurityGroupIds }},
 {{ StorageConfigurations }},
 {{ SubnetIds }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.m2.environments
WHERE data__Identifier = '<EnvironmentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:ModifyNetworkInterfaceAttribute,
elasticfilesystem:DescribeMountTargets,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:AddTags,
fsx:DescribeFileSystems,
iam:CreateServiceLinkedRole,
kms:DescribeKey,
kms:CreateGrant,
m2:CreateEnvironment,
m2:GetEnvironment,
m2:ListTagsForResource,
m2:TagResource
```

### Delete
```json
elasticloadbalancing:DeleteLoadBalancer,
m2:DeleteEnvironment,
m2:GetEnvironment
```

### List
```json
m2:ListEnvironments
```

