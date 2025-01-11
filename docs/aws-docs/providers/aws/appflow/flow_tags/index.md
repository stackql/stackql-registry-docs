---
title: flow_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_tags
  - appflow
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

Expands all tag keys and values for <code>flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Flow.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.flow_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>ARN identifier of the flow.</td></tr>
<tr><td><CopyableCode code="flow_name" /></td><td><code>string</code></td><td>Name of the flow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow.</td></tr>
<tr><td><CopyableCode code="kms_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="trigger_config" /></td><td><code>object</code></td><td>Trigger settings of the flow.</td></tr>
<tr><td><CopyableCode code="flow_status" /></td><td><code>string</code></td><td>Flow activation status for Scheduled- and Event-triggered flows</td></tr>
<tr><td><CopyableCode code="source_flow_config" /></td><td><code>object</code></td><td>Configurations of Source connector of the flow.</td></tr>
<tr><td><CopyableCode code="destination_flow_config_list" /></td><td><code>array</code></td><td>List of Destination connectors of the flow.</td></tr>
<tr><td><CopyableCode code="tasks" /></td><td><code>array</code></td><td>List of tasks for the flow.</td></tr>
<tr><td><CopyableCode code="metadata_catalog_config" /></td><td><code>object</code></td><td>Configurations of metadata catalog of the flow.</td></tr>
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
Expands tags for all <code>flows</code> in a region.
```sql
SELECT
region,
flow_arn,
flow_name,
description,
kms_arn,
trigger_config,
flow_status,
source_flow_config,
destination_flow_config_list,
tasks,
metadata_catalog_config,
tag_key,
tag_value
FROM aws.appflow.flow_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_tags</code> resource, see <a href="/providers/aws/appflow/flows/#permissions"><code>flows</code></a>

