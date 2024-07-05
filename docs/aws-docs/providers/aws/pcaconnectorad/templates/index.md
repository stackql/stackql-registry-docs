---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - pcaconnectorad
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

Creates, updates, deletes or gets a <code>template</code> resource or lists <code>templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a template that defines certificate configurations, both for issuance and client handling</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="reenroll_all_certificate_holders" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ConnectorArn, Definition, Name, region" /></td>
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
Gets all <code>templates</code> in a region.
```sql
SELECT
region,
connector_arn,
definition,
name,
reenroll_all_certificate_holders,
tags,
template_arn
FROM aws.pcaconnectorad.templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>template</code>.
```sql
SELECT
region,
connector_arn,
definition,
name,
reenroll_all_certificate_holders,
tags,
template_arn
FROM aws.pcaconnectorad.templates
WHERE region = 'us-east-1' AND data__Identifier = '<TemplateArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pcaconnectorad.templates (
 ConnectorArn,
 Definition,
 Name,
 region
)
SELECT 
'{{ ConnectorArn }}',
 '{{ Definition }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorad.templates (
 ConnectorArn,
 Definition,
 Name,
 ReenrollAllCertificateHolders,
 Tags,
 region
)
SELECT 
 '{{ ConnectorArn }}',
 '{{ Definition }}',
 '{{ Name }}',
 '{{ ReenrollAllCertificateHolders }}',
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
  - name: template
    props:
      - name: ConnectorArn
        value: '{{ ConnectorArn }}'
      - name: Definition
        value: null
      - name: Name
        value: '{{ Name }}'
      - name: ReenrollAllCertificateHolders
        value: '{{ ReenrollAllCertificateHolders }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcaconnectorad.templates
WHERE data__Identifier = '<TemplateArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>templates</code> resource, the following permissions are required:

### Create
```json
pca-connector-ad:CreateTemplate
```

### Read
```json
pca-connector-ad:GetTemplate,
pca-connector-ad:ListTagsForResource
```

### Update
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource,
pca-connector-ad:UpdateTemplate
```

### Delete
```json
pca-connector-ad:GetTemplate,
pca-connector-ad:DeleteTemplate
```

### List
```json
pca-connector-ad:ListTemplates
```

