---
title: resolver_rule_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_rule_tags
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

Expands all tag keys and values for <code>resolver_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rule_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Resolver::ResolverRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_rule_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resolver_endpoint_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps</td></tr>
<tr><td><CopyableCode code="rule_type" /></td><td><code>string</code></td><td>When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.</td></tr>
<tr><td><CopyableCode code="resolver_rule_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resolver rule.</td></tr>
<tr><td><CopyableCode code="target_ips" /></td><td><code>array</code></td><td>An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the Resolver rule</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>resolver_rules</code> in a region.
```sql
SELECT
region,
resolver_endpoint_id,
domain_name,
rule_type,
resolver_rule_id,
arn,
target_ips,
name,
tag_key,
tag_value
FROM aws.route53resolver.resolver_rule_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resolver_rule_tags</code> resource, see <a href="/providers/aws/route53resolver/resolver_rules/#permissions"><code>resolver_rules</code></a>

