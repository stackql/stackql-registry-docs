---
title: firewall_rule_group_association
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rule_group_association
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
Gets an individual <code>firewall_rule_group_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_rule_group_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.firewall_rule_group_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>firewall_rule_group_id</code></td><td><code>string</code></td><td>FirewallRuleGroupId</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>VpcId</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>FirewallRuleGroupAssociationName</td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td>Priority</td></tr>
<tr><td><code>mutation_protection</code></td><td><code>string</code></td><td>MutationProtectionStatus</td></tr>
<tr><td><code>managed_owner_name</code></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><code>creator_request_id</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>modification_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM aws.route53resolver.firewall_rule_group_association
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
