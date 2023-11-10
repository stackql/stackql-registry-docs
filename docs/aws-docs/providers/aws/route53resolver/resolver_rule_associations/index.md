---
title: resolver_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_rule_associations
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
Retrieves a list of <code>resolver_rule_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_rule_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_rule_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resolver_rule_association_id</code></td><td><code>string</code></td><td>Primary Identifier for Resolver Rule Association</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resolver_rule_association_id
FROM aws.route53resolver.resolver_rule_associations
WHERE region = 'us-east-1'
```
