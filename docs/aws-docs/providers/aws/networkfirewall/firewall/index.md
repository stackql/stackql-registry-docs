---
title: firewall
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall
  - networkfirewall
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>firewall</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.firewall</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FirewallName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FirewallArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>FirewallId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FirewallPolicyArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VpcId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetMappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DeleteProtection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>SubnetChangeProtection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>FirewallPolicyChangeProtection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EndpointIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.networkfirewall.firewall
WHERE region = 'us-east-1' AND data__Identifier = '&lt;FirewallArn&gt;'
</pre>
