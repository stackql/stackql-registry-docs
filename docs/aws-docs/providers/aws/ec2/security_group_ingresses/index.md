---
title: security_group_ingresses
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_ingresses
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


Used to retrieve a list of <code>security_group_ingresses</code> in a region or to create or delete a <code>security_group_ingresses</code> resource, use <code>security_group_ingress</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_ingresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroupIngress</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_ingresses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Security Group Rule Id</td></tr>
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
FROM aws.ec2.security_group_ingresses
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
 "IpProtocol": "{{ IpProtocol }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.security_group_ingresses (
 IpProtocol,
 region
)
SELECT 
{{ .IpProtocol }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CidrIp": "{{ CidrIp }}",
 "CidrIpv6": "{{ CidrIpv6 }}",
 "Description": "{{ Description }}",
 "FromPort": "{{ FromPort }}",
 "GroupId": "{{ GroupId }}",
 "GroupName": "{{ GroupName }}",
 "IpProtocol": "{{ IpProtocol }}",
 "SourcePrefixListId": "{{ SourcePrefixListId }}",
 "SourceSecurityGroupId": "{{ SourceSecurityGroupId }}",
 "SourceSecurityGroupName": "{{ SourceSecurityGroupName }}",
 "SourceSecurityGroupOwnerId": "{{ SourceSecurityGroupOwnerId }}",
 "ToPort": "{{ ToPort }}"
}
>>>
--all properties
INSERT INTO aws.ec2.security_group_ingresses (
 CidrIp,
 CidrIpv6,
 Description,
 FromPort,
 GroupId,
 GroupName,
 IpProtocol,
 SourcePrefixListId,
 SourceSecurityGroupId,
 SourceSecurityGroupName,
 SourceSecurityGroupOwnerId,
 ToPort,
 region
)
SELECT 
 {{ .CidrIp }},
 {{ .CidrIpv6 }},
 {{ .Description }},
 {{ .FromPort }},
 {{ .GroupId }},
 {{ .GroupName }},
 {{ .IpProtocol }},
 {{ .SourcePrefixListId }},
 {{ .SourceSecurityGroupId }},
 {{ .SourceSecurityGroupName }},
 {{ .SourceSecurityGroupOwnerId }},
 {{ .ToPort }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.security_group_ingresses
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_group_ingresses</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeSecurityGroupRules,
ec2:AuthorizeSecurityGroupIngress
```

### Delete
```json
ec2:DescribeSecurityGroupRules,
ec2:RevokeSecurityGroupIngress
```

### List
```json
ec2:DescribeSecurityGroupRules
```

