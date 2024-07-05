---
title: scene_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - scene_tags
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

Expands all tag keys and values for <code>scenes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scene_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Scene</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.scene_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scene_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the scene.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the scene.</td></tr>
<tr><td><CopyableCode code="content_location" /></td><td><code>string</code></td><td>The relative path that specifies the location of the content definition file.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the scene was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td>A list of capabilities that the scene uses to render.</td></tr>
<tr><td><CopyableCode code="scene_metadata" /></td><td><code>object</code></td><td>A key-value pair of scene metadata for the scene.</td></tr>
<tr><td><CopyableCode code="generated_scene_metadata" /></td><td><code>object</code></td><td>A key-value pair of generated scene metadata for the scene.</td></tr>
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
Expands tags for all <code>scenes</code> in a region.
```sql
SELECT
region,
scene_id,
arn,
description,
content_location,
creation_date_time,
update_date_time,
workspace_id,
capabilities,
scene_metadata,
generated_scene_metadata,
tag_key,
tag_value
FROM aws.iottwinmaker.scene_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scene_tags</code> resource, see <a href="/providers/aws/iottwinmaker/scenes/#permissions"><code>scenes</code></a>


