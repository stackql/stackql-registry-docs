---
title: report_plans_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - report_plans_list_only
  - backup
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

Lists <code>report_plans</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/report_plans/"><code>report_plans</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_plans_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a report plan in AWS Backup Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.report_plans_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="report_plan_arn" /></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</td></tr>
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
Lists all <code>report_plans</code> in a region.
```sql
SELECT
region,
report_plan_arn
FROM aws.backup.report_plans_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>report_plans_list_only</code> resource, see <a href="/providers/aws/backup/report_plans/#permissions"><code>report_plans</code></a>

