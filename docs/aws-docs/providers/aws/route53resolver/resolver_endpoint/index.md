---
title: resolver_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_endpoint
  - route53resolver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resolver_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IpAddresses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResolverEndpointId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IpAddressCount</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OutpostArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PreferredInstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResolverEndpointType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Direction</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HostVPCId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53resolver.resolver_endpoint
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ResolverEndpointId&gt;'
</pre>
