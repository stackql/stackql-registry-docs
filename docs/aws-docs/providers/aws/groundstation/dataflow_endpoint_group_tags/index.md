---
title: dataflow_endpoint_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoint_group_tags
  - groundstation
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

Expands all tag keys and values for <code>dataflow_endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_endpoint_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station DataflowEndpointGroup schema for CloudFormation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.dataflow_endpoint_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="contact_pre_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.</td></tr>
<tr><td><CopyableCode code="contact_post_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.</td></tr>
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
Expands tags for all <code>dataflow_endpoint_groups</code> in a region.
```sql
SELECT
region,
id,
arn,
endpoint_details,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
tag_key,
tag_value
FROM aws.groundstation.dataflow_endpoint_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dataflow_endpoint_group_tags</code> resource, see <a href="/providers/aws/groundstation/dataflow_endpoint_groups/#permissions"><code>dataflow_endpoint_groups</code></a>

