---
title: threat_intel_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intel_sets
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

Creates, updates, deletes or gets a <code>threat_intel_set</code> resource or lists <code>threat_intel_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>threat_intel_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::ThreatIntelSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.threat_intel_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="activate" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Format, Location, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>threat_intel_sets</code> in a region.
```sql
SELECT
region,
id,
detector_id
FROM aws.guardduty.threat_intel_sets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>threat_intel_set</code>.
```sql
SELECT
region,
id,
format,
activate,
detector_id,
name,
location,
tags
FROM aws.guardduty.threat_intel_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<DetectorId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>threat_intel_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.guardduty.threat_intel_sets (
 Format,
 Location,
 region
)
SELECT 
'{{ Format }}',
 '{{ Location }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.guardduty.threat_intel_sets (
 Format,
 Activate,
 DetectorId,
 Name,
 Location,
 Tags,
 region
)
SELECT 
 '{{ Format }}',
 '{{ Activate }}',
 '{{ DetectorId }}',
 '{{ Name }}',
 '{{ Location }}',
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
  - name: threat_intel_set
    props:
      - name: Format
        value: '{{ Format }}'
      - name: Activate
        value: '{{ Activate }}'
      - name: DetectorId
        value: '{{ DetectorId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Location
        value: '{{ Location }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.guardduty.threat_intel_sets
WHERE data__Identifier = '<Id|DetectorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>threat_intel_sets</code> resource, the following permissions are required:

### Create
```json
guardduty:CreateThreatIntelSet,
guardduty:GetThreatIntelSet,
guardduty:TagResource,
iam:PutRolePolicy
```

### Read
```json
guardduty:GetThreatIntelSet
```

### Delete
```json
guardduty:ListDetectors,
guardduty:ListThreatIntelSets,
guardduty:DeleteThreatIntelSet,
guardduty:GetThreatIntelSet,
iam:DeleteRolePolicy
```

### Update
```json
guardduty:UpdateThreatIntelSet,
guardduty:GetThreatIntelSet,
guardduty:ListThreatIntelSets,
iam:PutRolePolicy
```

### List
```json
guardduty:ListThreatIntelSets
```

