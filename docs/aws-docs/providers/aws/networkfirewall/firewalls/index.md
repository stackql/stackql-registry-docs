---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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
Retrieves a list of <code>firewalls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewalls</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.firewalls</code></td></tr>
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
SELECT *<br/>FROM aws.networkfirewall.firewalls<br/>WHERE region = 'us-east-1'
</pre>
