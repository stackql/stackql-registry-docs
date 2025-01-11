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

Creates, updates, deletes or gets a <code>firewall_rule_group_association</code> resource or lists <code>firewall_rule_group_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::FirewallRuleGroupAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.firewall_rule_group_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="firewall_rule_group_id" /></td><td><code>string</code></td><td>FirewallRuleGroupId</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>VpcId</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>FirewallRuleGroupAssociationName</td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td>Priority</td></tr>
<tr><td><CopyableCode code="mutation_protection" /></td><td><code>string</code></td><td>MutationProtectionStatus</td></tr>
<tr><td><CopyableCode code="managed_owner_name" /></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="modification_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html"><code>AWS::Route53Resolver::FirewallRuleGroupAssociation</code></a>.

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
    <td><CopyableCode code="FirewallRuleGroupId, VpcId, Priority, region" /></td>
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
Gets all <code>firewall_rule_group_associations</code> in a region.
```sql
SELECT
region,
id,
arn,
firewall_rule_group_id,
vpc_id,
name,
priority,
mutation_protection,
managed_owner_name,
status,
status_message,
creator_request_id,
creation_time,
modification_time,
tags
FROM aws.route53resolver.firewall_rule_group_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>firewall_rule_group_association</code>.
```sql
SELECT
region,
id,
arn,
firewall_rule_group_id,
vpc_id,
name,
priority,
mutation_protection,
managed_owner_name,
status,
status_message,
creator_request_id,
creation_time,
modification_time,
tags
FROM aws.route53resolver.firewall_rule_group_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.firewall_rule_group_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>firewall_rule_group_associations</code> resource, the following permissions are required:

### Create
```json
route53resolver:AssociateFirewallRuleGroup,
route53resolver:GetFirewallRuleGroupAssociation,
route53resolver:TagResource,
route53resolver:ListTagsForResource,
ec2:DescribeVpcs
```

### Read
```json
route53resolver:GetFirewallRuleGroupAssociation,
route53resolver:ListTagsForResource
```

### List
```json
route53resolver:ListFirewallRuleGroupAssociations,
route53resolver:ListTagsForResource
```

### Delete
```json
route53resolver:DisassociateFirewallRuleGroup,
route53resolver:GetFirewallRuleGroupAssociation,
route53resolver:UntagResource,
route53resolver:ListTagsForResource
```

### Update
```json
route53resolver:UpdateFirewallRuleGroupAssociation,
route53resolver:GetFirewallRuleGroupAssociation,
route53resolver:TagResource,
route53resolver:UntagResource,
route53resolver:ListTagsForResource
```
