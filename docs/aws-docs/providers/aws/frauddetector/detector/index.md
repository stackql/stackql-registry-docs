---
title: detector
hide_title: false
hide_table_of_contents: false
keywords:
  - detector
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

Gets or operates on an individual <code>detector</code> resource, use <code>detectors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Detector in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.detector" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td>The ID of the detector</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
detector_id,
detector_version_status,
detector_version_id,
rule_execution_mode,
tags,
description,
rules,
event_type,
arn,
created_time,
last_updated_time,
associated_models
FROM aws.frauddetector.detector
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>detector</code> resource, the following permissions are required:

### Update
```json
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:PutDetector,
frauddetector:UpdateDetectorVersion,
frauddetector:UpdateDetectorVersionStatus,
frauddetector:UpdateDetectorVersionMetadata,
frauddetector:UpdateRuleVersion,
frauddetector:UpdateRuleMetadata,
frauddetector:CreateRule,
frauddetector:CreateVariable,
frauddetector:UpdateVariable,
frauddetector:GetVariables,
frauddetector:PutLabel,
frauddetector:PutOutcome,
frauddetector:PutEntityType,
frauddetector:PutEventType,
frauddetector:GetRules,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:GetExternalModels,
frauddetector:GetModelVersion,
frauddetector:DeleteEventType,
frauddetector:DeleteVariable,
frauddetector:DeleteLabel,
frauddetector:DeleteEntityType,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:DescribeDetector,
frauddetector:GetRules,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:DeleteDetector,
frauddetector:DeleteDetectorVersion,
frauddetector:DeleteRule,
frauddetector:DeleteEventType,
frauddetector:DeleteVariable,
frauddetector:DeleteLabel,
frauddetector:DeleteOutcome,
frauddetector:DeleteEntityType,
frauddetector:ListTagsForResource
```

### Read
```json
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:DescribeDetector,
frauddetector:GetRules,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetExternalModels,
frauddetector:GetModelVersion,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```

