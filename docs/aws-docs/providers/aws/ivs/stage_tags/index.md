---
title: stage_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stage_tags
  - ivs
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

Expands all tag keys and values for <code>stages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Definition for type AWS::IVS::Stage.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.stage_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Stage ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Stage name</td></tr>
<tr><td><CopyableCode code="auto_participant_recording_configuration" /></td><td><code>object</code></td><td>Configuration object for individual participant recording, to attach to the new stage.</td></tr>
<tr><td><CopyableCode code="active_session_id" /></td><td><code>string</code></td><td>ID of the active session within the stage.</td></tr>
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
Expands tags for all <code>stages</code> in a region.
```sql
SELECT
region,
arn,
name,
auto_participant_recording_configuration,
active_session_id,
tag_key,
tag_value
FROM aws.ivs.stage_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stage_tags</code> resource, see <a href="/providers/aws/ivs/stages/#permissions"><code>stages</code></a>

