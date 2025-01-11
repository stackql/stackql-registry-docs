---
title: inputs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs_list_only
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

Lists <code>inputs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/inputs/"><code>inputs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inputs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into ITE. This is done by sending messages as *inputs* to ITE. For more information, see &#91;How to Use&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.inputs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="input_name" /></td><td><code>string</code></td><td>The name of the input.</td></tr>
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
Lists all <code>inputs</code> in a region.
```sql
SELECT
region,
input_name
FROM aws.iotevents.inputs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>inputs_list_only</code> resource, see <a href="/providers/aws/iotevents/inputs/#permissions"><code>inputs</code></a>

