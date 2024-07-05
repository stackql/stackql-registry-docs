---
title: model_card_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - model_card_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>model_cards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_card_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelCard.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_card_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="model_card_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the successfully created model card.</td></tr>
<tr><td><CopyableCode code="model_card_version" /></td><td><code>integer</code></td><td>A version of the model card.</td></tr>
<tr><td><CopyableCode code="model_card_name" /></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
<tr><td><CopyableCode code="security_config" /></td><td><code>object</code></td><td>An optional Key Management Service key to encrypt, decrypt, and re-encrypt model card content for regulated workloads with highly sensitive data.<br /></td></tr>
<tr><td><CopyableCode code="model_card_status" /></td><td><code>string</code></td><td>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The content of the model card.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the model card was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>The date and time the model card was last modified.</td></tr>
<tr><td><CopyableCode code="last_modified_by" /></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><CopyableCode code="model_card_processing_status" /></td><td><code>string</code></td><td>The processing status of model card deletion. The ModelCardProcessingStatus updates throughout the different deletion steps.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>model_cards</code> in a region.
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
tag_key,
tag_value
FROM aws.sagemaker.model_card_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>model_card_tags</code> resource, see <a href="/providers/aws/sagemaker/model_cards/#permissions"><code>model_cards</code></a>


