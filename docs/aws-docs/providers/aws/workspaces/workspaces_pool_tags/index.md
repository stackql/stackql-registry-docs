---
title: workspaces_pool_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_pool_tags
  - workspaces
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

Expands all tag keys and values for <code>workspaces_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_pool_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::WorkSpaces::WorkspacesPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspaces.workspaces_pool_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_settings" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>workspaces_pools</code> in a region.
```sql
SELECT
region,
pool_id,
pool_arn,
capacity,
pool_name,
description,
created_at,
bundle_id,
directory_id,
application_settings,
timeout_settings,
tag_key,
tag_value
FROM aws.workspaces.workspaces_pool_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workspaces_pool_tags</code> resource, see <a href="/providers/aws/workspaces/workspaces_pools/#permissions"><code>workspaces_pools</code></a>

