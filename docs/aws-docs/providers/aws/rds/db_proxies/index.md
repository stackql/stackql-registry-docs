---
title: db_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxies
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>db_proxies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_proxies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Auth</code></td><td><code>array</code></td><td>The authorization mechanism that the proxy uses.</td></tr><tr><td><code>DBProxyArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the proxy.</td></tr><tr><td><code>DBProxyName</code></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr><tr><td><code>DebugLogging</code></td><td><code>boolean</code></td><td>Whether the proxy includes detailed information about SQL statements in its logs.</td></tr><tr><td><code>Endpoint</code></td><td><code>string</code></td><td>The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.</td></tr><tr><td><code>EngineFamily</code></td><td><code>string</code></td><td>The kinds of databases that the proxy can connect to.</td></tr><tr><td><code>IdleClientTimeout</code></td><td><code>integer</code></td><td>The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.</td></tr><tr><td><code>RequireTLS</code></td><td><code>boolean</code></td><td>A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.</td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy.</td></tr><tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td>VPC security group IDs to associate with the new proxy.</td></tr><tr><td><code>VpcSubnetIds</code></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new proxy.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.rds.db_proxies
WHERE region = 'us-east-1'
```
