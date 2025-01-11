---
title: alarm_models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_models_list_only
  - iotevents
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

Lists <code>alarm_models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/alarm_models/"><code>alarm_models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an alarm model to monitor an ITE input attribute. You can use the alarm to get notified when the value is outside a specified range. For more information, see &#91;Create an alarm model&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
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
Lists all <code>alarm_models</code> in a region.
```sql
SELECT
region,
alarm_model_name
FROM aws.iotevents.alarm_models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>alarm_models_list_only</code> resource, see <a href="/providers/aws/iotevents/alarm_models/#permissions"><code>alarm_models</code></a>

