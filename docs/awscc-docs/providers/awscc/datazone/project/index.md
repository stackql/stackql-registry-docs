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
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the project was created.</td></tr>
<tr><td><code>created_by</code></td><td><code>string</code></td><td>The Amazon DataZone user who created the project.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the Amazon DataZone project.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the project was created.</td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this project is created.</td></tr>
<tr><td><code>glossary_terms</code></td><td><code>array</code></td><td>The glossary terms that can be used in this Amazon DataZone project.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone project.</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The timestamp of when the project was last updated.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Amazon DataZone project.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.datazone.project
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

