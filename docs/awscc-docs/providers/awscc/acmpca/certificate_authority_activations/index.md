---
title: certificate_authority_activations
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority_activations
  - acmpca
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>certificate_authority_activations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority_activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate_authority_activations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.acmpca.certificate_authority_activations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td>Arn of the Certificate Authority.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>certificate_authority_activations</code> resource, the following permissions are required:

### Create
<pre>
acm-pca:ImportCertificateAuthorityCertificate,
acm-pca:UpdateCertificateAuthority</pre>


## Example
```sql
SELECT
region,
certificate_authority_arn
FROM awscc.acmpca.certificate_authority_activations
WHERE region = 'us-east-1'
```