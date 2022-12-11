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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.security_group_egress</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `security_group_egress_Authorize` | `EXEC` | `GroupId` | &lt;p&gt;[VPC only] Adds the specified outbound (egress) rules to a security group for use with a VPC.&lt;/p&gt; &lt;p&gt;An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 CIDR address ranges, or to the instances that are associated with the specified source security groups.&lt;/p&gt; &lt;p&gt;You specify a protocol for each rule (for example, TCP). For the TCP and UDP protocols, you must also specify the destination port or port range. For the ICMP protocol, you must also specify the ICMP type and code. You can use -1 for the type or code to mean all types or all codes.&lt;/p&gt; &lt;p&gt;Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.&lt;/p&gt; &lt;p&gt;For information about VPC security group quotas, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html"&gt;Amazon VPC quotas&lt;/a&gt;.&lt;/p&gt; |
| `security_group_egress_Revoke` | `EXEC` | `GroupId` | &lt;p&gt;[VPC only] Removes the specified outbound (egress) rules from a security group for EC2-VPC. This action does not apply to security groups for use in EC2-Classic.&lt;/p&gt; &lt;p&gt;You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing rule's values exactly. Each rule has a protocol, from and to ports, and destination (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule.&lt;/p&gt; &lt;p&gt;[Default VPC] If the values you specify do not match the existing rule's values, no error is returned, and the output describes the security group rules that were not revoked.&lt;/p&gt; &lt;p&gt;Amazon Web Services recommends that you describe the security group to verify that the rules were removed.&lt;/p&gt; &lt;p&gt;Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.&lt;/p&gt; |
