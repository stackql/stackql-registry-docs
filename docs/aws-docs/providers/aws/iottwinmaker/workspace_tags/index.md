---
title: workspace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_tags
  - iottwinmaker
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

Expands all tag keys and values for <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.workspace_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the workspace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workspace.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The ARN of the execution role associated with the workspace.</td></tr>
<tr><td><CopyableCode code="s3_location" /></td><td><code>string</code></td><td>The ARN of the S3 bucket where resources associated with the workspace are stored.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the workspace was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
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
Expands tags for all <code>workspaces</code> in a region.
```sql
SELECT
region,
workspace_id,
arn,
description,
role,
s3_location,
creation_date_time,
update_date_time,
tag_key,
tag_value
FROM aws.iottwinmaker.workspace_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workspace_tags</code> resource, see <a href="/providers/aws/iottwinmaker/workspaces/#permissions"><code>workspaces</code></a>


