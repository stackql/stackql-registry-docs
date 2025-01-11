---
title: dashboard_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_tags
  - iotsitewise
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Dashboard</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.dashboard_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the project in which to create the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td>The ID of the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_name" /></td><td><code>string</code></td><td>A friendly name for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_description" /></td><td><code>string</code></td><td>A description for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_definition" /></td><td><code>string</code></td><td>The dashboard definition specified in a JSON literal.</td></tr>
<tr><td><CopyableCode code="dashboard_arn" /></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
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
project_id,
dashboard_id,
dashboard_name,
dashboard_description,
dashboard_definition,
dashboard_arn,
tag_key,
tag_value
FROM aws.iotsitewise.dashboard_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dashboard_tags</code> resource, see <a href="/providers/aws/iotsitewise/dashboards/#permissions"><code>dashboards</code></a>

