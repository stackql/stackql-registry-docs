---
title: dashboard_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_tags
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

Expands all tag keys and values for <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Dashboard Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.dashboard_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that this dashboard was created.</p></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td><p>A list of Amazon QuickSight parameters and the list's override values.</p></td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_entity" /></td><td><code>object</code></td><td><p>Dashboard source entity.</p></td></tr>
<tr><td><CopyableCode code="theme_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The last time that this dashboard was updated.</p></td></tr>
<tr><td><CopyableCode code="validation_strategy" /></td><td><code>object</code></td><td><p>The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to <code>LENIENT</code>, validation is skipped for specific errors.</p></td></tr>
<tr><td><CopyableCode code="folder_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="link_sharing_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_publish_options" /></td><td><code>object</code></td><td><p>Dashboard publish options.</p></td></tr>
<tr><td><CopyableCode code="last_published_time" /></td><td><code>string</code></td><td><p>The last time that this dashboard was published.</p></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>object</code></td><td><p>Dashboard version.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="link_entities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the resource.</p></td></tr>
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
Expands tags for all <code>dashboards</code> in a region.
```sql
SELECT
region,
created_time,
parameters,
version_description,
source_entity,
theme_arn,
definition,
last_updated_time,
validation_strategy,
folder_arns,
dashboard_id,
link_sharing_configuration,
name,
dashboard_publish_options,
last_published_time,
version,
aws_account_id,
permissions,
link_entities,
arn,
tag_key,
tag_value
FROM aws.quicksight.dashboard_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dashboard_tags</code> resource, see <a href="/providers/aws/quicksight/dashboards/#permissions"><code>dashboards</code></a>

