---
title: model_card
hide_title: false
hide_table_of_contents: false
keywords:
  - model_card
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>model_card</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_card</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_card</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.model_card</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>model_card_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the successfully created model card.</td></tr>
<tr><td><code>model_card_version</code></td><td><code>integer</code></td><td>A version of the model card.</td></tr>
<tr><td><code>model_card_name</code></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
<tr><td><code>security_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_card_status</code></td><td><code>string</code></td><td>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</td></tr>
<tr><td><code>content</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The date and time the model card was created.</td></tr>
<tr><td><code>created_by</code></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td>The date and time the model card was last modified.</td></tr>
<tr><td><code>last_modified_by</code></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><code>model_card_processing_status</code></td><td><code>string</code></td><td>The processing status of model card deletion. The ModelCardProcessingStatus updates throughout the different deletion steps.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Key-value pairs used to manage metadata for model cards.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
model_card_arn,
model_card_version,
model_card_name,
security_config,
model_card_status,
content,
creation_time,
created_by,
last_modified_time,
last_modified_by,
model_card_processing_status,
tags
FROM awscc.sagemaker.model_card
WHERE region = 'us-east-1'
AND data__Identifier = '{ModelCardName}';
```

## Permissions

To operate on the <code>model_card</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeModelCard,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
kms:Decrypt,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateModelCard,
sagemaker:DescribeModelCard,
kms:GenerateDataKey,
kms:Decrypt,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DescribeModelCard,
sagemaker:DeleteModelCard,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
kms:RetireGrant,
kms:Decrypt,
sagemaker:ListTags,
sagemaker:DeleteTags
```

