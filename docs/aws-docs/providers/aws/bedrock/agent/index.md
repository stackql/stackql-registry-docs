---
title: agent
hide_title: false
hide_table_of_contents: false
keywords:
  - agent
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

Gets or operates on an individual <code>agent</code> resource, use <code>agents</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::Agent Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.agent" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="action_groups" /></td><td><code>array</code></td><td>List of ActionGroups</td></tr>
<tr><td><CopyableCode code="agent_arn" /></td><td><code>string</code></td><td>Arn representation of the Agent.</td></tr>
<tr><td><CopyableCode code="agent_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="agent_name" /></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><CopyableCode code="agent_resource_role_arn" /></td><td><code>string</code></td><td>ARN of a IAM role.</td></tr>
<tr><td><CopyableCode code="agent_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="agent_version" /></td><td><code>string</code></td><td>Draft Agent Version.</td></tr>
<tr><td><CopyableCode code="auto_prepare" /></td><td><code>boolean</code></td><td>Specifies whether to automatically prepare after creating or updating the agent.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="skip_resource_in_use_check_on_delete" /></td><td><code>boolean</code></td><td>Specifies whether to allow deleting agent while it is in use.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>Failure Reasons for Error.</td></tr>
<tr><td><CopyableCode code="foundation_model" /></td><td><code>string</code></td><td>ARN or name of a Bedrock model.</td></tr>
<tr><td><CopyableCode code="idle_session_ttl_in_seconds" /></td><td><code>number</code></td><td>Max Session Time.</td></tr>
<tr><td><CopyableCode code="instruction" /></td><td><code>string</code></td><td>Instruction for the agent.</td></tr>
<tr><td><CopyableCode code="knowledge_bases" /></td><td><code>array</code></td><td>List of Agent Knowledge Bases</td></tr>
<tr><td><CopyableCode code="prepared_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="prompt_override_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="recommended_actions" /></td><td><code>array</code></td><td>The recommended actions users can take to resolve an error in failureReasons.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
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
idle_session_ttl_in_seconds,
instruction,
knowledge_bases,
prepared_at,
prompt_override_configuration,
recommended_actions,
tags,
updated_at
FROM aws.bedrock.agent
WHERE data__Identifier = '<AgentId>';
```

## Permissions

To operate on the <code>agent</code> resource, the following permissions are required:

### Read
```json
bedrock:GetAgent,
bedrock:GetAgentActionGroup,
bedrock:ListAgentActionGroups,
bedrock:GetAgentKnowledgeBase,
bedrock:ListAgentKnowledgeBases,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:GetAgent,
bedrock:UpdateAgent,
bedrock:PrepareAgent,
bedrock:GetAgentKnowledgeBase,
bedrock:UpdateAgentKnowledgeBase,
bedrock:AssociateAgentKnowledgeBase,
bedrock:DisassociateAgentKnowledgeBase,
bedrock:ListAgentKnowledgeBases,
bedrock:CreateAgentActionGroup,
bedrock:GetAgentActionGroup,
bedrock:UpdateAgentActionGroup,
bedrock:DeleteAgentActionGroup,
bedrock:ListAgentActionGroups,
bedrock:TagResource,
bedrock:UntagResource,
bedrock:ListTagsForResource,
iam:PassRole
```

### Delete
```json
bedrock:GetAgent,
bedrock:DeleteAgent
```
