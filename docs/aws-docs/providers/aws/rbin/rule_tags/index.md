---
title: rule_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_tags
  - rbin
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

Expands all tag keys and values for <code>rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Rbin::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rbin.rule_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Rule Arn is unique for each rule.</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td>The unique ID of the retention rule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the retention rule.</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>Information about the resource tags used to identify resources that are retained by the retention rule.</td></tr>
<tr><td><CopyableCode code="exclude_resource_tags" /></td><td><code>array</code></td><td>Information about the exclude resource tags used to identify resources that are excluded by the retention rule.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type retained by the retention rule.</td></tr>
<tr><td><CopyableCode code="retention_period" /></td><td><code>object</code></td><td>Information about the retention period for which the retention rule is to retain resources.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The state of the retention rule. Only retention rules that are in the available state retain resources.</td></tr>
<tr><td><CopyableCode code="lock_configuration" /></td><td><code>object</code></td><td>Information about the retention rule lock configuration.</td></tr>
<tr><td><CopyableCode code="lock_state" /></td><td><code>string</code></td><td>The lock state for the retention rule.</td></tr>
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
Expands tags for all <code>rules</code> in a region.
```sql
SELECT
region,
arn,
identifier,
description,
resource_tags,
exclude_resource_tags,
resource_type,
retention_period,
status,
lock_configuration,
lock_state,
tag_key,
tag_value
FROM aws.rbin.rule_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rule_tags</code> resource, see <a href="/providers/aws/rbin/rules/#permissions"><code>rules</code></a>

