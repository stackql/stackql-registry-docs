---
title: api_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - api_destination
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
Gets an individual <code>api_destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.api_destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the apiDestination.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_arn</code></td><td><code>string</code></td><td>The arn of the connection.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The arn of the api destination.</td></tr>
<tr><td><code>invocation_rate_limit_per_second</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>invocation_endpoint</code></td><td><code>string</code></td><td>Url endpoint to invoke.</td></tr>
<tr><td><code>http_method</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
connection_arn,
arn,
invocation_rate_limit_per_second,
invocation_endpoint,
http_method
FROM awscc.events.api_destination
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>api_destination</code> resource, the following permissions are required:

### Read
```json
events:DescribeApiDestination
```

### Update
```json
events:UpdateApiDestination,
events:DescribeApiDestination
```

### Delete
```json
events:DeleteApiDestination,
events:DescribeApiDestination
```

