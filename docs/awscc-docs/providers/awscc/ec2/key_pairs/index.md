---
title: key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - key_pairs
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
Retrieves a list of <code>key_pairs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_pairs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.key_pairs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td>The name of the SSH key pair</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
key_name
FROM awscc.ec2.key_pairs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>key_pairs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateKeyPair,
ec2:ImportKeyPair,
ec2:CreateTags,
ssm:PutParameter
```

### List
```json
ec2:DescribeKeyPairs
```

