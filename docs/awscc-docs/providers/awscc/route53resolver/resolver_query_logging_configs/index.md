---
title: resolver_query_logging_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_configs
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
Retrieves a list of <code>resolver_query_logging_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_query_logging_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolver_query_logging_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resolver_query_logging_configs</code> resource, the following permissions are required:

### Create
<pre>
resolverquerylogging:CreateConfig,
resolverquerylogging:GetConfig,
route53resolver:CreateResolverQueryLogConfig,
route53resolver:GetResolverQueryLogConfig,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
resolverquerylogging:ListConfig,
route53resolver:ListResolverQueryLogConfigs</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.route53resolver.resolver_query_logging_configs
WHERE region = 'us-east-1'
```
