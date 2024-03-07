---
title: key_signing_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - key_signing_keys
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
Retrieves a list of <code>key_signing_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_signing_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_signing_keys</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.key_signing_keys</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
hosted_zone_id,
name
FROM awscc.route53.key_signing_keys

```

## Permissions

To operate on the <code>key_signing_keys</code> resource, the following permissions are required:

### Create
```json
route53:CreateKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### List
```json
route53:GetDNSSEC,
route53:ListHostedZones
```

