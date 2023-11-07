---
title: static_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - static_ips
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>static_ips</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>static_ips</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.static_ips</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>StaticIpName</code></td><td><code>string</code></td><td>The name of the static IP address.</td></tr>
<tr><td><code>AttachedTo</code></td><td><code>string</code></td><td>The instance where the static IP is attached.</td></tr>
<tr><td><code>IsAttached</code></td><td><code>boolean</code></td><td>A Boolean value indicating whether the static IP is attached.</td></tr>
<tr><td><code>IpAddress</code></td><td><code>string</code></td><td>The static IP address.</td></tr>
<tr><td><code>StaticIpArn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lightsail.static_ips<br/>WHERE region = 'us-east-1'
</pre>
