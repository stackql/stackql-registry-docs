---
title: resolver_query_logging_config_association
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_config_association
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
Gets an individual <code>resolver_query_logging_config_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_query_logging_config_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_query_logging_config_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>resolver_query_log_config_id</code></td><td><code>string</code></td><td>ResolverQueryLogConfigId</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationStatus</td></tr>
<tr><td><code>error</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationError</td></tr>
<tr><td><code>error_message</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationErrorMessage</td></tr>
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
resolver_query_log_config_id,
resource_id,
status,
error,
error_message,
creation_time
FROM aws.route53resolver.resolver_query_logging_config_association
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
