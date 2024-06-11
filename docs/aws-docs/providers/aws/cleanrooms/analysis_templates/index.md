---
title: analysis_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_templates
  - cleanrooms
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

Creates, updates, deletes or gets an <code>analysis_template</code> resource or lists <code>analysis_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a stored analysis within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.analysis_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms analysis template.</td></tr>
<tr><td><CopyableCode code="analysis_parameters" /></td><td><code>array</code></td><td>The member who can query can provide this placeholder for a literal data value in an analysis template</td></tr>
<tr><td><CopyableCode code="analysis_template_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Source, Format, Name, MembershipIdentifier, region" /></td>
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
List all <code>analysis_templates</code> in a region.
```sql
SELECT
region,
analysis_template_identifier,
membership_identifier
FROM aws.cleanrooms.analysis_templates
WHERE region = 'us-east-1';
```
Gets all properties from an <code>analysis_template</code>.
```sql
SELECT
region,
arn,
collaboration_arn,
collaboration_identifier,
tags,
analysis_parameters,
analysis_template_identifier,
description,
membership_arn,
membership_identifier,
name,
schema,
source,
format
FROM aws.cleanrooms.analysis_templates
WHERE region = 'us-east-1' AND data__Identifier = '<AnalysisTemplateIdentifier>|<MembershipIdentifier>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>analysis_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cleanrooms.analysis_templates (
 MembershipIdentifier,
 Name,
 Source,
 Format,
 region
)
SELECT 
'{{ MembershipIdentifier }}',
 '{{ Name }}',
 '{{ Source }}',
 '{{ Format }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanrooms.analysis_templates (
 Tags,
 AnalysisParameters,
 Description,
 MembershipIdentifier,
 Name,
 Source,
 Format,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ AnalysisParameters }}',
 '{{ Description }}',
 '{{ MembershipIdentifier }}',
 '{{ Name }}',
 '{{ Source }}',
 '{{ Format }}',
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
  - name: analysis_template
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AnalysisParameters
        value:
          - DefaultValue: '{{ DefaultValue }}'
            Name: '{{ Name }}'
            Type: '{{ Type }}'
      - name: Description
        value: '{{ Description }}'
      - name: MembershipIdentifier
        value: '{{ MembershipIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: Source
        value:
          Text: '{{ Text }}'
      - name: Format
        value: '{{ Format }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cleanrooms.analysis_templates
WHERE data__Identifier = '<AnalysisTemplateIdentifier|MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>analysis_templates</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateAnalysisTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListAnalysisTemplates
```

### Read
```json
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdateAnalysisTemplate,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource
```

### Delete
```json
cleanrooms:DeleteAnalysisTemplate,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListAnalysisTemplates,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```

### List
```json
cleanrooms:ListAnalysisTemplates
```

