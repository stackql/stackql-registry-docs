---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the project was created.</td></tr>
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

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html"><code>AWS::DataZone::Project</code></a>.

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
    <td><CopyableCode code="DomainIdentifier, Name, region" /></td>
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
Gets all <code>projects</code> in a region.
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
FROM aws.datazone.projects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>project</code>.
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
FROM aws.datazone.projects
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.projects (
 DomainIdentifier,
 Name,
 region
)
SELECT 
'{{ DomainIdentifier }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.projects (
 Description,
 DomainIdentifier,
 GlossaryTerms,
 Name,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DomainIdentifier }}',
 '{{ GlossaryTerms }}',
 '{{ Name }}',
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
  - name: project
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: GlossaryTerms
        value:
          - '{{ GlossaryTerms[0] }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.projects
WHERE data__Identifier = '<DomainId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
datazone:CreateProject,
datazone:GetProject
```

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

### List
```json
datazone:ListProjects
```
