---
title: transit_gateway_multicast_domain_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain_tags
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

Expands all tag keys and values for <code>transit_gateway_multicast_domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastDomain type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_domain_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="transit_gateway_multicast_domain_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time the transit gateway multicast domain was created.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>The options for the transit gateway multicast domain.</td></tr>
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
Expands tags for all <code>transit_gateway_multicast_domains</code> in a region.
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
transit_gateway_multicast_domain_arn,
transit_gateway_id,
state,
creation_time,
options,
tag_key,
tag_value
FROM aws.ec2.transit_gateway_multicast_domain_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transit_gateway_multicast_domain_tags</code> resource, see <a href="/providers/aws/ec2/transit_gateway_multicast_domains/#permissions"><code>transit_gateway_multicast_domains</code></a>

