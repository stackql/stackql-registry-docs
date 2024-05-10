---
title: filters
hide_title: false
hide_table_of_contents: false
keywords:
  - filters
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


Used to retrieve a list of <code>filters</code> in a region or to create or delete a <code>filters</code> resource, use <code>filter</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Filter</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
detector_id,
name
FROM aws.guardduty.filters
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "FindingCriteria": {
  "Criterion": {}
 }
}
>>>
--required properties only
INSERT INTO aws.guardduty.filters (
 FindingCriteria,
 region
)
SELECT 
{{ FindingCriteria }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Action": "{{ Action }}",
 "Description": "{{ Description }}",
 "DetectorId": "{{ DetectorId }}",
 "FindingCriteria": {
  "Criterion": {}
 },
 "Rank": "{{ Rank }}",
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.guardduty.filters (
 Action,
 Description,
 DetectorId,
 FindingCriteria,
 Rank,
 Name,
 Tags,
 region
)
SELECT 
 {{ Action }},
 {{ Description }},
 {{ DetectorId }},
 {{ FindingCriteria }},
 {{ Rank }},
 {{ Name }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.guardduty.filters
WHERE data__Identifier = '<DetectorId|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>filters</code> resource, the following permissions are required:

### Create
```json
guardduty:CreateFilter,
guardduty:GetFilter,
guardduty:TagResource
```

### Delete
```json
guardduty:ListDetectors,
guardduty:ListFilters,
guardduty:GetFilter,
guardduty:DeleteFilter
```

### List
```json
guardduty:ListFilters
```

