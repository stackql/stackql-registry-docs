---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - amplifyuibuilder
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

Creates, updates, deletes or gets a <code>component</code> resource or lists <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Component Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.components" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="binding_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="children" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="component_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="events" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="overrides" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="variants" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>components</code> in a region.
```sql
SELECT
region,
app_id,
binding_properties,
children,
collection_properties,
component_type,
created_at,
environment_name,
events,
id,
modified_at,
name,
overrides,
properties,
schema_version,
source_id,
tags,
variants
FROM aws.amplifyuibuilder.components
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>component</code>.
```sql
SELECT
region,
app_id,
binding_properties,
children,
collection_properties,
component_type,
created_at,
environment_name,
events,
id,
modified_at,
name,
overrides,
properties,
schema_version,
source_id,
tags,
variants
FROM aws.amplifyuibuilder.components
WHERE region = 'us-east-1' AND data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>component</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.amplifyuibuilder.components (
 AppId,
 BindingProperties,
 Children,
 CollectionProperties,
 ComponentType,
 EnvironmentName,
 Events,
 Name,
 Overrides,
 Properties,
 SchemaVersion,
 SourceId,
 Tags,
 Variants,
 region
)
SELECT 
'{{ AppId }}',
 '{{ BindingProperties }}',
 '{{ Children }}',
 '{{ CollectionProperties }}',
 '{{ ComponentType }}',
 '{{ EnvironmentName }}',
 '{{ Events }}',
 '{{ Name }}',
 '{{ Overrides }}',
 '{{ Properties }}',
 '{{ SchemaVersion }}',
 '{{ SourceId }}',
 '{{ Tags }}',
 '{{ Variants }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.amplifyuibuilder.components (
 AppId,
 BindingProperties,
 Children,
 CollectionProperties,
 ComponentType,
 EnvironmentName,
 Events,
 Name,
 Overrides,
 Properties,
 SchemaVersion,
 SourceId,
 Tags,
 Variants,
 region
)
SELECT 
 '{{ AppId }}',
 '{{ BindingProperties }}',
 '{{ Children }}',
 '{{ CollectionProperties }}',
 '{{ ComponentType }}',
 '{{ EnvironmentName }}',
 '{{ Events }}',
 '{{ Name }}',
 '{{ Overrides }}',
 '{{ Properties }}',
 '{{ SchemaVersion }}',
 '{{ SourceId }}',
 '{{ Tags }}',
 '{{ Variants }}',
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
  - name: component
    props:
      - name: AppId
        value: '{{ AppId }}'
      - name: BindingProperties
        value: {}
      - name: Children
        value:
          - ComponentType: '{{ ComponentType }}'
            Name: '{{ Name }}'
            Properties: {}
            Children:
              - null
            Events: {}
            SourceId: '{{ SourceId }}'
      - name: CollectionProperties
        value: {}
      - name: ComponentType
        value: '{{ ComponentType }}'
      - name: EnvironmentName
        value: '{{ EnvironmentName }}'
      - name: Events
        value: null
      - name: Name
        value: '{{ Name }}'
      - name: Overrides
        value: {}
      - name: Properties
        value: null
      - name: SchemaVersion
        value: '{{ SchemaVersion }}'
      - name: SourceId
        value: '{{ SourceId }}'
      - name: Tags
        value: {}
      - name: Variants
        value:
          - VariantValues: {}
            Overrides: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.amplifyuibuilder.components
WHERE data__Identifier = '<AppId|EnvironmentName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>components</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplifyuibuilder:CreateComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:TagResource
```

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetComponent
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetComponent,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateComponent
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:UntagResource
```

### List
```json
amplify:GetApp,
amplifyuibuilder:ListComponents
```

