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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>storage_lens</code> resource, use <code>storage_lens</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.storage_lens" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="storage_lens_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
storage_lens_configuration,
tags
FROM aws.s3.storage_lens
WHERE data__Identifier = '<StorageLensConfiguration/Id>';
```

## Permissions

To operate on the <code>storage_lens</code> resource, the following permissions are required:

### Read
```json
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging
```

### Update
```json
s3:PutStorageLensConfiguration,
s3:PutStorageLensConfigurationTagging,
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging,
organizations:DescribeOrganization,
organizations:ListAccounts,
organizations:ListAWSServiceAccessForOrganization,
organizations:ListDelegatedAdministrators,
iam:CreateServiceLinkedRole
```

### Delete
```json
s3:DeleteStorageLensConfiguration,
s3:DeleteStorageLensConfigurationTagging
```

