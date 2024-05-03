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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>document_classifier</code> resource, use <code>document_classifiers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_classifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Document Classifier enables training document classifier models.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.document_classifier" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_data_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="output_data_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="language_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="document_classifier_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="version_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="volume_kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.comprehend.document_classifier
WHERE data__Identifier = '<Arn>';
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

