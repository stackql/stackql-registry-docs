---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - omics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workflows</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.omics.workflows</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.omics.workflows
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>workflows</code> resource, the following permissions are required:

### Create
```json
omics:CreateWorkflow,
omics:GetWorkflow,
omics:TagResource,
s3:PutObject,
s3:GetObject,
s3:GetObjectAttributes,
s3:HeadObject,
s3:GetEncryptionConfiguration,
kms:Decrypt,
kms:GenerateDataKey,
kms:GenerateDataKeyPair,
kms:GenerateDataKeyPairWithoutPlaintext,
kms:GenerateDataKeyWithoutPlaintext
```

### List
```json
omics:ListWorkflows
```

