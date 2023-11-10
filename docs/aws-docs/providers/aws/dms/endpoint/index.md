---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - dms
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
<tr><td><b>Id</b></td><td><code>aws.dms.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sybase_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>redis_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>oracle_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kafka_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>my_sql_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s3_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kinesis_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ssl_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>redshift_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>endpoint_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mongo_db_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ibm_db2_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>external_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>neptune_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>elasticsearch_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>engine_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>doc_db_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dynamo_db_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>microsoft_sql_server_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>gcp_my_sq_lsettings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>server_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>extra_connection_attributes</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>postgre_sql_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
sybase_settings,
redis_settings,
oracle_settings,
kafka_settings,
port,
my_sql_settings,
s3_settings,
resource_identifier,
kinesis_settings,
ssl_mode,
redshift_settings,
endpoint_type,
tags,
password,
mongo_db_settings,
ibm_db2_settings,
kms_key_id,
external_id,
database_name,
neptune_settings,
elasticsearch_settings,
engine_name,
doc_db_settings,
dynamo_db_settings,
username,
microsoft_sql_server_settings,
gcp_my_sq_lsettings,
server_name,
extra_connection_attributes,
id,
endpoint_identifier,
certificate_arn,
postgre_sql_settings
FROM aws.dms.endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
