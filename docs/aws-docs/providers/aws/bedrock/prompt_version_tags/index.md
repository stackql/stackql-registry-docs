---
title: prompt_version_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt_version_tags
  - bedrock
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

Expands all tag keys and values for <code>prompt_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt_version_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::PromptVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.prompt_version_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>ARN of a prompt resource possibly with a version</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of a prompt version resource</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="prompt_id" /></td><td><code>string</code></td><td>Identifier for a Prompt</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Version.</td></tr>
<tr><td><CopyableCode code="variants" /></td><td><code>array</code></td><td>List of prompt variants</td></tr>
<tr><td><CopyableCode code="default_variant" /></td><td><code>string</code></td><td>Name for a variant.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for a prompt version resource.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for a prompt resource.</td></tr>
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
Expands tags for all <code>prompt_versions</code> in a region.
```sql
SELECT
region,
prompt_arn,
arn,
created_at,
prompt_id,
updated_at,
version,
variants,
default_variant,
description,
customer_encryption_key_arn,
name,
tag_key,
tag_value
FROM aws.bedrock.prompt_version_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>prompt_version_tags</code> resource, see <a href="/providers/aws/bedrock/prompt_versions/#permissions"><code>prompt_versions</code></a>

