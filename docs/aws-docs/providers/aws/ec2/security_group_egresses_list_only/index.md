---
title: security_group_egresses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_egresses_list_only
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

Lists <code>security_group_egresses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/security_group_egresses/"><code>security_group_egresses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_egresses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds the specified outbound (egress) rule to a security group.<br />An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see &#91;Security group rules&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).<br />You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.<br />You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.<br />Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_egresses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>security_group_egresses</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.security_group_egresses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_group_egresses_list_only</code> resource, see <a href="/providers/aws/ec2/security_group_egresses/#permissions"><code>security_group_egresses</code></a>

