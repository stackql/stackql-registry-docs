---
title: flow
hide_title: false
hide_table_of_contents: false
keywords:
  - flow
  - appflow
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appflow.flow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>flow_arn</code></td><td><code>string</code></td><td>ARN identifier of the flow.</td></tr>
<tr><td><code>flow_name</code></td><td><code>string</code></td><td>Name of the flow.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the flow.</td></tr>
<tr><td><code>k_ms_arn</code></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><code>trigger_config</code></td><td><code>object</code></td><td>Trigger settings of the flow.</td></tr>
<tr><td><code>source_flow_config</code></td><td><code>object</code></td><td>Configurations of Source connector of the flow.</td></tr>
<tr><td><code>destination_flow_config_list</code></td><td><code>array</code></td><td>List of Destination connectors of the flow.</td></tr>
<tr><td><code>tasks</code></td><td><code>array</code></td><td>List of tasks for the flow.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>List of Tags.</td></tr>
<tr><td><code>metadata_catalog_config</code></td><td><code>object</code></td><td>Configurations of metadata catalog of the flow.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
flow_arn,
flow_name,
description,
k_ms_arn,
trigger_config,
source_flow_config,
destination_flow_config_list,
tasks,
tags,
metadata_catalog_config
FROM aws.appflow.flow
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FlowName&gt;'
```
