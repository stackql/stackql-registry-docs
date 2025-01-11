---
title: agent_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_tags
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

Expands all tag keys and values for <code>agents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::Agent Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.agent_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action_groups" /></td><td><code>array</code></td><td>List of ActionGroups</td></tr>
<tr><td><CopyableCode code="agent_arn" /></td><td><code>string</code></td><td>Arn representation of the Agent.</td></tr>
<tr><td><CopyableCode code="agent_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="agent_name" /></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><CopyableCode code="agent_resource_role_arn" /></td><td><code>string</code></td><td>ARN of a IAM role.</td></tr>
<tr><td><CopyableCode code="agent_status" /></td><td><code>string</code></td><td>Schema Type for Action APIs.</td></tr>
<tr><td><CopyableCode code="agent_version" /></td><td><code>string</code></td><td>Draft Agent Version.</td></tr>
<tr><td><CopyableCode code="auto_prepare" /></td><td><code>boolean</code></td><td>Specifies whether to automatically prepare after creating or updating the agent.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="skip_resource_in_use_check_on_delete" /></td><td><code>boolean</code></td><td>Specifies whether to allow deleting agent while it is in use.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>Failure Reasons for Error.</td></tr>
<tr><td><CopyableCode code="foundation_model" /></td><td><code>string</code></td><td>ARN or name of a Bedrock model.</td></tr>
<tr><td><CopyableCode code="guardrail_configuration" /></td><td><code>object</code></td><td>Configuration for a guardrail</td></tr>
<tr><td><CopyableCode code="idle_session_ttl_in_seconds" /></td><td><code>number</code></td><td>Max Session Time.</td></tr>
<tr><td><CopyableCode code="instruction" /></td><td><code>string</code></td><td>Instruction for the agent.</td></tr>
<tr><td><CopyableCode code="knowledge_bases" /></td><td><code>array</code></td><td>List of Agent Knowledge Bases</td></tr>
<tr><td><CopyableCode code="prepared_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="prompt_override_configuration" /></td><td><code>object</code></td><td>Configuration for prompt override.</td></tr>
<tr><td><CopyableCode code="recommended_actions" /></td><td><code>array</code></td><td>The recommended actions users can take to resolve an error in failureReasons.</td></tr>
<tr><td><CopyableCode code="test_alias_tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
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
Expands tags for all <code>agents</code> in a region.
```sql
SELECT
region,
action_groups,
agent_arn,
agent_id,
agent_name,
agent_resource_role_arn,
agent_status,
agent_version,
auto_prepare,
created_at,
customer_encryption_key_arn,
skip_resource_in_use_check_on_delete,
description,
failure_reasons,
foundation_model,
guardrail_configuration,
idle_session_ttl_in_seconds,
instruction,
knowledge_bases,
prepared_at,
prompt_override_configuration,
recommended_actions,
test_alias_tags,
updated_at,
tag_key,
tag_value
FROM aws.bedrock.agent_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>agent_tags</code> resource, see <a href="/providers/aws/bedrock/agents/#permissions"><code>agents</code></a>

