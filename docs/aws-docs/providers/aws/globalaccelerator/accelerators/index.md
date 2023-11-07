---
title: accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerators
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
Retrieves a list of <code>accelerators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.globalaccelerator.accelerators</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of accelerator.</td></tr>
<tr><td><code>IpAddressType</code></td><td><code>string</code></td><td>IP Address type.</td></tr>
<tr><td><code>IpAddresses</code></td><td><code>array</code></td><td>The IP addresses from BYOIP Prefix pool.</td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td>Indicates whether an accelerator is enabled. The value is true or false.</td></tr>
<tr><td><code>DnsName</code></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.</td></tr>
<tr><td><code>Ipv4Addresses</code></td><td><code>array</code></td><td>The IPv4 addresses assigned to the accelerator.</td></tr>
<tr><td><code>Ipv6Addresses</code></td><td><code>array</code></td><td>The IPv6 addresses assigned if the accelerator is dualstack</td></tr>
<tr><td><code>DualStackDnsName</code></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.</td></tr>
<tr><td><code>AcceleratorArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.globalaccelerator.accelerators
WHERE region = 'us-east-1'
</pre>
