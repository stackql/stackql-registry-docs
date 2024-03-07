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
<tr><td><b>Description</b></td><td>certificate</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_name</code></td><td><code>string</code></td><td>The name for the certificate.</td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for the certificate.</td></tr>
<tr><td><code>subject_alternative_names</code></td><td><code>array</code></td><td>An array of strings that specify the alternate domains (e.g., example2.com) and subdomains (e.g., blog.example.com) for the certificate.</td></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The validation status of the certificate.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_name,
domain_name,
subject_alternative_names,
certificate_arn,
status,
tags
FROM awscc.lightsail.certificate
WHERE region = 'us-east-1'
AND data__Identifier = '{CertificateName}';
```

## Permissions

To operate on the <code>certificate</code> resource, the following permissions are required:

### Read
```json
lightsail:GetCertificates
```

### Update
```json
lightsail:GetCertificates,
lightsail:TagResource,
lightsail:UntagResource
```

### Delete
```json
lightsail:DeleteCertificate,
lightsail:GetCertificates
```

