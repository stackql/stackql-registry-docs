---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
Gets an individual <code>certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>usage</code></td><td><code>string</code></td><td>Specifies the usage type for the certificate.</td></tr>
<tr><td><code>certificate</code></td><td><code>string</code></td><td>Specifies the certificate body to be imported.</td></tr>
<tr><td><code>certificate_chain</code></td><td><code>string</code></td><td>Specifies the certificate chain to be imported.</td></tr>
<tr><td><code>private_key</code></td><td><code>string</code></td><td>Specifies the private key for the certificate.</td></tr>
<tr><td><code>active_date</code></td><td><code>string</code></td><td>Specifies the active date for the certificate.</td></tr>
<tr><td><code>inactive_date</code></td><td><code>string</code></td><td>Specifies the inactive date for the certificate.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A textual description for the certificate.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
<tr><td><code>certificate_id</code></td><td><code>string</code></td><td>A unique identifier for the certificate.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>A status description for the certificate.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Describing the type of certificate. With or without a private key.</td></tr>
<tr><td><code>serial</code></td><td><code>string</code></td><td>Specifies Certificate's serial.</td></tr>
<tr><td><code>not_before_date</code></td><td><code>string</code></td><td>Specifies the not before date for the certificate.</td></tr>
<tr><td><code>not_after_date</code></td><td><code>string</code></td><td>Specifies the not after date for the certificate.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
usage,
certificate,
certificate_chain,
private_key,
active_date,
inactive_date,
description,
tags,
arn,
certificate_id,
status,
type,
serial,
not_before_date,
not_after_date
FROM aws.transfer.certificate
WHERE region = 'us-east-1'
AND data__Identifier = '<CertificateId>'
```
