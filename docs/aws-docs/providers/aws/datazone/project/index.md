---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - datazone
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

Gets or operates on an individual <code>project</code> resource, use <code>projects</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.project" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the project was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created the project.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Amazon DataZone project.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the project was created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this project is created.</td></tr>
<tr><td><CopyableCode code="glossary_terms" /></td><td><code>array</code></td><td>The glossary terms that can be used in this Amazon DataZone project.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone project.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the project was last updated.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Amazon DataZone project.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
created_at,
created_by,
description,
domain_id,
domain_identifier,
glossary_terms,
id,
last_updated_at,
name
FROM aws.datazone.project
WHERE data__Identifier = '<DomainId>|<Id>';
```

## Permissions

To operate on the <code>project</code> resource, the following permissions are required:

### Read
```json
datazone:GetProject
```

### Update
```json
datazone:UpdateProject,
datazone:GetProject
```

### Delete
```json
datazone:DeleteProject,
datazone:GetProject
```
