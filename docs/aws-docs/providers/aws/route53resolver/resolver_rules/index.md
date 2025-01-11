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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>resolver_rule</code> resource or lists <code>resolver_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Resolver::ResolverRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resolver_endpoint_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps</td></tr>
<tr><td><CopyableCode code="rule_type" /></td><td><code>string</code></td><td>When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.</td></tr>
<tr><td><CopyableCode code="resolver_rule_id" /></td><td><code>string</code></td><td>The ID of the endpoint that the rule is associated with.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resolver rule.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="target_ips" /></td><td><code>array</code></td><td>An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the Resolver rule</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html"><code>AWS::Route53Resolver::ResolverRule</code></a>.

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
    <td><CopyableCode code="RuleType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>resolver_rules</code> in a region.
```sql
SELECT
region,
resolver_endpoint_id,
domain_name,
rule_type,
resolver_rule_id,
arn,
tags,
target_ips,
name
FROM aws.route53resolver.resolver_rules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resolver_rule</code>.
```sql
SELECT
region,
resolver_endpoint_id,
domain_name,
rule_type,
resolver_rule_id,
arn,
tags,
target_ips,
name
FROM aws.route53resolver.resolver_rules
WHERE region = 'us-east-1' AND data__Identifier = '<ResolverRuleId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolver_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolver_rules (
 RuleType,
 region
)
SELECT 
'{{ RuleType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolver_rules (
 ResolverEndpointId,
 DomainName,
 RuleType,
 Tags,
 TargetIps,
 Name,
 region
)
SELECT 
 '{{ ResolverEndpointId }}',
 '{{ DomainName }}',
 '{{ RuleType }}',
 '{{ Tags }}',
 '{{ TargetIps }}',
 '{{ Name }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: resolver_rule
    props:
      - name: ResolverEndpointId
        value: '{{ ResolverEndpointId }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: RuleType
        value: '{{ RuleType }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: TargetIps
        value:
          - Ipv6: '{{ Ipv6 }}'
            Ip: '{{ Ip }}'
            Port: '{{ Port }}'
            Protocol: '{{ Protocol }}'
            ServerNameIndication: '{{ ServerNameIndication }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.resolver_rules
WHERE data__Identifier = '<ResolverRuleId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolver_rules</code> resource, the following permissions are required:

### Read
```json
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource
```

### Create
```json
route53resolver:CreateResolverRule,
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource,
route53resolver:TagResource
```

### Update
```json
route53resolver:UpdateResolverRule,
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource,
route53resolver:TagResource,
route53resolver:UntagResource
```

### List
```json
route53resolver:ListResolverRules
```

### Delete
```json
route53resolver:DeleteResolverRule,
route53resolver:GetResolverRule
```
