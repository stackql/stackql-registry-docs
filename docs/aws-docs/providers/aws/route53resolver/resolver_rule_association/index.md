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
Gets or operates on an individual <code>resolver_rule_association</code> resource, use <code>resolver_rule_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>In the response to an &#91;AssociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_AssociateResolverRule.html), &#91;DisassociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_DisassociateResolverRule.html), or &#91;ListResolverRuleAssociations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_ListResolverRuleAssociations.html) request, provides information about an association between a resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_rule_association</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpc_id,
resolver_rule_id,
resolver_rule_association_id,
name
FROM aws.route53resolver.resolver_rule_association
WHERE data__Identifier = '<ResolverRuleAssociationId>';
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

