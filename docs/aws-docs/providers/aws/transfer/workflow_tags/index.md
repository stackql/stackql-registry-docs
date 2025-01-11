---
title: workflow_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_tags
  - transfer
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

Expands all tag keys and values for <code>workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Workflow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.workflow_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="on_exception_steps" /></td><td><code>array</code></td><td>Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.</td></tr>
<tr><td><CopyableCode code="steps" /></td><td><code>array</code></td><td>Specifies the details for the steps that are in the specified workflow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the workflow.</td></tr>
<tr><td><CopyableCode code="workflow_id" /></td><td><code>string</code></td><td>A unique identifier for the workflow.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the workflow.</td></tr>
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
Expands tags for all <code>workflows</code> in a region.
```sql
SELECT
region,
on_exception_steps,
steps,
description,
workflow_id,
arn,
tag_key,
tag_value
FROM aws.transfer.workflow_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workflow_tags</code> resource, see <a href="/providers/aws/transfer/workflows/#permissions"><code>workflows</code></a>

