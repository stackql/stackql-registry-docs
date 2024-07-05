---
title: evaluation_form_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_form_tags
  - connect
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

Expands all tag keys and values for <code>evaluation_forms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluation_form_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::EvaluationForm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.evaluation_form_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="title" /></td><td><code>string</code></td><td>The title of the evaluation form.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the evaluation form.</td></tr>
<tr><td><CopyableCode code="evaluation_form_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the evaluation form.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="items" /></td><td><code>array</code></td><td>The list of evaluation form items.</td></tr>
<tr><td><CopyableCode code="scoring_strategy" /></td><td><code>object</code></td><td>The scoring strategy.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the evaluation form.</td></tr>
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
Expands tags for all <code>evaluation_forms</code> in a region.
```sql
SELECT
region,
title,
description,
evaluation_form_arn,
instance_arn,
items,
scoring_strategy,
status,
tag_key,
tag_value
FROM aws.connect.evaluation_form_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>evaluation_form_tags</code> resource, see <a href="/providers/aws/connect/evaluation_forms/#permissions"><code>evaluation_forms</code></a>


