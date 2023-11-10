---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_source</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>open_search_service_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_bridge_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>http_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>relational_database_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>lambda_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dynamo_db_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>elasticsearch_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
open_search_service_config,
description,
service_role_arn,
name,
data_source_arn,
type,
event_bridge_config,
http_config,
relational_database_config,
lambda_config,
id,
api_id,
dynamo_db_config,
elasticsearch_config
FROM aws.appsync.data_source
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
