---
title: detector_models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - detector_models_list_only
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

Lists <code>detector_models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/detector_models/"><code>detector_models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector_models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see &#91;How to Use&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *Developer Guide*.<br />When you successfully update a detector model (using the ITE console, ITE API or CLI commands, or CFN) all detector instances created by the model are reset to their initial states. (The detector's <code>state</code>, and the values of any variables and timers are reset.)<br />When you successfully update a detector model (using the ITE console, ITE API or CLI commands, or CFN) the version number of the detector model is incremented. (A detector model with version number 1 before the update has version number 2 after the update succeeds.)<br />If you attempt to update a detector model using CFN and the update does not succeed, the system may, in some cases, restore the original detector model. When this occurs, the detector model's version is incremented twice (for example, from version 1 to version 3) and the detector instances are reset.<br />Also, be aware that if you attempt to update several detector models at once using CFN, some updates may succeed and others fail. In this case, the effects on each detector model's detector instances and version number depend on whether the update succeeded or failed, with the results as stated.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.detector_models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="detector_model_name" /></td><td><code>string</code></td><td>The name of the detector model.</td></tr>
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
Lists all <code>detector_models</code> in a region.
```sql
SELECT
region,
detector_model_name
FROM aws.iotevents.detector_models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>detector_models_list_only</code> resource, see <a href="/providers/aws/iotevents/detector_models/#permissions"><code>detector_models</code></a>

