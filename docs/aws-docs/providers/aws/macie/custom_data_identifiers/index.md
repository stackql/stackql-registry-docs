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

Creates, updates, deletes or gets a <code>custom_data_identifier</code> resource or lists <code>custom_data_identifiers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie CustomDataIdentifier resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.custom_data_identifiers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of custom data identifier.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of custom data identifier.</td></tr>
<tr><td><CopyableCode code="regex" /></td><td><code>string</code></td><td>Regular expression for custom data identifier.</td></tr>
<tr><td><CopyableCode code="maximum_match_distance" /></td><td><code>integer</code></td><td>Maximum match distance.</td></tr>
<tr><td><CopyableCode code="keywords" /></td><td><code>array</code></td><td>Keywords to be matched against.</td></tr>
<tr><td><CopyableCode code="ignore_words" /></td><td><code>array</code></td><td>Words to be ignored.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Custom data identifier ARN.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="Name, Regex, region" /></td>
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
Gets all <code>custom_data_identifiers</code> in a region.
```sql
SELECT
region,
name,
description,
regex,
maximum_match_distance,
keywords,
ignore_words,
id,
arn,
tags
FROM aws.macie.custom_data_identifiers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_data_identifier</code>.
```sql
SELECT
region,
name,
description,
regex,
maximum_match_distance,
keywords,
ignore_words,
id,
arn,
tags
FROM aws.macie.custom_data_identifiers
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_data_identifier</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
macie2:GetCustomDataIdentifier
```

### Delete
```json
macie2:DeleteCustomDataIdentifier
```

### List
```json
macie2:ListCustomDataIdentifiers
```

### Update
```json
macie2:TagResource,
macie2:UntagResource
```

