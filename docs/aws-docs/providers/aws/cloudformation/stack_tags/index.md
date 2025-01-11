---
title: stack_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_tags
  - cloudformation
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

Expands all tag keys and values for <code>stacks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stack_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_rollback" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_termination_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="root_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="change_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_in_minutes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>stacks</code> in a region.
```sql
SELECT
region,
capabilities,
role_arn,
outputs,
description,
disable_rollback,
enable_termination_protection,
notification_arns,
parameters,
parent_id,
root_id,
change_set_id,
stack_name,
stack_id,
stack_policy_body,
stack_policy_url,
stack_status,
stack_status_reason,
template_body,
template_url,
timeout_in_minutes,
last_update_time,
creation_time,
tag_key,
tag_value
FROM aws.cloudformation.stack_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stack_tags</code> resource, see <a href="/providers/aws/cloudformation/stacks/#permissions"><code>stacks</code></a>

