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
<tr><td><b>Description</b></td><td>In the response to an &#91;AssociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_AssociateResolverRule.html), &#91;DisassociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_DisassociateResolverRule.html), or &#91;ListResolverRuleAssociations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_ListResolverRuleAssociations.html) request, provides information about an association between a resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_rule_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resolver_rule_association_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
resolver_rule_association_id
FROM aws.route53resolver.resolver_rule_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>resolver_rule_associations</code> resource, the following permissions are required:

### Create
```json
route53resolver:AssociateResolverRule,
route53resolver:GetResolverRuleAssociation,
ec2:DescribeVpcs
```

### List
```json
route53resolver:ListResolverRuleAssociations
```

