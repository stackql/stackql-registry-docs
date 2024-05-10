---
title: detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - detectors
  - guardduty
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


Used to retrieve a list of <code>detectors</code> in a region or to create or delete a <code>detectors</code> resource, use <code>detector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Detector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.guardduty.detectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>detector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- detector.iql (required properties only)
INSERT INTO aws.guardduty.detectors (
 Enable,
 region
)
SELECT 
'{{ Enable }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- detector.iql (all properties)
INSERT INTO aws.guardduty.detectors (
 FindingPublishingFrequency,
 Enable,
 DataSources,
 Features,
 Tags,
 region
)
SELECT 
 '{{ FindingPublishingFrequency }}',
 '{{ Enable }}',
 '{{ DataSources }}',
 '{{ Features }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: detector
    props:
      - name: FindingPublishingFrequency
        value: '{{ FindingPublishingFrequency }}'
      - name: Enable
        value: '{{ Enable }}'
      - name: DataSources
        value:
          S3Logs:
            Enable: '{{ Enable }}'
          Kubernetes:
            AuditLogs:
              Enable: '{{ Enable }}'
          MalwareProtection:
            ScanEc2InstanceWithFindings:
              EbsVolumes: '{{ EbsVolumes }}'
      - name: Features
        value:
          - Name: '{{ Name }}'
            Status: '{{ Status }}'
            AdditionalConfiguration:
              - Name: '{{ Name }}'
                Status: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.guardduty.detectors
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>detectors</code> resource, the following permissions are required:

### Create
```json
guardduty:CreateDetector,
guardduty:GetDetector,
guardduty:TagResource,
iam:CreateServiceLinkedRole,
iam:GetRole
```

### Delete
```json
guardduty:ListDetectors,
guardduty:DeleteDetector,
guardduty:GetDetector
```

### List
```json
guardduty:ListDetectors
```

