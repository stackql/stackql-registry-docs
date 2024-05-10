---
title: matching_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - matching_workflows
  - entityresolution
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


Used to retrieve a list of <code>matching_workflows</code> in a region or to create or delete a <code>matching_workflows</code> resource, use <code>matching_workflow</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matching_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>MatchingWorkflow defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.matching_workflows" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>undefined</code></td><td>The name of the MatchingWorkflow</td></tr>
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
workflow_name
FROM aws.entityresolution.matching_workflows
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
 "WorkflowName": "{{ WorkflowName }}",
 "InputSourceConfig": [
  {
   "InputSourceARN": "{{ InputSourceARN }}",
   "SchemaArn": "{{ SchemaArn }}",
   "ApplyNormalization": "{{ ApplyNormalization }}"
  }
 ],
 "OutputSourceConfig": [
  {
   "OutputS3Path": "{{ OutputS3Path }}",
   "Output": [
    {
     "Name": "{{ Name }}",
     "Hashed": "{{ Hashed }}"
    }
   ],
   "KMSArn": "{{ KMSArn }}",
   "ApplyNormalization": "{{ ApplyNormalization }}"
  }
 ],
 "ResolutionTechniques": {
  "ResolutionType": "{{ ResolutionType }}",
  "RuleBasedProperties": {
   "Rules": [
    {
     "RuleName": "{{ RuleName }}",
     "MatchingKeys": [
      null
     ]
    }
   ],
   "AttributeMatchingModel": "{{ AttributeMatchingModel }}"
  },
  "ProviderProperties": {
   "ProviderServiceArn": "{{ ProviderServiceArn }}",
   "ProviderConfiguration": {},
   "IntermediateSourceConfiguration": {
    "IntermediateS3Path": "{{ IntermediateS3Path }}"
   }
  }
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.entityresolution.matching_workflows (
 WorkflowName,
 InputSourceConfig,
 OutputSourceConfig,
 ResolutionTechniques,
 RoleArn,
 region
)
SELECT 
{{ WorkflowName }},
 {{ InputSourceConfig }},
 {{ OutputSourceConfig }},
 {{ ResolutionTechniques }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "WorkflowName": "{{ WorkflowName }}",
 "Description": "{{ Description }}",
 "InputSourceConfig": [
  {
   "InputSourceARN": "{{ InputSourceARN }}",
   "SchemaArn": "{{ SchemaArn }}",
   "ApplyNormalization": "{{ ApplyNormalization }}"
  }
 ],
 "OutputSourceConfig": [
  {
   "OutputS3Path": "{{ OutputS3Path }}",
   "Output": [
    {
     "Name": "{{ Name }}",
     "Hashed": "{{ Hashed }}"
    }
   ],
   "KMSArn": "{{ KMSArn }}",
   "ApplyNormalization": "{{ ApplyNormalization }}"
  }
 ],
 "ResolutionTechniques": {
  "ResolutionType": "{{ ResolutionType }}",
  "RuleBasedProperties": {
   "Rules": [
    {
     "RuleName": "{{ RuleName }}",
     "MatchingKeys": [
      null
     ]
    }
   ],
   "AttributeMatchingModel": "{{ AttributeMatchingModel }}"
  },
  "ProviderProperties": {
   "ProviderServiceArn": "{{ ProviderServiceArn }}",
   "ProviderConfiguration": {},
   "IntermediateSourceConfiguration": {
    "IntermediateS3Path": "{{ IntermediateS3Path }}"
   }
  }
 },
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.entityresolution.matching_workflows (
 WorkflowName,
 Description,
 InputSourceConfig,
 OutputSourceConfig,
 ResolutionTechniques,
 RoleArn,
 Tags,
 region
)
SELECT 
 {{ WorkflowName }},
 {{ Description }},
 {{ InputSourceConfig }},
 {{ OutputSourceConfig }},
 {{ ResolutionTechniques }},
 {{ RoleArn }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.entityresolution.matching_workflows
WHERE data__Identifier = '<WorkflowName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>matching_workflows</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateMatchingWorkflow,
entityresolution:GetMatchingWorkflow,
entityresolution:TagResource,
kms:CreateGrant,
kms:DescribeKey,
iam:PassRole
```

### Delete
```json
entityresolution:DeleteMatchingWorkflow,
entityresolution:GetMatchingWorkflow,
entityresolution:UntagResource
```

### List
```json
entityresolution:ListMatchingWorkflows
```

