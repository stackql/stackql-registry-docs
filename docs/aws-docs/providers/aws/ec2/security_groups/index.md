---
title: security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups
  - ec2
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


Used to retrieve a list of <code>security_groups</code> in a region or to create or delete a <code>security_groups</code> resource, use <code>security_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The group name or group ID depending on whether the SG is created in default or specific VPC</td></tr>
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
id
FROM aws.ec2.security_groups
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
 "GroupDescription": "{{ GroupDescription }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.security_groups (
 GroupDescription,
 region
)
SELECT 
{{ GroupDescription }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GroupDescription": "{{ GroupDescription }}",
 "GroupName": "{{ GroupName }}",
 "VpcId": "{{ VpcId }}",
 "SecurityGroupIngress": [
  {
   "CidrIp": "{{ CidrIp }}",
   "CidrIpv6": "{{ CidrIpv6 }}",
   "Description": "{{ Description }}",
   "FromPort": "{{ FromPort }}",
   "SourceSecurityGroupName": "{{ SourceSecurityGroupName }}",
   "ToPort": "{{ ToPort }}",
   "SourceSecurityGroupOwnerId": "{{ SourceSecurityGroupOwnerId }}",
   "IpProtocol": "{{ IpProtocol }}",
   "SourceSecurityGroupId": "{{ SourceSecurityGroupId }}",
   "SourcePrefixListId": "{{ SourcePrefixListId }}"
  }
 ],
 "SecurityGroupEgress": [
  {
   "CidrIp": "{{ CidrIp }}",
   "CidrIpv6": "{{ CidrIpv6 }}",
   "Description": "{{ Description }}",
   "FromPort": "{{ FromPort }}",
   "ToPort": "{{ ToPort }}",
   "IpProtocol": "{{ IpProtocol }}",
   "DestinationSecurityGroupId": "{{ DestinationSecurityGroupId }}",
   "DestinationPrefixListId": "{{ DestinationPrefixListId }}"
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
INSERT INTO aws.ec2.security_groups (
 GroupDescription,
 GroupName,
 VpcId,
 SecurityGroupIngress,
 SecurityGroupEgress,
 Tags,
 region
)
SELECT 
 {{ GroupDescription }},
 {{ GroupName }},
 {{ VpcId }},
 {{ SecurityGroupIngress }},
 {{ SecurityGroupEgress }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.security_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_groups</code> resource, the following permissions are required:

### Create
```json
ec2:CreateSecurityGroup,
ec2:DescribeSecurityGroups,
ec2:RevokeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateTags
```

### List
```json
ec2:DescribeSecurityGroups
```

### Delete
```json
ec2:DeleteSecurityGroup,
ec2:DescribeInstances
```

