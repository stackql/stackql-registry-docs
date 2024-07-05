---
title: knowledge_bases_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases_list_only
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

Lists <code>knowledge_bases</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/knowledge_bases/"><code>knowledge_bases</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.knowledge_bases_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="knowledge_base_configuration" /></td><td><code>object</code></td><td>Contains details about the embeddings model used for the knowledge base.</td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td>The unique identifier of the knowledge base.</td></tr>
<tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td>The ARN of the knowledge base.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the knowledge base.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of a knowledge base.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role with permissions to invoke API operations on the knowledge base. The ARN must begin with AmazonBedrockExecutionRoleForKnowledgeBase_</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was created.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>A list of reasons that the API operation on the knowledge base failed.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
<tr><td><CopyableCode code="storage_configuration" /></td><td><code>object</code></td><td>The vector store service in which the knowledge base is stored.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
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
Lists all <code>knowledge_bases</code> in a region.
```sql
SELECT
region,
knowledge_base_id
FROM aws.bedrock.knowledge_bases_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>knowledge_bases_list_only</code> resource, see <a href="/providers/aws/bedrock/knowledge_bases/#permissions"><code>knowledge_bases</code></a>


