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
Retrieves a list of <code>firewall_rule_group_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_rule_group_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.firewall_rule_group_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>FirewallRuleGroupId</code></td><td><code>string</code></td><td>FirewallRuleGroupId</td></tr>
<tr><td><code>VpcId</code></td><td><code>string</code></td><td>VpcId</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>FirewallRuleGroupAssociationName</td></tr>
<tr><td><code>Priority</code></td><td><code>integer</code></td><td>Priority</td></tr>
<tr><td><code>MutationProtection</code></td><td><code>string</code></td><td>MutationProtectionStatus</td></tr>
<tr><td><code>ManagedOwnerName</code></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><code>StatusMessage</code></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><code>CreatorRequestId</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>ModificationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53resolver.firewall_rule_group_associations
WHERE region = 'us-east-1'
</pre>
