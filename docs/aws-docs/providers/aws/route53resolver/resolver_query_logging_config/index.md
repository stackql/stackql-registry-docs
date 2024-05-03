---
title: resolver_query_logging_config
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_config
  - route53resolver
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

Gets or operates on an individual <code>resolver_query_logging_config</code> resource, use <code>resolver_query_logging_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_config" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.</td></tr>
<tr><td><CopyableCode code="share_status" /></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><CopyableCode code="association_count" /></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>ResolverQueryLogConfigName</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td>destination arn</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
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
id,
owner_id,
status,
share_status,
association_count,
arn,
name,
creator_request_id,
destination_arn,
creation_time
FROM aws.route53resolver.resolver_query_logging_config
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>resolver_query_logging_config</code> resource, the following permissions are required:

### Read
```json
resolverquerylogging:GetConfig,
route53resolver:GetResolverQueryLogConfig
```

### Delete
```json
resolverquerylogging:DeleteConfig,
resolverquerylogging:ListConfig,
route53resolver:DeleteResolverQueryLogConfig,
route53resolver:ListResolverQueryLogConfigs
```

