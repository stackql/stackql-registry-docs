---
title: db_proxy_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_endpoints
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
Retrieves a list of <code>db_proxy_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_proxy_endpoints</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_proxy_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DBProxyEndpointName</code></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><code>DBProxyEndpointArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB proxy endpoint.</td></tr>
<tr><td><code>DBProxyName</code></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><code>VpcId</code></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td>VPC security group IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>VpcSubnetIds</code></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><code>Endpoint</code></td><td><code>string</code></td><td>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><code>TargetRole</code></td><td><code>string</code></td><td>A value that indicates whether the DB proxy endpoint can be used for read&#x2F;write or read-only operations.</td></tr>
<tr><td><code>IsDefault</code></td><td><code>boolean</code></td><td>A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read&#x2F;write capability. Other endpoints that you associate with the DB proxy can be either read&#x2F;write or read-only.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.rds.db_proxy_endpoints<br/>WHERE region = 'us-east-1'
</pre>
