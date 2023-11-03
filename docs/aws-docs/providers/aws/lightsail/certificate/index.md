---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
Gets an individual <code>certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CertificateName</code></td><td><code>string</code></td><td>The name for the certificate.</td></tr><tr><td><code>DomainName</code></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for the certificate.</td></tr><tr><td><code>SubjectAlternativeNames</code></td><td><code>array</code></td><td>An array of strings that specify the alternate domains (e.g., example2.com) and subdomains (e.g., blog.example.com) for the certificate.</td></tr><tr><td><code>CertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The validation status of the certificate.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lightsail.certificate
WHERE region = 'us-east-1' AND data__Identifier = '{CertificateName}'
</pre>
