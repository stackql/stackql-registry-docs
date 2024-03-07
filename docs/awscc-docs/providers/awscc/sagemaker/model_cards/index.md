---
title: model_cards
hide_title: false
hide_table_of_contents: false
keywords:
  - model_cards
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
Retrieves a list of <code>model_cards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_cards</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.model_cards</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>model_card_name</code></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>model_cards</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelCard,
kms:DescribeKey,
kms:GenerateDataKey,
kms:CreateGrant,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
sagemaker:AddTags
```

### List
```json
sagemaker:ListModelCards,
sagemaker:ListModelCardVersions
```


## Example
```sql
SELECT
region,
model_card_name
FROM awscc.sagemaker.model_cards
WHERE region = 'us-east-1'
```
