---
title: security_group_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_rules
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.security_group_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The security group rule description. |
| `toPort` | `integer` | The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of &lt;code&gt;-1&lt;/code&gt; indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.  |
| `isEgress` | `boolean` | Indicates whether the security group rule is an outbound rule. |
| `prefixListId` | `string` | The ID of the prefix list. |
| `referencedGroupInfo` | `object` |  Describes the security group that is referenced in the security group rule. |
| `securityGroupRuleId` | `string` | The ID of the security group rule. |
| `cidrIpv4` | `string` | The IPv4 CIDR range. |
| `groupId` | `string` | The ID of the security group. |
| `ipProtocol` | `string` | &lt;p&gt;The IP protocol name (&lt;code&gt;tcp&lt;/code&gt;, &lt;code&gt;udp&lt;/code&gt;, &lt;code&gt;icmp&lt;/code&gt;, &lt;code&gt;icmpv6&lt;/code&gt;) or number (see &lt;a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"&gt;Protocol Numbers&lt;/a&gt;). &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;-1&lt;/code&gt; to specify all protocols.&lt;/p&gt; |
| `cidrIpv6` | `string` | The IPv6 CIDR range. |
| `groupOwnerId` | `string` | The ID of the Amazon Web Services account that owns the security group.  |
| `tagSet` | `array` | The tags applied to the security group rule. |
| `fromPort` | `integer` | The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `security_group_rules_Describe` | `SELECT` |  | Describes one or more of your security group rules. |
| `security_group_rules_Modify` | `EXEC` | `GroupId, SecurityGroupRule` | Modifies the rules of a security group. |
