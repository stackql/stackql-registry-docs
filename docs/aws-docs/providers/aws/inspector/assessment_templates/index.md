---
title: assessment_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_templates
  - inspector
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


Used to retrieve a list of <code>assessment_templates</code> in a region or to create or delete a <code>assessment_templates</code> resource, use <code>assessment_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Inspector::AssessmentTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.inspector.assessment_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.inspector.assessment_templates
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
 "AssessmentTargetArn": "{{ AssessmentTargetArn }}",
 "DurationInSeconds": "{{ DurationInSeconds }}",
 "RulesPackageArns": [
  "{{ RulesPackageArns[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.inspector.assessment_templates (
 AssessmentTargetArn,
 DurationInSeconds,
 RulesPackageArns,
 region
)
SELECT 
{{ .AssessmentTargetArn }},
 {{ .DurationInSeconds }},
 {{ .RulesPackageArns }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssessmentTargetArn": "{{ AssessmentTargetArn }}",
 "DurationInSeconds": "{{ DurationInSeconds }}",
 "AssessmentTemplateName": "{{ AssessmentTemplateName }}",
 "RulesPackageArns": [
  "{{ RulesPackageArns[0] }}"
 ],
 "UserAttributesForFindings": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.inspector.assessment_templates (
 AssessmentTargetArn,
 DurationInSeconds,
 AssessmentTemplateName,
 RulesPackageArns,
 UserAttributesForFindings,
 region
)
SELECT 
 {{ .AssessmentTargetArn }},
 {{ .DurationInSeconds }},
 {{ .AssessmentTemplateName }},
 {{ .RulesPackageArns }},
 {{ .UserAttributesForFindings }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.inspector.assessment_templates
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assessment_templates</code> resource, the following permissions are required:

### Create
```json
inspector:CreateAssessmentTemplate,
inspector:ListAssessmentTemplates,
inspector:DescribeAssessmentTemplates
```

### Delete
```json
inspector:DeleteAssessmentTemplate
```

### List
```json
inspector:ListAssessmentTemplates
```

