---
title: report_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - report_definitions_list_only
  - cur
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

Lists <code>report_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/report_definitions/"><code>report_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cur.report_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="report_name" /></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr>
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
Lists all <code>report_definitions</code> in a region.
```sql
SELECT
region,
report_name
FROM aws.cur.report_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>report_definitions_list_only</code> resource, see <a href="/providers/aws/cur/report_definitions/#permissions"><code>report_definitions</code></a>

