---
title: domain_names
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_names
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>domain_names</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_names</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.domain_names</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MutualTlsAuthentication</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RegionalHostedZoneId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RegionalDomainName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainNameConfigurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigatewayv2.domain_names<br/>WHERE region = 'us-east-1'
</pre>
