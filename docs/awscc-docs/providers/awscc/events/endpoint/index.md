---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - events
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>routing_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>replication_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>event_buses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>endpoint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
arn,
role_arn,
description,
routing_config,
replication_config,
event_buses,
endpoint_id,
endpoint_url,
state,
state_reason
FROM awscc.events.endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>endpoint</code> resource, the following permissions are required:

### Read
```json
events:DescribeEndpoint
```

### Update
```json
events:DescribeEndpoint,
events:UpdateEndpoint,
route53:GetHealthCheck,
iam:PassRole
```

### Delete
```json
events:DeleteEndpoint,
events:DescribeEndpoint
```

