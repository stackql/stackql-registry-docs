---
title: transit_gateway_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_tags
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

Expands all tag keys and values for <code>transit_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_route_table_propagation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_accept_shared_attachments" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_route_table_association" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpn_ecmp_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_referencing_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="multicast_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_side_asn" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_cidr_blocks" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="association_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="propagation_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>transit_gateways</code> in a region.
```sql
SELECT
region,
default_route_table_propagation,
transit_gateway_arn,
description,
auto_accept_shared_attachments,
default_route_table_association,
id,
vpn_ecmp_support,
dns_support,
security_group_referencing_support,
multicast_support,
amazon_side_asn,
transit_gateway_cidr_blocks,
association_default_route_table_id,
propagation_default_route_table_id,
tag_key,
tag_value
FROM aws.ec2.transit_gateway_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transit_gateway_tags</code> resource, see <a href="/providers/aws/ec2/transit_gateways/#permissions"><code>transit_gateways</code></a>

