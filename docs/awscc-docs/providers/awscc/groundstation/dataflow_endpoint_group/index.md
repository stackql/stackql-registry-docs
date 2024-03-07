---
title: dataflow_endpoint_group
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoint_group
  - groundstation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dataflow_endpoint_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_endpoint_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataflow_endpoint_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.groundstation.dataflow_endpoint_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_details</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>contact_pre_pass_duration_seconds</code></td><td><code>integer</code></td><td>Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.</td></tr>
<tr><td><code>contact_post_pass_duration_seconds</code></td><td><code>integer</code></td><td>Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
endpoint_details,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
tags
FROM awscc.groundstation.dataflow_endpoint_group
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>dataflow_endpoint_group</code> resource, the following permissions are required:

### Read
```json
groundstation:GetDataflowEndpointGroup,
groundstation:ListTagsForResource
```

### Delete
```json
groundstation:DeleteDataflowEndpointGroup,
groundstation:GetDataflowEndpointGroup
```

