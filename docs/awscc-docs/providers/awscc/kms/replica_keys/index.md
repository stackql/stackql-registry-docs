---
title: replica_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_keys
  - kms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>replica_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replica_keys</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kms.replica_keys</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>replica_keys</code> resource, the following permissions are required:

### Create
<pre>
kms:ReplicateKey,
kms:CreateKey,
kms:DescribeKey,
kms:DisableKey,
kms:TagResource</pre>

### List
<pre>
kms:ListKeys,
kms:DescribeKey</pre>


## Example
```sql
SELECT
region,
key_id
FROM awscc.kms.replica_keys
WHERE region = 'us-east-1'
```