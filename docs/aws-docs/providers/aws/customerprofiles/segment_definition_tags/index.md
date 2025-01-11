---
title: segment_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - segment_definition_tags
  - customerprofiles
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

Expands all tag keys and values for <code>segment_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>segment_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A segment definition resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.segment_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this segment definition got created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the segment definition.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the segment definition.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="segment_definition_name" /></td><td><code>string</code></td><td>The unique name of the segment definition.</td></tr>
<tr><td><CopyableCode code="segment_groups" /></td><td><code>object</code></td><td>An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.</td></tr>
<tr><td><CopyableCode code="segment_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the segment definition.</td></tr>
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
Expands tags for all <code>segment_definitions</code> in a region.
```sql
SELECT
region,
created_at,
description,
display_name,
domain_name,
segment_definition_name,
segment_groups,
segment_definition_arn,
tag_key,
tag_value
FROM aws.customerprofiles.segment_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>segment_definition_tags</code> resource, see <a href="/providers/aws/customerprofiles/segment_definitions/#permissions"><code>segment_definitions</code></a>

