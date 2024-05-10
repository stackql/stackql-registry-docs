---
title: calculated_attribute_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - calculated_attribute_definitions
  - customerprofiles
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


Used to retrieve a list of <code>calculated_attribute_definitions</code> in a region or to create or delete a <code>calculated_attribute_definitions</code> resource, use <code>calculated_attribute_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calculated_attribute_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A calculated attribute definition for Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.calculated_attribute_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="calculated_attribute_name" /></td><td><code>undefined</code></td><td></td></tr>
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
domain_name,
calculated_attribute_name
FROM aws.customerprofiles.calculated_attribute_definitions
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
 "DomainName": "{{ DomainName }}",
 "CalculatedAttributeName": "{{ CalculatedAttributeName }}",
 "AttributeDetails": {
  "Attributes": [
   {
    "Name": "{{ Name }}"
   }
  ],
  "Expression": "{{ Expression }}"
 },
 "Statistic": "{{ Statistic }}"
}
>>>
--required properties only
INSERT INTO aws.customerprofiles.calculated_attribute_definitions (
 DomainName,
 CalculatedAttributeName,
 AttributeDetails,
 Statistic,
 region
)
SELECT 
{{ DomainName }},
 {{ CalculatedAttributeName }},
 {{ AttributeDetails }},
 {{ Statistic }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DomainName": "{{ DomainName }}",
 "CalculatedAttributeName": "{{ CalculatedAttributeName }}",
 "DisplayName": "{{ DisplayName }}",
 "Description": "{{ Description }}",
 "AttributeDetails": {
  "Attributes": [
   {
    "Name": "{{ Name }}"
   }
  ],
  "Expression": "{{ Expression }}"
 },
 "Conditions": {
  "Range": {
   "Value": "{{ Value }}",
   "Unit": "{{ Unit }}"
  },
  "ObjectCount": "{{ ObjectCount }}",
  "Threshold": {
   "Value": "{{ Value }}",
   "Operator": "{{ Operator }}"
  }
 },
 "Statistic": "{{ Statistic }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.customerprofiles.calculated_attribute_definitions (
 DomainName,
 CalculatedAttributeName,
 DisplayName,
 Description,
 AttributeDetails,
 Conditions,
 Statistic,
 Tags,
 region
)
SELECT 
 {{ DomainName }},
 {{ CalculatedAttributeName }},
 {{ DisplayName }},
 {{ Description }},
 {{ AttributeDetails }},
 {{ Conditions }},
 {{ Statistic }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.customerprofiles.calculated_attribute_definitions
WHERE data__Identifier = '<DomainName|CalculatedAttributeName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>calculated_attribute_definitions</code> resource, the following permissions are required:

### Create
```json
profile:CreateCalculatedAttributeDefinition,
profile:TagResource
```

### Delete
```json
profile:DeleteCalculatedAttributeDefinition
```

### List
```json
profile:ListCalculatedAttributeDefinitions
```

