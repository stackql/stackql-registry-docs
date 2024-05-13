---
title: security_group_egress
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_egress
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


Gets or updates an individual <code>security_group_egress</code> resource, use <code>security_group_egresses</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds the specified outbound (egress) rule to a security group.&lt;br&#x2F;&gt; An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see &#91;Security group rules&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;security-group-rules.html).&lt;br&#x2F;&gt; You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.&lt;br&#x2F;&gt; You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP&#x2F;ICMPv6 type and code. To specify all types or all codes, use -1.&lt;br&#x2F;&gt; Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_egress" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cidr_ip" /></td><td><code>string</code></td><td>The IPv4 address range, in CIDR format.&lt;br&#x2F;&gt; You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.&lt;br&#x2F;&gt; For examples of rules that you can add to security groups for specific access scenarios, see &#91;Security group rules for different use cases&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;security-group-rules-reference.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="cidr_ipv6" /></td><td><code>string</code></td><td>The IPv6 address range, in CIDR format.&lt;br&#x2F;&gt; You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.&lt;br&#x2F;&gt; For examples of rules that you can add to security groups for specific access scenarios, see &#91;Security group rules for different use cases&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;security-group-rules-reference.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of an egress (outbound) security group rule.&lt;br&#x2F;&gt; Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:&#x2F;()#,@&#91;&#93;+=;&#123;&#125;!$*</td></tr>
<tr><td><CopyableCode code="from_port" /></td><td><code>integer</code></td><td>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</td></tr>
<tr><td><CopyableCode code="to_port" /></td><td><code>integer</code></td><td>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</td></tr>
<tr><td><CopyableCode code="ip_protocol" /></td><td><code>string</code></td><td>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see &#91;Protocol Numbers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;www.iana.org&#x2F;assignments&#x2F;protocol-numbers&#x2F;protocol-numbers.xhtml)).&lt;br&#x2F;&gt; Use <code>-1</code> to specify all protocols. When authorizing security group rules, specifying <code>-1</code> or a protocol number other than <code>tcp</code>, <code>udp</code>, <code>icmp</code>, or <code>icmpv6</code> allows traffic on all ports, regardless of any port range you specify. For <code>tcp</code>, <code>udp</code>, and <code>icmp</code>, you must specify a port range. For <code>icmpv6</code>, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.</td></tr>
<tr><td><CopyableCode code="destination_security_group_id" /></td><td><code>string</code></td><td>The ID of the security group.&lt;br&#x2F;&gt; You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_prefix_list_id" /></td><td><code>string</code></td><td>The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.&lt;br&#x2F;&gt; You must specify exactly one of the following: <code>CidrIp</code>, <code>CidrIpv6</code>, <code>DestinationPrefixListId</code>, or <code>DestinationSecurityGroupId</code>.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.security_group_egress
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>security_group_egress</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeSecurityGroupRules
```

### Update
```json
ec2:UpdateSecurityGroupRuleDescriptionsEgress
```

