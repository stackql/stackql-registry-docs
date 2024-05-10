---
title: resolver_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_rule
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>resolver_rule</code> resource, use <code>resolver_rules</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Resolver::ResolverRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resolver_endpoint_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the Resolver rule</td></tr>
<tr><td><CopyableCode code="rule_type" /></td><td><code>string</code></td><td>When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="target_ips" /></td><td><code>array</code></td><td>An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resolver rule.</td></tr>
<tr><td><CopyableCode code="resolver_rule_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
resolver_endpoint_id,
domain_name,
name,
rule_type,
tags,
target_ips,
arn,
resolver_rule_id
FROM aws.route53resolver.resolver_rule
WHERE region = 'us-east-1' AND data__Identifier = '<ResolverRuleId>';
```


## Permissions

To operate on the <code>resolver_rule</code> resource, the following permissions are required:

### Read
```json
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource
```

### Update
```json
route53resolver:UpdateResolverRule,
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource,
route53resolver:TagResource,
route53resolver:UntagResource
```

