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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>model_cards</code> in a region or create a <code>model_cards</code> resource, use <code>model_card</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelCard.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_cards" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="model_card_name" /></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
model_card_name
FROM aws.sagemaker.model_cards
WHERE region = 'us-east-1'
```

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

