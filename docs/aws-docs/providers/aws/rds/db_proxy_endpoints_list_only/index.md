---
title: db_proxy_endpoints_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_endpoints_list_only
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

Lists <code>db_proxy_endpoints</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_proxy_endpoints/"><code>db_proxy_endpoints</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoints_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyEndpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_endpoints_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_proxy_endpoint_name" /></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
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
Lists all <code>db_proxy_endpoints</code> in a region.
```sql
SELECT
region,
db_proxy_endpoint_name
FROM aws.rds.db_proxy_endpoints_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_proxy_endpoints_list_only</code> resource, see <a href="/providers/aws/rds/db_proxy_endpoints/#permissions"><code>db_proxy_endpoints</code></a>

