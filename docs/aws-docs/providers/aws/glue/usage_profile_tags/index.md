---
title: usage_profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_profile_tags
  - glue
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

Expands all tag keys and values for <code>usage_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This creates a Resource of UsageProfile type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.usage_profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the UsageProfile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the UsageProfile.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td>UsageProfile configuration for supported service ex: (Jobs, Sessions).</td></tr>
<tr><td><CopyableCode code="created_on" /></td><td><code>string</code></td><td>Creation time.</td></tr>
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
Expands tags for all <code>usage_profiles</code> in a region.
```sql
SELECT
region,
name,
description,
configuration,
created_on,
tag_key,
tag_value
FROM aws.glue.usage_profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>usage_profile_tags</code> resource, see <a href="/providers/aws/glue/usage_profiles/#permissions"><code>usage_profiles</code></a>

