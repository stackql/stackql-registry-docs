---
title: firewall_rule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rule_group
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
Gets an individual <code>firewall_rule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_rule_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.firewall_rule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>FirewallRuleGroupName</td></tr>
<tr><td><code>rule_count</code></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td>FirewallRuleGroupStatus</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><code>share_status</code></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><code>creator_request_id</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>modification_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>firewall_rules</code></td><td><code>array</code></td><td>FirewallRules</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>firewall_rule_group</code> resource, the following permissions are required:

### Read
<pre>
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*</pre>

### Delete
<pre>
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*</pre>

### Update
<pre>
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*</pre>


## Example
```sql
SELECT
region,
id,
arn,
name,
rule_count,
status,
status_message,
owner_id,
share_status,
creator_request_id,
creation_time,
modification_time,
firewall_rules,
tags
FROM awscc.route53resolver.firewall_rule_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
