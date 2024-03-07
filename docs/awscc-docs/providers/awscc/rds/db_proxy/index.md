---
title: db_proxy
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy
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
Gets an individual <code>db_proxy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_proxy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_proxy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auth</code></td><td><code>array</code></td><td>The authorization mechanism that the proxy uses.</td></tr>
<tr><td><code>d_bproxy_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the proxy.</td></tr>
<tr><td><code>d_bproxy_name</code></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><code>debug_logging</code></td><td><code>boolean</code></td><td>Whether the proxy includes detailed information about SQL statements in its logs.</td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td>The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><code>engine_family</code></td><td><code>string</code></td><td>The kinds of databases that the proxy can connect to.</td></tr>
<tr><td><code>idle_client_timeout</code></td><td><code>integer</code></td><td>The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.</td></tr>
<tr><td><code>require_tl_s</code></td><td><code>boolean</code></td><td>A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy.</td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td>VPC security group IDs to associate with the new proxy.</td></tr>
<tr><td><code>vpc_subnet_ids</code></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new proxy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>db_proxy</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBProxies
```

### Update
```json
rds:ModifyDBProxy,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
iam:PassRole
```

### Delete
```json
rds:DescribeDBProxies,
rds:DeleteDBProxy
```


## Example
```sql
SELECT
region,
auth,
d_bproxy_arn,
d_bproxy_name,
debug_logging,
endpoint,
engine_family,
idle_client_timeout,
require_tl_s,
role_arn,
tags,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids
FROM awscc.rds.db_proxy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DBProxyName&gt;'
```
