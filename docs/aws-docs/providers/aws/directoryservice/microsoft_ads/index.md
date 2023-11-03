---
title: microsoft_ads
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_ads
  - directoryservice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>microsoft_ads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.directoryservice.microsoft_ads</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Alias</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DnsIpAddresses</code></td><td><code>array</code></td><td></td></tr><tr><td><code>CreateAlias</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Edition</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EnableSso</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Password</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ShortName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VpcSettings</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.directoryservice.microsoft_ads
WHERE region = 'us-east-1'
</pre>
