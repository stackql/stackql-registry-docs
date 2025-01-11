---
title: findings_filter_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_filter_tags
  - macie
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

Expands all tag keys and values for <code>findings_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filter_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie FindingsFilter resource schema.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.findings_filter_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Findings filter name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Findings filter description</td></tr>
<tr><td><CopyableCode code="finding_criteria" /></td><td><code>object</code></td><td>Findings filter criteria.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td>Findings filter action.</td></tr>
<tr><td><CopyableCode code="position" /></td><td><code>integer</code></td><td>Findings filter position.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
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
Expands tags for all <code>findings_filters</code> in a region.
```sql
SELECT
region,
name,
description,
finding_criteria,
action,
position,
id,
arn,
tag_key,
tag_value
FROM aws.macie.findings_filter_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>findings_filter_tags</code> resource, see <a href="/providers/aws/macie/findings_filters/#permissions"><code>findings_filters</code></a>

