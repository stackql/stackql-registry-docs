---
title: test_case_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - test_case_tags
  - apptest
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

Expands all tag keys and values for <code>test_cases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_case_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a Test Case that can be captured and executed</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apptest.test_case_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="latest_version" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="steps" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_version" /></td><td><code>number</code></td><td></td></tr>
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
Expands tags for all <code>test_cases</code> in a region.
```sql
SELECT
region,
creation_time,
description,
last_update_time,
latest_version,
name,
status,
steps,
test_case_arn,
test_case_id,
test_case_version,
tag_key,
tag_value
FROM aws.apptest.test_case_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>test_case_tags</code> resource, see <a href="/providers/aws/apptest/test_cases/#permissions"><code>test_cases</code></a>

