---
title: event_invoke_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_configs_list_only
  - lambda
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

Lists <code>event_invoke_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/event_invoke_configs/"><code>event_invoke_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.event_invoke_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="destination_config" /></td><td><code>object</code></td><td>A configuration object that specifies the destination of an event after Lambda processes it.</td></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><CopyableCode code="maximum_event_age_in_seconds" /></td><td><code>integer</code></td><td>The maximum age of a request that Lambda sends to a function for processing.</td></tr>
<tr><td><CopyableCode code="maximum_retry_attempts" /></td><td><code>integer</code></td><td>The maximum number of times to retry when the function returns an error.</td></tr>
<tr><td><CopyableCode code="qualifier" /></td><td><code>string</code></td><td>The identifier of a version or alias.</td></tr>
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
Lists all <code>event_invoke_configs</code> in a region.
```sql
SELECT
region,
function_name,
qualifier
FROM aws.lambda.event_invoke_configs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_invoke_configs_list_only</code> resource, see <a href="/providers/aws/lambda/event_invoke_configs/#permissions"><code>event_invoke_configs</code></a>


