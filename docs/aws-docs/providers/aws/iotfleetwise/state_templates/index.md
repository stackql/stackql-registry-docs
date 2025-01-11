---
title: state_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - state_templates
  - iotfleetwise
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

Creates, updates, deletes or gets a <code>state_template</code> resource or lists <code>state_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::StateTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.state_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_catalog_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_template_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="metadata_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-statetemplate.html"><code>AWS::IoTFleetWise::StateTemplate</code></a>.

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
    <td><CopyableCode code="Name, SignalCatalogArn, StateTemplateProperties, region" /></td>
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
Gets all <code>state_templates</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
signal_catalog_arn,
state_template_properties,
data_extra_dimensions,
metadata_extra_dimensions,
tags
FROM aws.iotfleetwise.state_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>state_template</code>.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
signal_catalog_arn,
state_template_properties,
data_extra_dimensions,
metadata_extra_dimensions,
tags
FROM aws.iotfleetwise.state_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>state_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotfleetwise.state_templates (
 Name,
 SignalCatalogArn,
 StateTemplateProperties,
 region
)
SELECT 
'{{ Name }}',
 '{{ SignalCatalogArn }}',
 '{{ StateTemplateProperties }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotfleetwise.state_templates (
 Description,
 Name,
 SignalCatalogArn,
 StateTemplateProperties,
 DataExtraDimensions,
 MetadataExtraDimensions,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ SignalCatalogArn }}',
 '{{ StateTemplateProperties }}',
 '{{ DataExtraDimensions }}',
 '{{ MetadataExtraDimensions }}',
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
  - name: state_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: SignalCatalogArn
        value: '{{ SignalCatalogArn }}'
      - name: StateTemplateProperties
        value:
          - '{{ StateTemplateProperties[0] }}'
      - name: DataExtraDimensions
        value:
          - '{{ DataExtraDimensions[0] }}'
      - name: MetadataExtraDimensions
        value:
          - '{{ MetadataExtraDimensions[0] }}'
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
DELETE FROM aws.iotfleetwise.state_templates
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_templates</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:GetStateTemplate,
iotfleetwise:CreateStateTemplate,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource
```

### Read
```json
iotfleetwise:GetStateTemplate,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:UpdateStateTemplate,
iotfleetwise:GetStateTemplate,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:DeleteStateTemplate,
iotfleetwise:GetStateTemplate
```

### List
```json
iotfleetwise:ListStateTemplates
```
