---
title: key_signing_key
hide_title: false
hide_table_of_contents: false
keywords:
  - key_signing_key
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>key_signing_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_signing_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_signing_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.key_signing_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.</td></tr>
<tr><td><code>key_management_service_arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
hosted_zone_id,
status,
name,
key_management_service_arn
FROM awscc.route53.key_signing_key
WHERE data__Identifier = '<HostedZoneId>|<Name>';
```

## Permissions

To operate on the <code>key_signing_key</code> resource, the following permissions are required:

### Read
```json
route53:GetDNSSEC
```

### Update
```json
route53:GetDNSSEC,
route53:ActivateKeySigningKey,
route53:DeactivateKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### Delete
```json
route53:DeactivateKeySigningKey,
route53:DeleteKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

