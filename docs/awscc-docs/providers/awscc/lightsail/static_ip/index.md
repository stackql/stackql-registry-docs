---
title: static_ip
hide_title: false
hide_table_of_contents: false
keywords:
  - static_ip
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
Gets an individual <code>static_ip</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_ip</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>static_ip</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.static_ip</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>static_ip_name</code></td><td><code>string</code></td><td>The name of the static IP address.</td></tr>
<tr><td><code>attached_to</code></td><td><code>string</code></td><td>The instance where the static IP is attached.</td></tr>
<tr><td><code>is_attached</code></td><td><code>boolean</code></td><td>A Boolean value indicating whether the static IP is attached.</td></tr>
<tr><td><code>ip_address</code></td><td><code>string</code></td><td>The static IP address.</td></tr>
<tr><td><code>static_ip_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>static_ip</code> resource, the following permissions are required:

### Read
<pre>
lightsail:GetStaticIp,
lightsail:GetStaticIps</pre>

### Update
<pre>
lightsail:AttachStaticIp,
lightsail:DetachStaticIp,
lightsail:GetInstance,
lightsail:GetStaticIp,
lightsail:GetStaticIps</pre>

### Delete
<pre>
lightsail:GetStaticIp,
lightsail:GetStaticIps,
lightsail:ReleaseStaticIp</pre>


## Example
```sql
SELECT
region,
static_ip_name,
attached_to,
is_attached,
ip_address,
static_ip_arn
FROM awscc.lightsail.static_ip
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StaticIpName&gt;'
```
