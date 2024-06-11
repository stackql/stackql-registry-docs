---
title: in_app_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - in_app_templates
  - pinpoint
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

Creates, updates, deletes or gets an <code>in_app_template</code> resource or lists <code>in_app_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>in_app_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Pinpoint::InAppTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pinpoint.in_app_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="layout" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="TemplateName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>in_app_templates</code> in a region.
```sql
SELECT
region,
template_name
FROM aws.pinpoint.in_app_templates
WHERE region = 'us-east-1';
```
Gets all properties from an <code>in_app_template</code>.
```sql
SELECT
region,
arn,
content,
custom_config,
layout,
tags,
template_description,
template_name
FROM aws.pinpoint.in_app_templates
WHERE region = 'us-east-1' AND data__Identifier = '<TemplateName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>in_app_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pinpoint.in_app_templates (
 TemplateName,
 region
)
SELECT 
'{{ TemplateName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pinpoint.in_app_templates (
 Content,
 CustomConfig,
 Layout,
 Tags,
 TemplateDescription,
 TemplateName,
 region
)
SELECT 
 '{{ Content }}',
 '{{ CustomConfig }}',
 '{{ Layout }}',
 '{{ Tags }}',
 '{{ TemplateDescription }}',
 '{{ TemplateName }}',
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
  - name: in_app_template
    props:
      - name: Content
        value:
          - BackgroundColor: '{{ BackgroundColor }}'
            BodyConfig:
              Alignment: '{{ Alignment }}'
              Body: '{{ Body }}'
              TextColor: '{{ TextColor }}'
            HeaderConfig:
              Alignment: null
              Header: '{{ Header }}'
              TextColor: '{{ TextColor }}'
            ImageUrl: '{{ ImageUrl }}'
            PrimaryBtn:
              Android:
                ButtonAction: '{{ ButtonAction }}'
                Link: '{{ Link }}'
              DefaultConfig:
                BackgroundColor: '{{ BackgroundColor }}'
                BorderRadius: '{{ BorderRadius }}'
                ButtonAction: null
                Link: '{{ Link }}'
                Text: '{{ Text }}'
                TextColor: '{{ TextColor }}'
              IOS: null
              Web: null
            SecondaryBtn: null
      - name: CustomConfig
        value: {}
      - name: Layout
        value: '{{ Layout }}'
      - name: Tags
        value: {}
      - name: TemplateDescription
        value: '{{ TemplateDescription }}'
      - name: TemplateName
        value: '{{ TemplateName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pinpoint.in_app_templates
WHERE data__Identifier = '<TemplateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>in_app_templates</code> resource, the following permissions are required:

### Create
```json
mobiletargeting:CreateInAppTemplate,
mobiletargeting:GetInAppTemplate,
mobiletargeting:TagResource
```

### Delete
```json
mobiletargeting:DeleteInAppTemplate,
mobiletargeting:GetInAppTemplate
```

### List
```json
mobiletargeting:GetInAppTemplate,
mobiletargeting:ListTemplates
```

### Read
```json
mobiletargeting:GetInAppTemplate,
mobiletargeting:ListTemplates
```

### Update
```json
mobiletargeting:UpdateInAppTemplate,
mobiletargeting:GetInAppTemplate
```

