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
<tr><td><b>Id</b></td><td><code>awscc.iot.ca_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ca_certificate_pem</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>verification_certificate_pem</code></td><td><code>string</code></td><td>The private key verification certificate.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_registration_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>remove_auto_registration</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>registration_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ca_certificate_pem,
verification_certificate_pem,
status,
certificate_mode,
auto_registration_status,
remove_auto_registration,
registration_config,
id,
arn,
tags
FROM awscc.iot.ca_certificate
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>ca_certificate</code> resource, the following permissions are required:

### Read
```json
iot:DescribeCACertificate,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateCACertificate,
iot:DescribeCACertificate,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:UpdateCACertificate,
iot:DeleteCACertificate,
iot:DescribeCACertificate
```

