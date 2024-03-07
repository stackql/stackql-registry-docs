---
title: db_proxy_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_endpoint
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
Gets an individual <code>db_proxy_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_proxy_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_proxy_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>d_bproxy_endpoint_name</code></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><code>d_bproxy_endpoint_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB proxy endpoint.</td></tr>
<tr><td><code>d_bproxy_name</code></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td>VPC security group IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>vpc_subnet_ids</code></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><code>target_role</code></td><td><code>string</code></td><td>A value that indicates whether the DB proxy endpoint can be used for read&#x2F;write or read-only operations.</td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td>A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read&#x2F;write capability. Other endpoints that you associate with the DB proxy can be either read&#x2F;write or read-only.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>db_proxy_endpoint</code> resource, the following permissions are required:

### Read
<pre>
rds:DescribeDBProxyEndpoints,
rds:ListTagsForResource</pre>

### Update
<pre>
rds:ModifyDBProxyEndpoint,
rds:AddTagsToResource,
rds:RemoveTagsFromResource</pre>

### Delete
<pre>
rds:DescribeDBProxyEndpoints,
rds:DeleteDBProxyEndpoint</pre>


## Example
```sql
SELECT
region,
d_bproxy_endpoint_name,
d_bproxy_endpoint_arn,
d_bproxy_name,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids,
endpoint,
target_role,
is_default,
tags
FROM awscc.rds.db_proxy_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DBProxyEndpointName&gt;'
```
