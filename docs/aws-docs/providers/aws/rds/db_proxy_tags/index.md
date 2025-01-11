---
title: db_proxy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>db_proxies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auth" /></td><td><code>array</code></td><td>The authorization mechanism that the proxy uses.</td></tr>
<tr><td><CopyableCode code="db_proxy_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the proxy.</td></tr>
<tr><td><CopyableCode code="db_proxy_name" /></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="debug_logging" /></td><td><code>boolean</code></td><td>Whether the proxy includes detailed information about SQL statements in its logs.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><CopyableCode code="engine_family" /></td><td><code>string</code></td><td>The kinds of databases that the proxy can connect to.</td></tr>
<tr><td><CopyableCode code="idle_client_timeout" /></td><td><code>integer</code></td><td>The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.</td></tr>
<tr><td><CopyableCode code="require_tls" /></td><td><code>boolean</code></td><td>A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>VPC security group IDs to associate with the new proxy.</td></tr>
<tr><td><CopyableCode code="vpc_subnet_ids" /></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new proxy.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>db_proxies</code> in a region.
```sql
SELECT
region,
auth,
db_proxy_arn,
db_proxy_name,
debug_logging,
endpoint,
engine_family,
idle_client_timeout,
require_tls,
role_arn,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids,
tag_key,
tag_value
FROM aws.rds.db_proxy_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_proxy_tags</code> resource, see <a href="/providers/aws/rds/db_proxies/#permissions"><code>db_proxies</code></a>

