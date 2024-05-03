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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>resolver_rule_associations</code> in a region or create a <code>resolver_rule_associations</code> resource, use <code>resolver_rule_association</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>In the response to an &#91;AssociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_AssociateResolverRule.html), &#91;DisassociateResolverRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_DisassociateResolverRule.html), or &#91;ListResolverRuleAssociations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;APIReference&#x2F;API_route53resolver_ListResolverRuleAssociations.html) request, provides information about an association between a resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_rule_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resolver_rule_association_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
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

