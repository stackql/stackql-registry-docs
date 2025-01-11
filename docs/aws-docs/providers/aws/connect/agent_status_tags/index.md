---
title: agent_status_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_status_tags
  - connect
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

Expands all tag keys and values for <code>agent_statuses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_status_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::AgentStatus</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.agent_status_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="agent_status_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the agent status.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the status.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the status.</td></tr>
<tr><td><CopyableCode code="display_order" /></td><td><code>integer</code></td><td>The display order of the status.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the status.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of agent status.</td></tr>
<tr><td><CopyableCode code="reset_order_number" /></td><td><code>boolean</code></td><td>A number indicating the reset order of the agent status.</td></tr>
<tr><td><CopyableCode code="last_modified_region" /></td><td><code>string</code></td><td>Last modified region.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>number</code></td><td>Last modified time.</td></tr>
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
Expands tags for all <code>agent_statuses</code> in a region.
```sql
SELECT
region,
instance_arn,
agent_status_arn,
description,
name,
display_order,
state,
type,
reset_order_number,
last_modified_region,
last_modified_time,
tag_key,
tag_value
FROM aws.connect.agent_status_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>agent_status_tags</code> resource, see <a href="/providers/aws/connect/agent_statuses/#permissions"><code>agent_statuses</code></a>

