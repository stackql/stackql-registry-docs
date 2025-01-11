---
title: extension_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_associations
  - appconfig
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

Creates, updates, deletes or gets an <code>extension_association</code> resource or lists <code>extension_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extension_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.extension_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_version_number" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html"><code>AWS::AppConfig::ExtensionAssociation</code></a>.

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
Gets all <code>extension_associations</code> in a region.
```sql
SELECT
region,
id,
arn,
extension_arn,
resource_arn,
extension_identifier,
resource_identifier,
extension_version_number,
parameters,
tags
FROM aws.appconfig.extension_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>extension_association</code>.
```sql
SELECT
region,
id,
arn,
extension_arn,
resource_arn,
extension_identifier,
resource_identifier,
extension_version_number,
parameters,
tags
FROM aws.appconfig.extension_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extension_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appconfig.extension_associations (
 ExtensionIdentifier,
 ResourceIdentifier,
 ExtensionVersionNumber,
 Parameters,
 Tags,
 region
)
SELECT 
'{{ ExtensionIdentifier }}',
 '{{ ResourceIdentifier }}',
 '{{ ExtensionVersionNumber }}',
 '{{ Parameters }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.extension_associations (
 ExtensionIdentifier,
 ResourceIdentifier,
 ExtensionVersionNumber,
 Parameters,
 Tags,
 region
)
SELECT 
 '{{ ExtensionIdentifier }}',
 '{{ ResourceIdentifier }}',
 '{{ ExtensionVersionNumber }}',
 '{{ Parameters }}',
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
  - name: extension_association
    props:
      - name: ExtensionIdentifier
        value: '{{ ExtensionIdentifier }}'
      - name: ResourceIdentifier
        value: '{{ ResourceIdentifier }}'
      - name: ExtensionVersionNumber
        value: '{{ ExtensionVersionNumber }}'
      - name: Parameters
        value: {}
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
DELETE FROM aws.appconfig.extension_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>extension_associations</code> resource, the following permissions are required:

### Create
```json
appconfig:CreateExtensionAssociation,
appconfig:TagResource
```

### Read
```json
appconfig:GetExtensionAssociation
```

### Update
```json
appconfig:UpdateExtensionAssociation,
appconfig:TagResource,
appconfig:UntagResource
```

### Delete
```json
appconfig:DeleteExtensionAssociation,
appconfig:UntagResource
```

### List
```json
appconfig:ListExtensionAssociations
```
