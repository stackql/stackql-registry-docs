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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>firewall_rule_group</code> resource, use <code>firewall_rule_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::FirewallRuleGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.firewall_rule_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>FirewallRuleGroupName</td></tr>
<tr><td><CopyableCode code="rule_count" /></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>FirewallRuleGroupStatus</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="share_status" /></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="modification_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="firewall_rules" /></td><td><code>array</code></td><td>FirewallRules</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
FROM aws.route53resolver.firewall_rule_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>firewall_rule_group</code> resource, the following permissions are required:

### Read
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

### Update
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

