---
title: stacks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - stacks_list_only
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

Lists <code>stacks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/stacks/"><code>stacks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stacks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stacks_list_only" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_in_minutes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>stacks</code> in a region.
```sql
SELECT
region,
stack_id
FROM aws.cloudformation.stacks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stacks_list_only</code> resource, see <a href="/providers/aws/cloudformation/stacks/#permissions"><code>stacks</code></a>


