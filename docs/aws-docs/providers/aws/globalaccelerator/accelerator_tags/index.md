---
title: accelerator_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator_tags
  - globalaccelerator
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

Expands all tag keys and values for <code>accelerators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerator_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::Accelerator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.accelerator_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of accelerator.</td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>IP Address type.</td></tr>
<tr><td><CopyableCode code="ip_addresses" /></td><td><code>array</code></td><td>The IP addresses from BYOIP Prefix pool.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Indicates whether an accelerator is enabled. The value is true or false.</td></tr>
<tr><td><CopyableCode code="dns_name" /></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.</td></tr>
<tr><td><CopyableCode code="ipv4_addresses" /></td><td><code>array</code></td><td>The IPv4 addresses assigned to the accelerator.</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>The IPv6 addresses assigned if the accelerator is dualstack</td></tr>
<tr><td><CopyableCode code="dual_stack_dns_name" /></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.</td></tr>
<tr><td><CopyableCode code="accelerator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
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
Expands tags for all <code>accelerators</code> in a region.
```sql
SELECT
region,
name,
ip_address_type,
ip_addresses,
enabled,
dns_name,
ipv4_addresses,
ipv6_addresses,
dual_stack_dns_name,
accelerator_arn,
tag_key,
tag_value
FROM aws.globalaccelerator.accelerator_tags
;
```


## Permissions

For permissions required to operate on the <code>accelerator_tags</code> resource, see <a href="/providers/aws/globalaccelerator/accelerators/#permissions"><code>accelerators</code></a>

