---
title: security_group_ingresses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_ingresses_list_only
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

Lists <code>security_group_ingresses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/security_group_ingresses/"><code>security_group_ingresses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_ingresses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroupIngress</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_ingresses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Security Group Rule Id</td></tr>
<tr><td><CopyableCode code="cidr_ip" /></td><td><code>string</code></td><td>The IPv4 ranges</td></tr>
<tr><td><CopyableCode code="cidr_ipv6" /></td><td><code>string</code></td><td>&#91;VPC only&#93; The IPv6 ranges</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously</td></tr>
<tr><td><CopyableCode code="from_port" /></td><td><code>integer</code></td><td>The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.<br />Use this for ICMP and any protocol that uses ports.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.<br />You must specify the GroupName property or the GroupId property. For security groups that are in a VPC, you must use the GroupId property.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the security group.</td></tr>
<tr><td><CopyableCode code="ip_protocol" /></td><td><code>string</code></td><td>The IP protocol name (tcp, udp, icmp, icmpv6) or number (see Protocol Numbers).<br />&#91;VPC only&#93; Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or icmpv6 allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For icmpv6, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.</td></tr>
<tr><td><CopyableCode code="source_prefix_list_id" /></td><td><code>string</code></td><td>&#91;EC2-VPC only&#93; The ID of a prefix list.<br /></td></tr>
<tr><td><CopyableCode code="source_security_group_id" /></td><td><code>string</code></td><td>The ID of the security group. You must specify either the security group ID or the security group name. For security groups in a nondefault VPC, you must specify the security group ID.</td></tr>
<tr><td><CopyableCode code="source_security_group_name" /></td><td><code>string</code></td><td>&#91;EC2-Classic, default VPC&#93; The name of the source security group.<br />You must specify the GroupName property or the GroupId property. For security groups that are in a VPC, you must use the GroupId property.</td></tr>
<tr><td><CopyableCode code="source_security_group_owner_id" /></td><td><code>string</code></td><td>&#91;nondefault VPC&#93; The AWS account ID that owns the source security group. You can't specify this property with an IP address range.<br />If you specify SourceSecurityGroupName or SourceSecurityGroupId and that security group is owned by a different account than the account creating the stack, you must specify the SourceSecurityGroupOwnerId; otherwise, this property is optional.</td></tr>
<tr><td><CopyableCode code="to_port" /></td><td><code>integer</code></td><td>The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.<br />Use this for ICMP and any protocol that uses ports.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>security_group_ingresses</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.security_group_ingresses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_group_ingresses_list_only</code> resource, see <a href="/providers/aws/ec2/security_group_ingresses/#permissions"><code>security_group_ingresses</code></a>


