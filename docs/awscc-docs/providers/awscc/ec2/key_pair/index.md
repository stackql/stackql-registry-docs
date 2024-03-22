---
title: key_pair
hide_title: false
hide_table_of_contents: false
keywords:
  - key_pair
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>key_pair</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_pair</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_pair</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.key_pair</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td>The name of the SSH key pair</td></tr>
<tr><td><code>key_type</code></td><td><code>string</code></td><td>The crypto-system used to generate a key pair.</td></tr>
<tr><td><code>key_format</code></td><td><code>string</code></td><td>The format of the private key</td></tr>
<tr><td><code>public_key_material</code></td><td><code>string</code></td><td>Plain text public key to import</td></tr>
<tr><td><code>key_fingerprint</code></td><td><code>string</code></td><td>A short sequence of bytes used for public key verification</td></tr>
<tr><td><code>key_pair_id</code></td><td><code>string</code></td><td>An AWS generated ID for the key pair</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
key_name,
key_type,
key_format,
public_key_material,
key_fingerprint,
key_pair_id,
tags
FROM awscc.ec2.key_pair
WHERE data__Identifier = '<KeyName>';
```

## Permissions

To operate on the <code>key_pair</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeKeyPairs
```

### Delete
```json
ec2:DeleteKeyPair,
ssm:DeleteParameter,
ec2:DescribeKeyPairs
```

