---
title: metric_filters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_filters_list_only
  - logs
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

Lists <code>metric_filters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/metric_filters/"><code>metric_filters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_filters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Logs::MetricFilter</code> resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.<br />The maximum number of metric filters that can be associated with a log group is 100.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.metric_filters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of an existing log group that you want to associate with this metric filter.</td></tr>
<tr><td><CopyableCode code="filter_name" /></td><td><code>string</code></td><td>The name of the metric filter.</td></tr>
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
Lists all <code>metric_filters</code> in a region.
```sql
SELECT
region,
log_group_name,
filter_name
FROM aws.logs.metric_filters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>metric_filters_list_only</code> resource, see <a href="/providers/aws/logs/metric_filters/#permissions"><code>metric_filters</code></a>

