---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - nimblestudio
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>studios</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>studios</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.nimblestudio.studios</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>studios</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
nimble:CreateStudio,
nimble:GetStudio,
nimble:TagResource,
sso:CreateManagedApplicationInstance,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### List
```json
nimble:ListStudios
```


## Example
```sql
SELECT
region,
studio_id
FROM awscc.nimblestudio.studios
WHERE region = 'us-east-1'
```
