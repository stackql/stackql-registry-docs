---
title: delivery_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_sources_list_only
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

Lists <code>delivery_sources</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/delivery_sources/"><code>delivery_sources</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_sources_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.<br />Only some AWS services support being configured as a delivery source. These services are listed as Supported &#91;V2 Permissions&#93; in the table at &#91;Enabling logging from AWS services&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name of the Log source.</td></tr>
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
Lists all <code>delivery_sources</code> in a region.
```sql
SELECT
region,
name
FROM aws.logs.delivery_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>delivery_sources_list_only</code> resource, see <a href="/providers/aws/logs/delivery_sources/#permissions"><code>delivery_sources</code></a>

