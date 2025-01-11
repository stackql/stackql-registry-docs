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

Creates, updates, deletes or gets a <code>calculated_attribute_definition</code> resource or lists <code>calculated_attribute_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calculated_attribute_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A calculated attribute definition for Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.calculated_attribute_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="calculated_attribute_name" /></td><td><code>string</code></td><td>The unique name of the calculated attribute.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the calculated attribute.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event trigger.</td></tr>
<tr><td><CopyableCode code="attribute_details" /></td><td><code>object</code></td><td>Mathematical expression and a list of attribute items specified in that expression.</td></tr>
<tr><td><CopyableCode code="conditions" /></td><td><code>object</code></td><td>The conditions including range, object count, and threshold for the calculated attribute.</td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td>The aggregation operation to perform for the calculated attribute.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was most recently edited.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html"><code>AWS::CustomerProfiles::CalculatedAttributeDefinition</code></a>.

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
    <td><CopyableCode code="DomainName, CalculatedAttributeName, AttributeDetails, Statistic, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>calculated_attribute_definitions</code> in a region.
```sql
SELECT
region,
domain_name,
calculated_attribute_name,
display_name,
description,
attribute_details,
conditions,
statistic,
created_at,
last_updated_at,
tags
FROM aws.customerprofiles.calculated_attribute_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>calculated_attribute_definition</code>.
```sql
SELECT
region,
domain_name,
calculated_attribute_name,
display_name,
description,
attribute_details,
conditions,
statistic,
created_at,
last_updated_at,
tags
FROM aws.customerprofiles.calculated_attribute_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<CalculatedAttributeName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>calculated_attribute_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.customerprofiles.calculated_attribute_definitions (
 DomainName,
 CalculatedAttributeName,
 AttributeDetails,
 Statistic,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ CalculatedAttributeName }}',
 '{{ AttributeDetails }}',
 '{{ Statistic }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ DomainName }}',
 '{{ CalculatedAttributeName }}',
 '{{ DisplayName }}',
 '{{ Description }}',
 '{{ AttributeDetails }}',
 '{{ Conditions }}',
 '{{ Statistic }}',
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
  - name: calculated_attribute_definition
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: CalculatedAttributeName
        value: '{{ CalculatedAttributeName }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Description
        value: '{{ Description }}'
      - name: AttributeDetails
        value:
          Attributes:
            - Name: '{{ Name }}'
          Expression: '{{ Expression }}'
      - name: Conditions
        value:
          Range:
            Value: '{{ Value }}'
            Unit: '{{ Unit }}'
          ObjectCount: '{{ ObjectCount }}'
          Threshold:
            Value: '{{ Value }}'
            Operator: '{{ Operator }}'
      - name: Statistic
        value: '{{ Statistic }}'
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

### Read
```json
profile:GetCalculatedAttributeDefinition
```

### Update
```json
profile:GetCalculatedAttributeDefinition,
profile:UpdateCalculatedAttributeDefinition,
profile:UntagResource,
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
