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


Used to retrieve a list of <code>templates</code> in a region or to create or delete a <code>templates</code> resource, use <code>template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a template that defines certificate configurations, both for issuance and client handling</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
template_arn
FROM aws.pcaconnectorad.templates
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
 "ConnectorArn": "{{ ConnectorArn }}",
 "Definition": null,
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.pcaconnectorad.templates (
 ConnectorArn,
 Definition,
 Name,
 region
)
SELECT 
{{ .ConnectorArn }},
 {{ .Definition }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ConnectorArn": "{{ ConnectorArn }}",
 "Definition": null,
 "Name": "{{ Name }}",
 "ReenrollAllCertificateHolders": "{{ ReenrollAllCertificateHolders }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.pcaconnectorad.templates (
 ConnectorArn,
 Definition,
 Name,
 ReenrollAllCertificateHolders,
 Tags,
 region
)
SELECT 
 {{ .ConnectorArn }},
 {{ .Definition }},
 {{ .Name }},
 {{ .ReenrollAllCertificateHolders }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
pca-connector-ad:GetTemplate,
pca-connector-ad:DeleteTemplate
```

### List
```json
pca-connector-ad:ListTemplates
```

