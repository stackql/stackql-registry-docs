---
title: worker_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - worker_configurations_list_only
  - kafkaconnect
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

Lists <code>worker_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/worker_configurations/"><code>worker_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>worker_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The configuration of the workers, which are the processes that run the connector logic.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.worker_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the worker configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the worker configuration.</td></tr>
<tr><td><CopyableCode code="worker_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom configuration.</td></tr>
<tr><td><CopyableCode code="properties_file_content" /></td><td><code>string</code></td><td>Base64 encoded contents of connect-distributed.properties file.</td></tr>
<tr><td><CopyableCode code="revision" /></td><td><code>integer</code></td><td>The description of a revision of the worker configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Lists all <code>worker_configurations</code> in a region.
```sql
SELECT
region,
worker_configuration_arn
FROM aws.kafkaconnect.worker_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>worker_configurations_list_only</code> resource, see <a href="/providers/aws/kafkaconnect/worker_configurations/#permissions"><code>worker_configurations</code></a>


