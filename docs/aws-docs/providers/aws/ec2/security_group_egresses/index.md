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
Retrieves a list of <code>security_group_egresses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds the specified outbound (egress) rule to a security group.&lt;br&#x2F;&gt; An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see &#91;Security group rules&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;security-group-rules.html).&lt;br&#x2F;&gt; You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.&lt;br&#x2F;&gt; You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP&#x2F;ICMPv6 type and code. To specify all types or all codes, use -1.&lt;br&#x2F;&gt; Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.security_group_egresses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ec2.security_group_egresses
WHERE region = 'us-east-1'
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

