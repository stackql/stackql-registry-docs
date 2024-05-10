---
title: firewall_rule_group_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rule_group_associations
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


Used to retrieve a list of <code>firewall_rule_group_associations</code> in a region or to create or delete a <code>firewall_rule_group_associations</code> resource, use <code>firewall_rule_group_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::FirewallRuleGroupAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.firewall_rule_group_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
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
id
FROM aws.route53resolver.firewall_rule_group_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>firewall_rule_group_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- firewall_rule_group_association.iql (required properties only)
INSERT INTO aws.route53resolver.firewall_rule_group_associations (
 FirewallRuleGroupId,
 VpcId,
 Priority,
 region
)
SELECT 
'{{ FirewallRuleGroupId }}',
 '{{ VpcId }}',
 '{{ Priority }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- firewall_rule_group_association.iql (all properties)
INSERT INTO aws.route53resolver.firewall_rule_group_associations (
 FirewallRuleGroupId,
 VpcId,
 Name,
 Priority,
 MutationProtection,
 Tags,
 region
)
SELECT 
 '{{ FirewallRuleGroupId }}',
 '{{ VpcId }}',
 '{{ Name }}',
 '{{ Priority }}',
 '{{ MutationProtection }}',
 '{{ Tags }}',
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
  - name: firewall_rule_group_association
    props:
      - name: FirewallRuleGroupId
        value: '{{ FirewallRuleGroupId }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Priority
        value: '{{ Priority }}'
      - name: MutationProtection
        value: '{{ MutationProtection }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53resolver.firewall_rule_group_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>firewall_rule_group_associations</code> resource, the following permissions are required:

### Create
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

### List
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

### Delete
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

