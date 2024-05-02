---
title: detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - detectors
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
Retrieves a list of <code>detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Detector in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.frauddetector.detectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the detector.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.frauddetector.detectors
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>detectors</code> resource, the following permissions are required:

### Create
```json
frauddetector:PutDetector,
frauddetector:CreateDetectorVersion,
frauddetector:UpdateDetectorVersionStatus,
frauddetector:CreateRule,
frauddetector:CreateVariable,
frauddetector:PutLabel,
frauddetector:PutOutcome,
frauddetector:PutEntityType,
frauddetector:PutEventType,
frauddetector:DescribeDetector,
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
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

### List
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

