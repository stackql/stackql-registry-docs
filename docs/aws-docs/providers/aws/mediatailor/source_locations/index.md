---
title: source_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_locations
  - mediatailor
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


Used to retrieve a list of <code>source_locations</code> in a region or to create or delete a <code>source_locations</code> resource, use <code>source_location</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::SourceLocation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.source_locations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
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
source_location_name
FROM aws.mediatailor.source_locations
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
 "HttpConfiguration": {
  "BaseUrl": "{{ BaseUrl }}"
 },
 "SourceLocationName": "{{ SourceLocationName }}"
}
>>>
--required properties only
INSERT INTO aws.mediatailor.source_locations (
 HttpConfiguration,
 SourceLocationName,
 region
)
SELECT 
{{ .HttpConfiguration }},
 {{ .SourceLocationName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccessConfiguration": {
  "AccessType": "{{ AccessType }}",
  "SecretsManagerAccessTokenConfiguration": {
   "HeaderName": "{{ HeaderName }}",
   "SecretArn": "{{ SecretArn }}",
   "SecretStringKey": "{{ SecretStringKey }}"
  }
 },
 "DefaultSegmentDeliveryConfiguration": {
  "BaseUrl": "{{ BaseUrl }}"
 },
 "HttpConfiguration": {
  "BaseUrl": "{{ BaseUrl }}"
 },
 "SegmentDeliveryConfigurations": [
  {
   "BaseUrl": "{{ BaseUrl }}",
   "Name": "{{ Name }}"
  }
 ],
 "SourceLocationName": "{{ SourceLocationName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.mediatailor.source_locations (
 AccessConfiguration,
 DefaultSegmentDeliveryConfiguration,
 HttpConfiguration,
 SegmentDeliveryConfigurations,
 SourceLocationName,
 Tags,
 region
)
SELECT 
 {{ .AccessConfiguration }},
 {{ .DefaultSegmentDeliveryConfiguration }},
 {{ .HttpConfiguration }},
 {{ .SegmentDeliveryConfigurations }},
 {{ .SourceLocationName }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediatailor.source_locations
WHERE data__Identifier = '<SourceLocationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>source_locations</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateSourceLocation,
mediatailor:DescribeSourceLocation,
mediatailor:TagResource,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
kms:CreateGrant
```

### Delete
```json
mediatailor:DeleteSourceLocation,
mediatailor:DescribeSourceLocation
```

### List
```json
mediatailor:ListSourceLocations
```

