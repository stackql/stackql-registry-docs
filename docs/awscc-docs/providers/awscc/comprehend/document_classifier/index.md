---
title: document_classifier
hide_title: false
hide_table_of_contents: false
keywords:
  - document_classifier
  - comprehend
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>document_classifier</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_classifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>document_classifier</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.comprehend.document_classifier</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>data_access_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>input_data_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>output_data_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>language_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>document_classifier_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>version_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volume_kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
data_access_role_arn,
input_data_config,
output_data_config,
language_code,
model_kms_key_id,
model_policy,
document_classifier_name,
mode,
tags,
version_name,
volume_kms_key_id,
vpc_config,
arn
FROM awscc.comprehend.document_classifier
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>document_classifier</code> resource, the following permissions are required:

### Read
```json
comprehend:DescribeDocumentClassifier,
comprehend:DescribeResourcePolicy,
comprehend:ListTagsForResource
```

### Update
```json
iam:PassRole,
comprehend:PutResourcePolicy,
comprehend:DeleteResourcePolicy,
comprehend:DescribeResourcePolicy,
comprehend:DescribeDocumentClassifier,
comprehend:ListTagsForResource,
comprehend:TagResource,
comprehend:UntagResource
```

### Delete
```json
comprehend:DescribeDocumentClassifier,
comprehend:DeleteDocumentClassifier
```

