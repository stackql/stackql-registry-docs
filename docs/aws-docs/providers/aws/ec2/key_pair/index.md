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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>key_pair</code> resource, use <code>key_pairs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_pair</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::KeyPair creates an SSH key pair</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.key_pair" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>The name of the SSH key pair</td></tr>
<tr><td><CopyableCode code="key_type" /></td><td><code>string</code></td><td>The crypto-system used to generate a key pair.</td></tr>
<tr><td><CopyableCode code="key_format" /></td><td><code>string</code></td><td>The format of the private key</td></tr>
<tr><td><CopyableCode code="public_key_material" /></td><td><code>string</code></td><td>Plain text public key to import</td></tr>
<tr><td><CopyableCode code="key_fingerprint" /></td><td><code>string</code></td><td>A short sequence of bytes used for public key verification</td></tr>
<tr><td><CopyableCode code="key_pair_id" /></td><td><code>string</code></td><td>An AWS generated ID for the key pair</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.key_pair
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
