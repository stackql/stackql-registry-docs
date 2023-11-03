---
title: ca_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificates
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
Retrieves a list of <code>ca_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iot.ca_certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CACertificatePem</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VerificationCertificatePem</code></td><td><code>string</code></td><td>The private key verification certificate.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CertificateMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutoRegistrationStatus</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RemoveAutoRegistration</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>RegistrationConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.ca_certificates
WHERE region = 'us-east-1'
</pre>
