---
title: robot_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_tags
  - robomaker
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

Expands all tag keys and values for <code>robots</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::RoboMaker::Robot resource creates an AWS RoboMaker Robot.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.robot_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the fleet.</td></tr>
<tr><td><CopyableCode code="architecture" /></td><td><code>string</code></td><td>The target architecture of the robot.</td></tr>
<tr><td><CopyableCode code="greengrass_group_id" /></td><td><code>string</code></td><td>The Greengrass group id.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the robot.</td></tr>
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
Expands tags for all <code>robots</code> in a region.
```sql
SELECT
region,
arn,
fleet,
architecture,
greengrass_group_id,
name,
tag_key,
tag_value
FROM aws.robomaker.robot_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>robot_tags</code> resource, see <a href="/providers/aws/robomaker/robots/#permissions"><code>robots</code></a>


