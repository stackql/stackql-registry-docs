---
title: load_balancer_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_tags
  - elasticloadbalancingv2
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

Expands all tag keys and values for <code>load_balancers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.load_balancer_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>The IP address type. Internal load balancers must use <code>ipv4</code>.<br />&#91;Application Load Balancers&#93; The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).<br />Application Load Balancer authentication supports IPv4 addresses only when connecting to an Identity Provider (IdP) or Amazon Cognito endpoint. Without a public IPv4 address the load balancer can't complete the authentication process, resulting in HTTP 500 errors.<br />&#91;Network Load Balancers and Gateway Load Balancers&#93; The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</td></tr>
<tr><td><CopyableCode code="enable_prefix_for_ipv6_source_nat" /></td><td><code>string</code></td><td>&#91;Network Load Balancers with UDP listeners&#93; Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>&#91;Application Load Balancers and Network Load Balancers&#93; The IDs of the security groups for the load balancer.</td></tr>
<tr><td><CopyableCode code="load_balancer_attributes" /></td><td><code>array</code></td><td>The load balancer attributes.</td></tr>
<tr><td><CopyableCode code="minimum_load_balancer_capacity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="scheme" /></td><td><code>string</code></td><td>The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.<br />The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.<br />The default is an Internet-facing load balancer.<br />You can't specify a scheme for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="dns_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the load balancer. This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".<br />If you don't specify a name, AWS CloudFormation generates a unique physical ID for the load balancer. If you specify a name, you cannot perform updates that require replacement of this resource, but you can perform other updates. To replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="load_balancer_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="load_balancer_full_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.<br />&#91;Application Load Balancers&#93; You must specify subnets from at least two Availability Zones.<br />&#91;Application Load Balancers on Outposts&#93; You must specify one Outpost subnet.<br />&#91;Application Load Balancers on Local Zones&#93; You can specify subnets from one or more Local Zones.<br />&#91;Network Load Balancers and Gateway Load Balancers&#93; You can specify subnets from one or more Availability Zones.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of load balancer. The default is <code>application</code>.</td></tr>
<tr><td><CopyableCode code="canonical_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="load_balancer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_mappings" /></td><td><code>array</code></td><td>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.<br />&#91;Application Load Balancers&#93; You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.<br />&#91;Application Load Balancers on Outposts&#93; You must specify one Outpost subnet.<br />&#91;Application Load Balancers on Local Zones&#93; You can specify subnets from one or more Local Zones.<br />&#91;Network Load Balancers&#93; You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.<br />&#91;Gateway Load Balancers&#93; You can specify subnets from one or more Availability Zones. You can't specify Elastic IP addresses for your subnets.</td></tr>
<tr><td><CopyableCode code="enforce_security_group_inbound_rules_on_private_link_traffic" /></td><td><code>string</code></td><td>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through privatelink.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>load_balancers</code> in a region.
```sql
SELECT
region,
ip_address_type,
enable_prefix_for_ipv6_source_nat,
security_groups,
load_balancer_attributes,
minimum_load_balancer_capacity,
scheme,
dns_name,
name,
load_balancer_name,
load_balancer_full_name,
subnets,
type,
canonical_hosted_zone_id,
load_balancer_arn,
subnet_mappings,
enforce_security_group_inbound_rules_on_private_link_traffic,
tag_key,
tag_value
FROM aws.elasticloadbalancingv2.load_balancer_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>load_balancer_tags</code> resource, see <a href="/providers/aws/elasticloadbalancingv2/load_balancers/#permissions"><code>load_balancers</code></a>

