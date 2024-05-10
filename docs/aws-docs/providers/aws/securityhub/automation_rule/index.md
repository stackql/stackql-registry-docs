---
title: automation_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rule
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


Gets or updates an individual <code>automation_rule</code> resource, use <code>automation_rules</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automation_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters. For more information, see &#91;Automation rules&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;automation-rules.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.automation_rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_status" /></td><td><code>string</code></td><td>Whether the rule is active after it is created. If this parameter is equal to ``ENABLED``, ASH applies the rule to findings and finding updates after the rule is created.</td></tr>
<tr><td><CopyableCode code="rule_order" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_terminal" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="criteria" /></td><td><code>object</code></td><td>A set of &#91;Security Finding Format (ASFF)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;securityhub-findings-format.html) finding field attributes and corresponding expected values that ASH uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, ASH applies the rule action to the finding.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
rule_arn,
rule_status,
rule_order,
description,
rule_name,
created_at,
updated_at,
created_by,
is_terminal,
actions,
criteria,
tags
FROM aws.securityhub.automation_rule
WHERE region = 'us-east-1' AND data__Identifier = '<RuleArn>';
```


## Permissions

To operate on the <code>automation_rule</code> resource, the following permissions are required:

### Read
```json
securityhub:ListAutomationRules,
securityhub:BatchGetAutomationRules,
securityhub:ListTagsForResource
```

### Update
```json
securityhub:BatchUpdateAutomationRules,
securityhub:TagResource,
securityhub:UntagResource,
securityhub:ListTagsForResource
```

