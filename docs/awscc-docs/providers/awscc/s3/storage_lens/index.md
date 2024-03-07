---
title: storage_lens
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_lens
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>storage_lens</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>storage_lens</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.storage_lens</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>storage_lens_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>storage_lens</code> resource, the following permissions are required:

### Read
<pre>
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging</pre>

### Update
<pre>
s3:PutStorageLensConfiguration,
s3:PutStorageLensConfigurationTagging,
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging,
organizations:DescribeOrganization,
organizations:ListAccounts,
organizations:ListAWSServiceAccessForOrganization,
organizations:ListDelegatedAdministrators,
iam:CreateServiceLinkedRole</pre>

### Delete
<pre>
s3:DeleteStorageLensConfiguration,
s3:DeleteStorageLensConfigurationTagging</pre>


## Example
```sql
SELECT
region,
storage_lens_configuration,
tags
FROM awscc.s3.storage_lens
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StorageLensConfiguration/Id&gt;'
```
