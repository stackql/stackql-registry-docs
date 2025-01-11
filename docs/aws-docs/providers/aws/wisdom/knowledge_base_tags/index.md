---
title: knowledge_base_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_base_tags
  - wisdom
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

Expands all tag keys and values for <code>knowledge_bases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_base_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.knowledge_base_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rendering_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="vector_ingestion_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>knowledge_bases</code> in a region.
```sql
SELECT
region,
description,
knowledge_base_arn,
knowledge_base_id,
knowledge_base_type,
name,
rendering_configuration,
server_side_encryption_configuration,
source_configuration,
vector_ingestion_configuration,
tag_key,
tag_value
FROM aws.wisdom.knowledge_base_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>knowledge_base_tags</code> resource, see <a href="/providers/aws/wisdom/knowledge_bases/#permissions"><code>knowledge_bases</code></a>

