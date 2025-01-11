---
title: resource_gateway_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_gateway_tags
  - vpclattice
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

Expands all tag keys and values for <code>resource_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_gateway_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a resource gateway for a service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.resource_gateway_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>resource_gateways</code> in a region.
```sql
SELECT
region,
ip_address_type,
vpc_identifier,
id,
arn,
subnet_ids,
security_group_ids,
name,
tag_key,
tag_value
FROM aws.vpclattice.resource_gateway_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_gateway_tags</code> resource, see <a href="/providers/aws/vpclattice/resource_gateways/#permissions"><code>resource_gateways</code></a>

