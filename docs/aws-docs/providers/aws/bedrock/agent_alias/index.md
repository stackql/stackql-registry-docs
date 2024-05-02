---
title: agent_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_alias
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
Gets an individual <code>agent_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::AgentAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bedrock.agent_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>agent_alias_arn</code></td><td><code>string</code></td><td>Arn representation of the Agent Alias.</td></tr>
<tr><td><code>agent_alias_history_events</code></td><td><code>array</code></td><td>The list of history events for an alias for an Agent.</td></tr>
<tr><td><code>agent_alias_id</code></td><td><code>string</code></td><td>Id for an Agent Alias generated at the server side.</td></tr>
<tr><td><code>agent_alias_name</code></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><code>agent_alias_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>agent_id</code></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><code>routing_configuration</code></td><td><code>array</code></td><td>Routing configuration for an Agent alias.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
agent_alias_arn,
agent_alias_history_events,
agent_alias_id,
agent_alias_name,
agent_alias_status,
agent_id,
created_at,
description,
routing_configuration,
tags,
updated_at
FROM aws.bedrock.agent_alias
WHERE data__Identifier = '<AgentId>|<AgentAliasId>';
```

## Permissions

To operate on the <code>agent_alias</code> resource, the following permissions are required:

### Read
```json
bedrock:GetAgentAlias,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:PrepareAgent,
bedrock:GetAgent,
bedrock:UpdateAgentAlias,
bedrock:TagResource,
bedrock:UntagResource,
bedrock:GetAgentAlias,
bedrock:ListTagsForResource
```

### Delete
```json
bedrock:DeleteAgentAlias
```

