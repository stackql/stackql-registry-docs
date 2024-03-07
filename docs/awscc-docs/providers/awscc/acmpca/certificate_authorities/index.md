---
title: certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authorities
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
Retrieves a list of <code>certificate_authorities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate_authorities</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.acmpca.certificate_authorities</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>certificate_authorities</code> resource, the following permissions are required:

### Create
```json
acm-pca:CreateCertificateAuthority,
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr
```

### List
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr,
acm-pca:ListCertificateAuthorities,
acm-pca:ListTags
```


## Example
```sql
SELECT
region,
arn
FROM awscc.acmpca.certificate_authorities
WHERE region = 'us-east-1'
```
