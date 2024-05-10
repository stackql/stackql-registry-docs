---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - databrew
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


Used to retrieve a list of <code>jobs</code> in a region or to create or delete a <code>jobs</code> resource, use <code>job</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.jobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Job name</td></tr>
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
name
FROM aws.databrew.jobs
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
 "Name": "{{ Name }}",
 "Type": "{{ Type }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.databrew.jobs (
 Name,
 Type,
 RoleArn,
 region
)
SELECT 
{{ Name }},
 {{ Type }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DatasetName": "{{ DatasetName }}",
 "EncryptionKeyArn": "{{ EncryptionKeyArn }}",
 "EncryptionMode": "{{ EncryptionMode }}",
 "Name": "{{ Name }}",
 "Type": "{{ Type }}",
 "LogSubscription": "{{ LogSubscription }}",
 "MaxCapacity": "{{ MaxCapacity }}",
 "MaxRetries": "{{ MaxRetries }}",
 "Outputs": [
  {
   "CompressionFormat": "{{ CompressionFormat }}",
   "Format": "{{ Format }}",
   "FormatOptions": {
    "Csv": {
     "Delimiter": "{{ Delimiter }}"
    }
   },
   "PartitionColumns": [
    "{{ PartitionColumns[0] }}"
   ],
   "Location": {
    "Bucket": "{{ Bucket }}",
    "Key": "{{ Key }}"
   },
   "Overwrite": "{{ Overwrite }}",
   "MaxOutputFiles": "{{ MaxOutputFiles }}"
  }
 ],
 "DataCatalogOutputs": [
  {
   "CatalogId": "{{ CatalogId }}",
   "DatabaseName": "{{ DatabaseName }}",
   "TableName": "{{ TableName }}",
   "S3Options": {
    "Location": null
   },
   "DatabaseOptions": {
    "TempDirectory": null,
    "TableName": "{{ TableName }}"
   },
   "Overwrite": "{{ Overwrite }}"
  }
 ],
 "DatabaseOutputs": [
  {
   "GlueConnectionName": "{{ GlueConnectionName }}",
   "DatabaseOutputMode": "{{ DatabaseOutputMode }}",
   "DatabaseOptions": null
  }
 ],
 "OutputLocation": {
  "Bucket": "{{ Bucket }}",
  "Key": "{{ Key }}",
  "BucketOwner": "{{ BucketOwner }}"
 },
 "ProjectName": "{{ ProjectName }}",
 "Recipe": {
  "Description": "{{ Description }}",
  "Name": "{{ Name }}",
  "Steps": [
   {
    "Action": {
     "Operation": "{{ Operation }}",
     "Parameters": null
    },
    "ConditionExpressions": [
     {
      "Condition": "{{ Condition }}",
      "Value": "{{ Value }}",
      "TargetColumn": "{{ TargetColumn }}"
     }
    ]
   }
  ],
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  null
 ],
 "Timeout": "{{ Timeout }}",
 "JobSample": {
  "Mode": "{{ Mode }}",
  "Size": "{{ Size }}"
 },
 "ProfileConfiguration": {
  "DatasetStatisticsConfiguration": {
   "IncludedStatistics": [
    "{{ IncludedStatistics[0] }}"
   ],
   "Overrides": [
    {
     "Statistic": null,
     "Parameters": {}
    }
   ]
  },
  "ProfileColumns": [
   {
    "Regex": "{{ Regex }}",
    "Name": "{{ Name }}"
   }
  ],
  "ColumnStatisticsConfigurations": [
   {
    "Selectors": [
     null
    ],
    "Statistics": null
   }
  ],
  "EntityDetectorConfiguration": {
   "EntityTypes": [
    "{{ EntityTypes[0] }}"
   ],
   "AllowedStatistics": {
    "Statistics": [
     null
    ]
   }
  }
 },
 "ValidationConfigurations": [
  {
   "RulesetArn": "{{ RulesetArn }}",
   "ValidationMode": "{{ ValidationMode }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.databrew.jobs (
 DatasetName,
 EncryptionKeyArn,
 EncryptionMode,
 Name,
 Type,
 LogSubscription,
 MaxCapacity,
 MaxRetries,
 Outputs,
 DataCatalogOutputs,
 DatabaseOutputs,
 OutputLocation,
 ProjectName,
 Recipe,
 RoleArn,
 Tags,
 Timeout,
 JobSample,
 ProfileConfiguration,
 ValidationConfigurations,
 region
)
SELECT 
 {{ DatasetName }},
 {{ EncryptionKeyArn }},
 {{ EncryptionMode }},
 {{ Name }},
 {{ Type }},
 {{ LogSubscription }},
 {{ MaxCapacity }},
 {{ MaxRetries }},
 {{ Outputs }},
 {{ DataCatalogOutputs }},
 {{ DatabaseOutputs }},
 {{ OutputLocation }},
 {{ ProjectName }},
 {{ Recipe }},
 {{ RoleArn }},
 {{ Tags }},
 {{ Timeout }},
 {{ JobSample }},
 {{ ProfileConfiguration }},
 {{ ValidationConfigurations }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.databrew.jobs
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>jobs</code> resource, the following permissions are required:

### Create
```json
databrew:CreateProfileJob,
databrew:CreateRecipeJob,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### Delete
```json
databrew:DeleteJob
```

### List
```json
databrew:ListJobs,
databrew:ListTagsForResource,
iam:ListRoles
```

