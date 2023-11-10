---
title: agent
hide_title: false
hide_table_of_contents: false
keywords:
  - agent
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
Gets an individual <code>agent</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>agent</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.agent</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>agent_name</code></td><td><code>string</code></td><td>The name configured for the agent. Text reference used to identify the agent in the console.</td></tr>
<tr><td><code>activation_key</code></td><td><code>string</code></td><td>Activation key of the Agent.</td></tr>
<tr><td><code>security_group_arns</code></td><td><code>array</code></td><td>The ARNs of the security group used to protect your data transfer task subnets.</td></tr>
<tr><td><code>subnet_arns</code></td><td><code>array</code></td><td>The ARNs of the subnets in which DataSync will create elastic network interfaces for each data transfer task.</td></tr>
<tr><td><code>vpc_endpoint_id</code></td><td><code>string</code></td><td>The ID of the VPC endpoint that the agent has access to.</td></tr>
<tr><td><code>endpoint_type</code></td><td><code>string</code></td><td>The service endpoints that the agent will connect to.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>agent_arn</code></td><td><code>string</code></td><td>The DataSync Agent ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
agent_name,
activation_key,
security_group_arns,
subnet_arns,
vpc_endpoint_id,
endpoint_type,
tags,
agent_arn
FROM aws.datasync.agent
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AgentArn&gt;'
```
