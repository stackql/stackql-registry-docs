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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>db_proxy_endpoint</code> resource, use <code>db_proxy_endpoints</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyEndpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_proxy_endpoint_name" /></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="db_proxy_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="db_proxy_name" /></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>VPC security group IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_subnet_ids" /></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><CopyableCode code="target_role" /></td><td><code>string</code></td><td>A value that indicates whether the DB proxy endpoint can be used for read&#x2F;write or read-only operations.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read&#x2F;write capability. Other endpoints that you associate with the DB proxy can be either read&#x2F;write or read-only.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
db_proxy_endpoint_name,
db_proxy_endpoint_arn,
db_proxy_name,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids,
endpoint,
target_role,
is_default,
tags
FROM aws.rds.db_proxy_endpoint
WHERE data__Identifier = '<DBProxyEndpointName>';
```

## Permissions

To operate on the <code>db_proxy_endpoint</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBProxyEndpoints,
rds:ListTagsForResource
```

### Update
```json
rds:ModifyDBProxyEndpoint,
rds:AddTagsToResource,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DescribeDBProxyEndpoints,
rds:DeleteDBProxyEndpoint
```

