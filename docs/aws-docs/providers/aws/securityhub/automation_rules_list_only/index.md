---
title: automation_rules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rules_list_only
  - securityhub
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

Lists <code>automation_rules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/automation_rules/"><code>automation_rules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automation_rules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::AutomationRule</code> resource specifies an automation rule based on input parameters. For more information, see &#91;Automation rules&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.automation_rules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_status" /></td><td><code>string</code></td><td>Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, ASH applies the rule to findings and finding updates after the rule is created.</td></tr>
<tr><td><CopyableCode code="rule_order" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_terminal" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="criteria" /></td><td><code>object</code></td><td>A set of &#91;Security Finding Format (ASFF)&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) finding field attributes and corresponding expected values that ASH uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, ASH applies the rule action to the finding.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
Lists all <code>automation_rules</code> in a region.
```sql
SELECT
region,
rule_arn
FROM aws.securityhub.automation_rules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>automation_rules_list_only</code> resource, see <a href="/providers/aws/securityhub/automation_rules/#permissions"><code>automation_rules</code></a>


