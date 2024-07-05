---
title: theme_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - theme_tags
  - quicksight
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

Expands all tag keys and values for <code>themes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>theme_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Theme Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.theme_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the theme.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_theme_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>object</code></td><td><p>The theme configuration. This configuration contains all of the display properties for<br />a theme.</p></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The date and time that the theme was created.</p></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The date and time that the theme was last updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="theme_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>object</code></td><td><p>A version of a theme.</p></td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>themes</code> in a region.
```sql
SELECT
region,
arn,
aws_account_id,
base_theme_id,
configuration,
created_time,
last_updated_time,
name,
permissions,
theme_id,
type,
version,
version_description,
tag_key,
tag_value
FROM aws.quicksight.theme_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>theme_tags</code> resource, see <a href="/providers/aws/quicksight/themes/#permissions"><code>themes</code></a>


