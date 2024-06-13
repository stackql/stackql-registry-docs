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

Creates, updates, deletes or gets a <code>security_group_egress</code> resource or lists <code>security_group_egresses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds the specified outbound (egress) rule to a security group.<br />An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see &#91;Security group rules&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).<br />You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.<br />You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.<br />Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_egresses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cidr_ip" /></td><td><code>string</code></td><td>The IPv4 address range, in CIDR format.<br />You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.<br />For examples of rules that you can add to security groups for specific access scenarios, see &#91;Security group rules for different use cases&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="cidr_ipv6" /></td><td><code>string</code></td><td>The IPv6 address range, in CIDR format.<br />You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.<br />For examples of rules that you can add to security groups for specific access scenarios, see &#91;Security group rules for different use cases&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of an egress (outbound) security group rule.<br />Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@&#91;&#93;+=;&#123;&#125;!$*</td></tr>
<tr><td><CopyableCode code="from_port" /></td><td><code>integer</code></td><td>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</td></tr>
<tr><td><CopyableCode code="to_port" /></td><td><code>integer</code></td><td>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</td></tr>
<tr><td><CopyableCode code="ip_protocol" /></td><td><code>string</code></td><td>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see &#91;Protocol Numbers&#93;(https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).<br />Use <code>-1</code> to specify all protocols. When authorizing security group rules, specifying <code>-1</code> or a protocol number other than <code>tcp</code>, <code>udp</code>, <code>icmp</code>, or <code>icmpv6</code> allows traffic on all ports, regardless of any port range you specify. For <code>tcp</code>, <code>udp</code>, and <code>icmp</code>, you must specify a port range. For <code>icmpv6</code>, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.</td></tr>
<tr><td><CopyableCode code="destination_security_group_id" /></td><td><code>string</code></td><td>The ID of the security group.<br />You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_prefix_list_id" /></td><td><code>string</code></td><td>The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.<br />You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.</td></tr>
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
    <td><CopyableCode code="IpProtocol, GroupId, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>security_group_egresses</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.security_group_egresses
WHERE region = 'us-east-1';
```
Gets all properties from a <code>security_group_egress</code>.
```sql
SELECT
region,
cidr_ip,
cidr_ipv6,
description,
from_port,
to_port,
ip_protocol,
destination_security_group_id,
id,
destination_prefix_list_id,
group_id
FROM aws.ec2.security_group_egresses
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_group_egress</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.security_group_egresses (
 IpProtocol,
 GroupId,
 region
)
SELECT 
'{{ IpProtocol }}',
 '{{ GroupId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ CidrIp }}',
 '{{ CidrIpv6 }}',
 '{{ Description }}',
 '{{ FromPort }}',
 '{{ ToPort }}',
 '{{ IpProtocol }}',
 '{{ DestinationSecurityGroupId }}',
 '{{ DestinationPrefixListId }}',
 '{{ GroupId }}',
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
  - name: security_group_egress
    props:
      - name: CidrIp
        value: '{{ CidrIp }}'
      - name: CidrIpv6
        value: '{{ CidrIpv6 }}'
      - name: Description
        value: '{{ Description }}'
      - name: FromPort
        value: '{{ FromPort }}'
      - name: ToPort
        value: '{{ ToPort }}'
      - name: IpProtocol
        value: '{{ IpProtocol }}'
      - name: DestinationSecurityGroupId
        value: '{{ DestinationSecurityGroupId }}'
      - name: DestinationPrefixListId
        value: '{{ DestinationPrefixListId }}'
      - name: GroupId
        value: '{{ GroupId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.security_group_egresses
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_group_egresses</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeSecurityGroupRules
```

### Create
```json
ec2:AuthorizeSecurityGroupEgress,
ec2:RevokeSecurityGroupEgress,
ec2:DescribeSecurityGroupRules
```

### Update
```json
ec2:UpdateSecurityGroupRuleDescriptionsEgress
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

