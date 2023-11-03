---
title: dnssec
hide_title: false
hide_table_of_contents: false
keywords:
  - dnssec
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dnssec</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dnssec</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.route53.dnssec</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>HostedZoneId</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53.dnssec
WHERE region = 'us-east-1' AND data__Identifier = '<HostedZoneId>'
</pre>
