---
title: security_group_egresses
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_egresses
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


Used to retrieve a list of <code>security_group_egresses</code> in a region or to create or delete a <code>security_group_egresses</code> resource, use <code>security_group_egress</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds the specified outbound (egress) rule to a security group.&lt;br&#x2F;&gt; An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see &#91;Security group rules&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;security-group-rules.html).&lt;br&#x2F;&gt; You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.&lt;br&#x2F;&gt; You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP&#x2F;ICMPv6 type and code. To specify all types or all codes, use -1.&lt;br&#x2F;&gt; Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_egresses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.ec2.security_group_egresses
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
 "IpProtocol": "{{ IpProtocol }}",
 "GroupId": "{{ GroupId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.security_group_egresses (
 IpProtocol,
 GroupId,
 region
)
SELECT 
{{ IpProtocol }},
 {{ GroupId }},
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
 "ToPort": "{{ ToPort }}",
 "IpProtocol": "{{ IpProtocol }}",
 "DestinationSecurityGroupId": "{{ DestinationSecurityGroupId }}",
 "DestinationPrefixListId": "{{ DestinationPrefixListId }}",
 "GroupId": "{{ GroupId }}"
}
>>>
--all properties
INSERT INTO aws.ec2.security_group_egresses (
 CidrIp,
 CidrIpv6,
 Description,
 FromPort,
 ToPort,
 IpProtocol,
 DestinationSecurityGroupId,
 DestinationPrefixListId,
 GroupId,
 region
)
SELECT 
 {{ CidrIp }},
 {{ CidrIpv6 }},
 {{ Description }},
 {{ FromPort }},
 {{ ToPort }},
 {{ IpProtocol }},
 {{ DestinationSecurityGroupId }},
 {{ DestinationPrefixListId }},
 {{ GroupId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.security_group_egresses
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_group_egresses</code> resource, the following permissions are required:

### Create
```json
ec2:AuthorizeSecurityGroupEgress,
ec2:RevokeSecurityGroupEgress,
ec2:DescribeSecurityGroupRules
```

### List
```json
ec2:DescribeSecurityGroupRules
```

### Delete
```json
ec2:RevokeSecurityGroupEgress,
ec2:DescribeSecurityGroupRules
```

