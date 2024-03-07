---
title: accelerator
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator
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
Gets an individual <code>accelerator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>accelerator</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.globalaccelerator.accelerator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of accelerator.</td></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td>IP Address type.</td></tr>
<tr><td><code>ip_addresses</code></td><td><code>array</code></td><td>The IP addresses from BYOIP Prefix pool.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Indicates whether an accelerator is enabled. The value is true or false.</td></tr>
<tr><td><code>dns_name</code></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.</td></tr>
<tr><td><code>ipv4_addresses</code></td><td><code>array</code></td><td>The IPv4 addresses assigned to the accelerator.</td></tr>
<tr><td><code>ipv6_addresses</code></td><td><code>array</code></td><td>The IPv6 addresses assigned if the accelerator is dualstack</td></tr>
<tr><td><code>dual_stack_dns_name</code></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.</td></tr>
<tr><td><code>accelerator_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
tags
FROM awscc.globalaccelerator.accelerator
WHERE data__Identifier = '{AcceleratorArn}';
```

## Permissions

To operate on the <code>accelerator</code> resource, the following permissions are required:

### Read
```json
globalaccelerator:DescribeAccelerator
```

### Update
```json
globalaccelerator:UpdateAccelerator,
globalaccelerator:TagResource,
globalaccelerator:UntagResource,
globalaccelerator:DescribeAccelerator
```

### Delete
```json
globalaccelerator:UpdateAccelerator,
globalaccelerator:DeleteAccelerator,
globalaccelerator:DescribeAccelerator
```

