---
title: rotation_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - rotation_tags
  - ssmcontacts
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

Expands all tag keys and values for <code>rotations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotation_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::Rotation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.rotation_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Rotation</td></tr>
<tr><td><CopyableCode code="contact_ids" /></td><td><code>array</code></td><td>Members of the rotation</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>Start time of the first shift of Oncall Schedule</td></tr>
<tr><td><CopyableCode code="time_zone_id" /></td><td><code>string</code></td><td>TimeZone Identifier for the Oncall Schedule</td></tr>
<tr><td><CopyableCode code="recurrence" /></td><td><code>object</code></td><td>Information about when an on-call rotation is in effect and how long the rotation period lasts.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rotation.</td></tr>
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
Expands tags for all <code>rotations</code> in a region.
```sql
SELECT
region,
name,
contact_ids,
start_time,
time_zone_id,
recurrence,
arn,
tag_key,
tag_value
FROM aws.ssmcontacts.rotation_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rotation_tags</code> resource, see <a href="/providers/aws/ssmcontacts/rotations/#permissions"><code>rotations</code></a>


