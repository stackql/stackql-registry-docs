---
title: agent_aliases_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_aliases_list_only
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

Lists <code>agent_aliases</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/agent_aliases/"><code>agent_aliases</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_aliases_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::AgentAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.agent_aliases_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="agent_alias_arn" /></td><td><code>string</code></td><td>Arn representation of the Agent Alias.</td></tr>
<tr><td><CopyableCode code="agent_alias_history_events" /></td><td><code>array</code></td><td>The list of history events for an alias for an Agent.</td></tr>
<tr><td><CopyableCode code="agent_alias_id" /></td><td><code>string</code></td><td>Id for an Agent Alias generated at the server side.</td></tr>
<tr><td><CopyableCode code="agent_alias_name" /></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><CopyableCode code="agent_alias_status" /></td><td><code>string</code></td><td>The statuses an Agent Alias can be in.</td></tr>
<tr><td><CopyableCode code="agent_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="routing_configuration" /></td><td><code>array</code></td><td>Routing configuration for an Agent alias.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>agent_aliases</code> in a region.
```sql
SELECT
region,
agent_id,
agent_alias_id
FROM aws.bedrock.agent_aliases_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>agent_aliases_list_only</code> resource, see <a href="/providers/aws/bedrock/agent_aliases/#permissions"><code>agent_aliases</code></a>


