---
title: ca_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificate
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
Gets an individual <code>ca_certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ca_certificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.ca_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CACertificatePem</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VerificationCertificatePem</code></td><td><code>string</code></td><td>The private key verification certificate.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CertificateMode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutoRegistrationStatus</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RemoveAutoRegistration</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>RegistrationConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iot.ca_certificate<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
