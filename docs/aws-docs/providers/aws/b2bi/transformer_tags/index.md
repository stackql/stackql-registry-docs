---
title: transformer_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - transformer_tags
  - b2bi
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

Expands all tag keys and values for <code>transformers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformer_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Transformer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.transformer_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="edi_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="file_format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_conversion" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="mapping" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="mapping_template" /></td><td><code>string</code></td><td>This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="output_conversion" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sample_document" /></td><td><code>string</code></td><td>This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.</td></tr>
<tr><td><CopyableCode code="sample_documents" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transformer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transformer_id" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>transformers</code> in a region.
```sql
SELECT
region,
created_at,
edi_type,
file_format,
input_conversion,
mapping,
mapping_template,
modified_at,
name,
output_conversion,
sample_document,
sample_documents,
status,
transformer_arn,
transformer_id,
tag_key,
tag_value
FROM aws.b2bi.transformer_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transformer_tags</code> resource, see <a href="/providers/aws/b2bi/transformers/#permissions"><code>transformers</code></a>

