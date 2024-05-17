---
title: security_group_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_rules
  - ec2_api
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.security_group_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The security group rule description. |
| <CopyableCode code="cidrIpv4" /> | `string` | The IPv4 CIDR range. |
| <CopyableCode code="cidrIpv6" /> | `string` | The IPv6 CIDR range. |
| <CopyableCode code="fromPort" /> | `integer` | The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes. |
| <CopyableCode code="groupId" /> | `string` | The ID of the security group. |
| <CopyableCode code="groupOwnerId" /> | `string` | The ID of the Amazon Web Services account that owns the security group.  |
| <CopyableCode code="ipProtocol" /> | `string` | &lt;p&gt;The IP protocol name (&lt;code&gt;tcp&lt;/code&gt;, &lt;code&gt;udp&lt;/code&gt;, &lt;code&gt;icmp&lt;/code&gt;, &lt;code&gt;icmpv6&lt;/code&gt;) or number (see &lt;a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"&gt;Protocol Numbers&lt;/a&gt;). &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;-1&lt;/code&gt; to specify all protocols.&lt;/p&gt; |
| <CopyableCode code="isEgress" /> | `boolean` | Indicates whether the security group rule is an outbound rule. |
| <CopyableCode code="prefixListId" /> | `string` | The ID of the prefix list. |
| <CopyableCode code="referencedGroupInfo" /> | `object` |  Describes the security group that is referenced in the security group rule. |
| <CopyableCode code="securityGroupRuleId" /> | `string` | The ID of the security group rule. |
| <CopyableCode code="tagSet" /> | `array` | The tags applied to the security group rule. |
| <CopyableCode code="toPort" /> | `integer` | The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of &lt;code&gt;-1&lt;/code&gt; indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="security_group_rules_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your security group rules. |
| <CopyableCode code="security_group_rules_Modify" /> | `EXEC` | <CopyableCode code="GroupId, SecurityGroupRule, region" /> | Modifies the rules of a security group. |
