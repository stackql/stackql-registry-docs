---
title: privacy_budget_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - privacy_budget_template_tags
  - cleanrooms
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

Expands all tag keys and values for <code>privacy_budget_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privacy_budget_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a privacy budget within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.privacy_budget_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="privacy_budget_template_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_refresh" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="privacy_budget_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>privacy_budget_templates</code> in a region.
```sql
SELECT
region,
arn,
collaboration_arn,
collaboration_identifier,
privacy_budget_template_identifier,
auto_refresh,
privacy_budget_type,
parameters,
membership_arn,
membership_identifier,
tag_key,
tag_value
FROM aws.cleanrooms.privacy_budget_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>privacy_budget_template_tags</code> resource, see <a href="/providers/aws/cleanrooms/privacy_budget_templates/#permissions"><code>privacy_budget_templates</code></a>


