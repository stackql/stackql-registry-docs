---
title: resolver_rule_association
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_rule_association
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
Gets an individual <code>resolver_rule_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_rule_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolver_rule_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC that you associated the Resolver rule with.</td></tr>
<tr><td><code>resolver_rule_id</code></td><td><code>string</code></td><td>The ID of the Resolver rule that you associated with the VPC that is specified by ``VPCId``.</td></tr>
<tr><td><code>resolver_rule_association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of an association between a Resolver rule and a VPC.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
vpc_id,
resolver_rule_id,
resolver_rule_association_id,
name
FROM awscc.route53resolver.resolver_rule_association
WHERE region = 'us-east-1'
AND data__Identifier = '{ResolverRuleAssociationId}';
```

## Permissions

To operate on the <code>resolver_rule_association</code> resource, the following permissions are required:

### Read
```json
route53resolver:GetResolverRuleAssociation
```

### Delete
```json
route53resolver:DisassociateResolverRule,
route53resolver:GetResolverRuleAssociation
```

