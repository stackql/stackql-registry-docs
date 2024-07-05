---
title: detectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - detectors_list_only
  - frauddetector
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

Lists <code>detectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/detectors/"><code>detectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Detector in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.detectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td>The ID of the detector</td></tr>
<tr><td><CopyableCode code="detector_version_status" /></td><td><code>string</code></td><td>The desired detector version status for the detector</td></tr>
<tr><td><CopyableCode code="detector_version_id" /></td><td><code>string</code></td><td>The active version ID of the detector</td></tr>
<tr><td><CopyableCode code="rule_execution_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this detector.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the detector.</td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="event_type" /></td><td><code>object</code></td><td>The event type to associate this detector with.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the detector.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the detector was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the detector was last updated.</td></tr>
<tr><td><CopyableCode code="associated_models" /></td><td><code>array</code></td><td>The models to associate with this detector.</td></tr>
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
Lists all <code>detectors</code> in a region.
```sql
SELECT
region,
arn
FROM aws.frauddetector.detectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>detectors_list_only</code> resource, see <a href="/providers/aws/frauddetector/detectors/#permissions"><code>detectors</code></a>


