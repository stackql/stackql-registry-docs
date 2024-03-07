---
title: resolver_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_rules
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
Retrieves a list of <code>resolver_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_rules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolver_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resolver_rule_id</code></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resolver_rules</code> resource, the following permissions are required:

### Create
<pre>
route53resolver:CreateResolverRule,
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource,
route53resolver:TagResource</pre>

### List
<pre>
route53resolver:ListResolverRules</pre>


## Example
```sql
SELECT
region,
resolver_rule_id
FROM awscc.route53resolver.resolver_rules
WHERE region = 'us-east-1'
```
