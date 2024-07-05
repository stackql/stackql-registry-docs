---
title: agents_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - agents_list_only
  - datasync
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

Lists <code>agents</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/agents/"><code>agents</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Agent.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.agents_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="agent_name" /></td><td><code>string</code></td><td>The name configured for the agent. Text reference used to identify the agent in the console.</td></tr>
<tr><td><CopyableCode code="activation_key" /></td><td><code>string</code></td><td>Activation key of the Agent.</td></tr>
<tr><td><CopyableCode code="security_group_arns" /></td><td><code>array</code></td><td>The ARNs of the security group used to protect your data transfer task subnets.</td></tr>
<tr><td><CopyableCode code="subnet_arns" /></td><td><code>array</code></td><td>The ARNs of the subnets in which DataSync will create elastic network interfaces for each data transfer task.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint_id" /></td><td><code>string</code></td><td>The ID of the VPC endpoint that the agent has access to.</td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td>The service endpoints that the agent will connect to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="agent_arn" /></td><td><code>string</code></td><td>The DataSync Agent ARN.</td></tr>
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
Lists all <code>agents</code> in a region.
```sql
SELECT
region,
agent_arn
FROM aws.datasync.agents_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>agents_list_only</code> resource, see <a href="/providers/aws/datasync/agents/#permissions"><code>agents</code></a>


