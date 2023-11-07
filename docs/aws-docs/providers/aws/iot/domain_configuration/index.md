---
title: domain_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_configuration
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.domain_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainConfigurationName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AuthorizerConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServerCertificateArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ServiceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ValidationCertificateArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainConfigurationStatus</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServerCertificates</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iot.domain_configuration<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DomainConfigurationName&gt;'
</pre>
