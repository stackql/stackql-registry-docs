---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - certificatemanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.certificatemanager.certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CertificateAuthorityArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DomainValidationOptions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>CertificateTransparencyLoggingPreference</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ValidationMethod</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SubjectAlternativeNames</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.certificatemanager.certificates
WHERE region = 'us-east-1'
</pre>
