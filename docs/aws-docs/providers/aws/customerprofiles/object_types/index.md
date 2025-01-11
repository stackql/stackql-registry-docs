---
title: object_types
hide_title: false
hide_table_of_contents: false
keywords:
  - object_types
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

Creates, updates, deletes or gets an <code>object_type</code> resource or lists <code>object_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An ObjectType resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.object_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the profile object type.</td></tr>
<tr><td><CopyableCode code="allow_profile_creation" /></td><td><code>boolean</code></td><td>Indicates whether a profile should be created when data is received.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the profile object type.</td></tr>
<tr><td><CopyableCode code="encryption_key" /></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><CopyableCode code="expiration_days" /></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>A list of the name and ObjectType field.</td></tr>
<tr><td><CopyableCode code="keys" /></td><td><code>array</code></td><td>A list of unique keys that can be used to map data to the profile.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at.</td></tr>
<tr><td><CopyableCode code="source_last_updated_timestamp_format" /></td><td><code>string</code></td><td>The format of your sourceLastUpdatedTimestamp that was previously set up.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration.</td></tr>
<tr><td><CopyableCode code="template_id" /></td><td><code>string</code></td><td>A unique identifier for the object template.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html"><code>AWS::CustomerProfiles::ObjectType</code></a>.

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
    <td><CopyableCode code="DomainName, ObjectTypeName, Description, region" /></td>
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
Gets all <code>object_types</code> in a region.
```sql
SELECT
region,
domain_name,
object_type_name,
allow_profile_creation,
description,
encryption_key,
expiration_days,
fields,
keys,
created_at,
last_updated_at,
source_last_updated_timestamp_format,
tags,
template_id
FROM aws.customerprofiles.object_types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>object_type</code>.
```sql
SELECT
region,
domain_name,
object_type_name,
allow_profile_creation,
description,
encryption_key,
expiration_days,
fields,
keys,
created_at,
last_updated_at,
source_last_updated_timestamp_format,
tags,
template_id
FROM aws.customerprofiles.object_types
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<ObjectTypeName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>object_type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.customerprofiles.object_types (
 DomainName,
 ObjectTypeName,
 Description,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ ObjectTypeName }}',
 '{{ Description }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.customerprofiles.object_types (
 DomainName,
 ObjectTypeName,
 AllowProfileCreation,
 Description,
 EncryptionKey,
 ExpirationDays,
 Fields,
 Keys,
 SourceLastUpdatedTimestampFormat,
 Tags,
 TemplateId,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ ObjectTypeName }}',
 '{{ AllowProfileCreation }}',
 '{{ Description }}',
 '{{ EncryptionKey }}',
 '{{ ExpirationDays }}',
 '{{ Fields }}',
 '{{ Keys }}',
 '{{ SourceLastUpdatedTimestampFormat }}',
 '{{ Tags }}',
 '{{ TemplateId }}',
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
  - name: object_type
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: ObjectTypeName
        value: '{{ ObjectTypeName }}'
      - name: AllowProfileCreation
        value: '{{ AllowProfileCreation }}'
      - name: Description
        value: '{{ Description }}'
      - name: EncryptionKey
        value: '{{ EncryptionKey }}'
      - name: ExpirationDays
        value: '{{ ExpirationDays }}'
      - name: Fields
        value:
          - Name: '{{ Name }}'
            ObjectTypeField:
              Source: '{{ Source }}'
              Target: '{{ Target }}'
              ContentType: '{{ ContentType }}'
      - name: Keys
        value:
          - Name: '{{ Name }}'
            ObjectTypeKeyList:
              - FieldNames:
                  - '{{ FieldNames[0] }}'
                StandardIdentifiers:
                  - '{{ StandardIdentifiers[0] }}'
      - name: SourceLastUpdatedTimestampFormat
        value: '{{ SourceLastUpdatedTimestampFormat }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TemplateId
        value: '{{ TemplateId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.customerprofiles.object_types
WHERE data__Identifier = '<DomainName|ObjectTypeName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>object_types</code> resource, the following permissions are required:

### Create
```json
profile:GetProfileObjectType,
profile:PutProfileObjectType,
profile:TagResource
```

### Read
```json
profile:GetProfileObjectType
```

### Update
```json
profile:GetProfileObjectType,
profile:PutProfileObjectType,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteProfileObjectType
```

### List
```json
profile:ListProfileObjectTypes
```
