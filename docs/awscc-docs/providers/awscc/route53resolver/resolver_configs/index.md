---
title: resolver_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_configs
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
Retrieves a list of <code>resolver_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolver_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resolver_configs</code> resource, the following permissions are required:

### Create
<pre>
route53resolver:UpdateResolverConfig,
route53resolver:GetResolverConfig,
ec2:DescribeVpcs</pre>

### List
<pre>
route53resolver:ListResolverConfigs,
ec2:DescribeVpcs</pre>


## Example
```sql
SELECT
region,
resource_id
FROM awscc.route53resolver.resolver_configs
WHERE region = 'us-east-1'
```
