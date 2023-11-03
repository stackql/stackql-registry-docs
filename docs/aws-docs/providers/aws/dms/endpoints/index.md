---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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
Retrieves a list of <code>endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SybaseSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RedisSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>OracleSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KafkaSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>MySqlSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>S3Settings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>KinesisSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SslMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RedshiftSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EndpointType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Password</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MongoDbSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>IbmDb2Settings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExternalId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DatabaseName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NeptuneSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ElasticsearchSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EngineName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DocDbSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DynamoDbSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Username</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MicrosoftSqlServerSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>GcpMySQLSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ServerName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExtraConnectionAttributes</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EndpointIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PostgreSqlSettings</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.dms.endpoints
WHERE region = 'us-east-1'
```
