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


Used to retrieve a list of <code>resolver_rules</code> in a region or to create or delete a <code>resolver_rules</code> resource, use <code>resolver_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Resolver::ResolverRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
resolver_rule_id
FROM aws.route53resolver.resolver_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>resolver_rule</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- resolver_rule.iql (required properties only)
INSERT INTO aws.route53resolver.resolver_rules (
 DomainName,
 RuleType,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ RuleType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- resolver_rule.iql (all properties)
INSERT INTO aws.route53resolver.resolver_rules (
 ResolverEndpointId,
 DomainName,
 Name,
 RuleType,
 Tags,
 TargetIps,
 region
)
SELECT 
 '{{ ResolverEndpointId }}',
 '{{ DomainName }}',
 '{{ Name }}',
 '{{ RuleType }}',
 '{{ Tags }}',
 '{{ TargetIps }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: RuleType
        value: '{{ RuleType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TargetIps
        value:
          - Ip: '{{ Ip }}'
            Ipv6: '{{ Ipv6 }}'
            Port: '{{ Port }}'
            Protocol: '{{ Protocol }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53resolver.resolver_rules
WHERE data__Identifier = '<ResolverRuleId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolver_rules</code> resource, the following permissions are required:

### Create
```json
route53resolver:CreateResolverRule,
route53resolver:GetResolverRule,
route53resolver:ListTagsForResource,
route53resolver:TagResource
```

### Delete
```json
route53resolver:DeleteResolverRule,
route53resolver:GetResolverRule
```

### List
```json
route53resolver:ListResolverRules
```

