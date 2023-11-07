---
title: task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task_definitions</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.task_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the new resource.</td></tr>
<tr><td><code>AutoCreateTasks</code></td><td><code>boolean</code></td><td>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.</td></tr>
<tr><td><code>Update</code></td><td><code>undefined</code></td><td>Information about the gateways to update.</td></tr>
<tr><td><code>LoRaWANUpdateGatewayTaskEntry</code></td><td><code>undefined</code></td><td>The list of task definitions.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
<tr><td><code>TaskDefinitionType</code></td><td><code>string</code></td><td>A filter to list only the wireless gateway task definitions that use this task definition type</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>TaskDefinition arn. Returned after successful create.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotwireless.task_definitions
WHERE region = 'us-east-1'
</pre>
