---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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

Creates, updates, deletes or gets a <code>load_balancer</code> resource or lists <code>load_balancers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.load_balancers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>The IP address type. The possible values are <code>ipv4</code> (for IPv4 addresses) and <code>dualstack</code> (for IPv4 and IPv6 addresses). You can’t specify <code>dualstack</code> for a load balancer with a UDP or TCP_UDP listener.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>&#91;Application Load Balancers and Network Load Balancers&#93; The IDs of the security groups for the load balancer.</td></tr>
<tr><td><CopyableCode code="load_balancer_attributes" /></td><td><code>array</code></td><td>The load balancer attributes.</td></tr>
<tr><td><CopyableCode code="scheme" /></td><td><code>string</code></td><td>The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.<br />The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.<br />The default is an Internet-facing load balancer.<br />You cannot specify a scheme for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="dns_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the load balancer. This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".<br />If you don't specify a name, AWS CloudFormation generates a unique physical ID for the load balancer. If you specify a name, you cannot perform updates that require replacement of this resource, but you can perform other updates. To replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="load_balancer_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="load_balancer_full_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.<br />&#91;Application Load Balancers&#93; You must specify subnets from at least two Availability Zones.<br />&#91;Application Load Balancers on Outposts&#93; You must specify one Outpost subnet.<br />&#91;Application Load Balancers on Local Zones&#93; You can specify subnets from one or more Local Zones.<br />&#91;Network Load Balancers&#93; You can specify subnets from one or more Availability Zones.<br />&#91;Gateway Load Balancers&#93; You can specify subnets from one or more Availability Zones.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of load balancer. The default is <code>application</code>.</td></tr>
<tr><td><CopyableCode code="canonical_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the load balancer.</td></tr>
<tr><td><CopyableCode code="load_balancer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_mappings" /></td><td><code>array</code></td><td>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.<br />&#91;Application Load Balancers&#93; You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.<br />&#91;Application Load Balancers on Outposts&#93; You must specify one Outpost subnet.<br />&#91;Application Load Balancers on Local Zones&#93; You can specify subnets from one or more Local Zones.<br />&#91;Network Load Balancers&#93; You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.<br />&#91;Gateway Load Balancers&#93; You can specify subnets from one or more Availability Zones. You cannot specify Elastic IP addresses for your subnets.</td></tr>
<tr><td><CopyableCode code="enforce_security_group_inbound_rules_on_private_link_traffic" /></td><td><code>string</code></td><td>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through privatelink.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>load_balancers</code> in a region.
```sql
SELECT
region,
ip_address_type,
security_groups,
load_balancer_attributes,
scheme,
dns_name,
name,
load_balancer_name,
load_balancer_full_name,
subnets,
type,
canonical_hosted_zone_id,
tags,
load_balancer_arn,
subnet_mappings,
enforce_security_group_inbound_rules_on_private_link_traffic
FROM aws.elasticloadbalancingv2.load_balancers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>load_balancer</code>.
```sql
SELECT
region,
ip_address_type,
security_groups,
load_balancer_attributes,
scheme,
dns_name,
name,
load_balancer_name,
load_balancer_full_name,
subnets,
type,
canonical_hosted_zone_id,
tags,
load_balancer_arn,
subnet_mappings,
enforce_security_group_inbound_rules_on_private_link_traffic
FROM aws.elasticloadbalancingv2.load_balancers
WHERE region = 'us-east-1' AND data__Identifier = '<LoadBalancerArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticloadbalancingv2.load_balancers (
 IpAddressType,
 SecurityGroups,
 LoadBalancerAttributes,
 Scheme,
 Name,
 Subnets,
 Type,
 Tags,
 SubnetMappings,
 EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic,
 region
)
SELECT 
'{{ IpAddressType }}',
 '{{ SecurityGroups }}',
 '{{ LoadBalancerAttributes }}',
 '{{ Scheme }}',
 '{{ Name }}',
 '{{ Subnets }}',
 '{{ Type }}',
 '{{ Tags }}',
 '{{ SubnetMappings }}',
 '{{ EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticloadbalancingv2.load_balancers (
 IpAddressType,
 SecurityGroups,
 LoadBalancerAttributes,
 Scheme,
 Name,
 Subnets,
 Type,
 Tags,
 SubnetMappings,
 EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic,
 region
)
SELECT 
 '{{ IpAddressType }}',
 '{{ SecurityGroups }}',
 '{{ LoadBalancerAttributes }}',
 '{{ Scheme }}',
 '{{ Name }}',
 '{{ Subnets }}',
 '{{ Type }}',
 '{{ Tags }}',
 '{{ SubnetMappings }}',
 '{{ EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic }}',
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
  - name: load_balancer
    props:
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: LoadBalancerAttributes
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Scheme
        value: '{{ Scheme }}'
      - name: Name
        value: '{{ Name }}'
      - name: Subnets
        value:
          - '{{ Subnets[0] }}'
      - name: Type
        value: '{{ Type }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: SubnetMappings
        value:
          - SubnetId: '{{ SubnetId }}'
            AllocationId: '{{ AllocationId }}'
            PrivateIPv4Address: '{{ PrivateIPv4Address }}'
            IPv6Address: '{{ IPv6Address }}'
      - name: EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
        value: '{{ EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticloadbalancingv2.load_balancers
WHERE data__Identifier = '<LoadBalancerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>load_balancers</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:ModifyLoadBalancerAttributes,
elasticloadbalancing:AddTags
```

### Delete
```json
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DeleteLoadBalancer
```

### List
```json
elasticloadbalancing:DescribeLoadBalancers
```

### Read
```json
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeLoadBalancerAttributes,
elasticloadbalancing:DescribeTags
```

### Update
```json
elasticloadbalancing:ModifyLoadBalancerAttributes,
elasticloadbalancing:SetSubnets,
elasticloadbalancing:SetIpAddressType,
elasticloadbalancing:SetSecurityGroups,
elasticloadbalancing:AddTags,
elasticloadbalancing:RemoveTags
```

