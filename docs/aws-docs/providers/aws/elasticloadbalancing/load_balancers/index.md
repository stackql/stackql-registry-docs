---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - elasticloadbalancing
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>load_balancers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>load_balancers</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancing.load_balancers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SecurityGroups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ConnectionDrainingPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Scheme</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SourceSecurityGroupOwnerAlias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HealthCheck</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CanonicalHostedZoneNameID</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CanonicalHostedZoneName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DNSName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AccessLoggingPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Instances</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LoadBalancerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Listeners</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CrossZone</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>AppCookieStickinessPolicy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LBCookieStickinessPolicy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SourceSecurityGroupGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConnectionSettings</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.elasticloadbalancing.load_balancers<br/>WHERE region = 'us-east-1'
</pre>
