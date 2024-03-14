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
Gets an individual <code>resolver_query_logging_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_query_logging_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolver_query_logging_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.</td></tr>
<tr><td><code>share_status</code></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><code>association_count</code></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>ResolverQueryLogConfigName</td></tr>
<tr><td><code>creator_request_id</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>destination_arn</code></td><td><code>string</code></td><td>destination arn</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.route53resolver.resolver_query_logging_config
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

