---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - transfer
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
<tr><td><b>Description</b></td><td>certificates</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Usage</code></td><td><code>string</code></td><td>Specifies the usage type for the certificate.</td></tr>
<tr><td><code>Certificate</code></td><td><code>string</code></td><td>Specifies the certificate body to be imported.</td></tr>
<tr><td><code>CertificateChain</code></td><td><code>string</code></td><td>Specifies the certificate chain to be imported.</td></tr>
<tr><td><code>PrivateKey</code></td><td><code>string</code></td><td>Specifies the private key for the certificate.</td></tr>
<tr><td><code>ActiveDate</code></td><td><code>string</code></td><td>Specifies the active date for the certificate.</td></tr>
<tr><td><code>InactiveDate</code></td><td><code>string</code></td><td>Specifies the inactive date for the certificate.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A textual description for the certificate.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
<tr><td><code>CertificateId</code></td><td><code>string</code></td><td>A unique identifier for the certificate.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>A status description for the certificate.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>Describing the type of certificate. With or without a private key.</td></tr>
<tr><td><code>Serial</code></td><td><code>string</code></td><td>Specifies Certificate's serial.</td></tr>
<tr><td><code>NotBeforeDate</code></td><td><code>string</code></td><td>Specifies the not before date for the certificate.</td></tr>
<tr><td><code>NotAfterDate</code></td><td><code>string</code></td><td>Specifies the not after date for the certificate.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.transfer.certificates
WHERE region = 'us-east-1'
</pre>
