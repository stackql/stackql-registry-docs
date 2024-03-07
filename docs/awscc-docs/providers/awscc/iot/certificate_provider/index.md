---
title: certificate_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_provider
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
Gets an individual <code>certificate_provider</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate_provider</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.certificate_provider</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lambda_function_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_default_for_operations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>certificate_provider</code> resource, the following permissions are required:

### Read
```json
iot:DescribeCertificateProvider,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateCertificateProvider,
iot:DescribeCertificateProvider,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteCertificateProvider,
iot:DescribeCertificateProvider
```


## Example
```sql
SELECT
region,
certificate_provider_name,
lambda_function_arn,
account_default_for_operations,
tags,
arn
FROM awscc.iot.certificate_provider
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;CertificateProviderName&gt;'
```
