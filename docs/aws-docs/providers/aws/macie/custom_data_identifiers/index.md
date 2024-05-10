---
title: custom_data_identifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_identifiers
  - macie
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


Used to retrieve a list of <code>custom_data_identifiers</code> in a region or to create or delete a <code>custom_data_identifiers</code> resource, use <code>custom_data_identifier</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie CustomDataIdentifier resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.custom_data_identifiers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr>
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
FROM aws.macie.custom_data_identifiers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>custom_data_identifier</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- custom_data_identifier.iql (required properties only)
INSERT INTO aws.macie.custom_data_identifiers (
 Name,
 Regex,
 region
)
SELECT 
'{{ Name }}',
 '{{ Regex }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- custom_data_identifier.iql (all properties)
INSERT INTO aws.macie.custom_data_identifiers (
 Name,
 Description,
 Regex,
 MaximumMatchDistance,
 Keywords,
 IgnoreWords,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Regex }}',
 '{{ MaximumMatchDistance }}',
 '{{ Keywords }}',
 '{{ IgnoreWords }}',
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
  - name: custom_data_identifier
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Regex
        value: '{{ Regex }}'
      - name: MaximumMatchDistance
        value: '{{ MaximumMatchDistance }}'
      - name: Keywords
        value:
          - '{{ Keywords[0] }}'
      - name: IgnoreWords
        value:
          - '{{ IgnoreWords[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.macie.custom_data_identifiers
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_data_identifiers</code> resource, the following permissions are required:

### Create
```json
macie2:CreateCustomDataIdentifier,
macie2:GetCustomDataIdentifier,
macie2:TagResource
```

### Delete
```json
macie2:DeleteCustomDataIdentifier
```

### List
```json
macie2:ListCustomDataIdentifiers
```

