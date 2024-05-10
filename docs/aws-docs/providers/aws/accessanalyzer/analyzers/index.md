---
title: analyzers
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzers
  - accessanalyzer
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


Used to retrieve a list of <code>analyzers</code> in a region or to create or delete a <code>analyzers</code> resource, use <code>analyzer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.accessanalyzer.analyzers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the analyzer</td></tr>
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
FROM aws.accessanalyzer.analyzers
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
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.accessanalyzer.analyzers (
 Type,
 region
)
SELECT 
&#123;&#123; Type &#125;&#125;,
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AnalyzerName": "{{ AnalyzerName }}",
 "ArchiveRules": [
  {
   "Filter": [
    {
     "Contains": [
      "{{ Contains[0] }}"
     ],
     "Eq": [
      "{{ Eq[0] }}"
     ],
     "Exists": "{{ Exists }}",
     "Property": "{{ Property }}",
     "Neq": [
      "{{ Neq[0] }}"
     ]
    }
   ],
   "RuleName": "{{ RuleName }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Type": "{{ Type }}",
 "AnalyzerConfiguration": {
  "UnusedAccessConfiguration": {
   "UnusedAccessAge": "{{ UnusedAccessAge }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.accessanalyzer.analyzers (
 AnalyzerName,
 ArchiveRules,
 Tags,
 Type,
 AnalyzerConfiguration,
 region
)
SELECT 
 &#123;&#123; AnalyzerName &#125;&#125;,
 &#123;&#123; ArchiveRules &#125;&#125;,
 &#123;&#123; Tags &#125;&#125;,
 &#123;&#123; Type &#125;&#125;,
 &#123;&#123; AnalyzerConfiguration &#125;&#125;,
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.accessanalyzer.analyzers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>analyzers</code> resource, the following permissions are required:

### Create
```json
access-analyzer:CreateAnalyzer,
access-analyzer:TagResource,
iam:CreateServiceLinkedRole,
organizations:ListAWSServiceAccessForOrganization,
organizations:ListDelegatedAdministrators
```

### Delete
```json
access-analyzer:DeleteAnalyzer
```

### List
```json
access-analyzer:ListAnalyzers
```

