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

Creates, updates, deletes or gets an <code>analyzer</code> resource or lists <code>analyzers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.accessanalyzer.analyzers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="analyzer_name" /></td><td><code>string</code></td><td>Analyzer name</td></tr>
<tr><td><CopyableCode code="archive_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the analyzer</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS</td></tr>
<tr><td><CopyableCode code="analyzer_configuration" /></td><td><code>object</code></td><td>The configuration for the analyzer</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html"><code>AWS::AccessAnalyzer::Analyzer</code></a>.

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
    <td><CopyableCode code="Type, region" /></td>
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
Gets all <code>analyzers</code> in a region.
```sql
SELECT
region,
analyzer_name,
archive_rules,
arn,
tags,
type,
analyzer_configuration
FROM aws.accessanalyzer.analyzers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>analyzer</code>.
```sql
SELECT
region,
analyzer_name,
archive_rules,
arn,
tags,
type,
analyzer_configuration
FROM aws.accessanalyzer.analyzers
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>analyzer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.accessanalyzer.analyzers (
 Type,
 region
)
SELECT 
'{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.accessanalyzer.analyzers (
 AnalyzerName,
 ArchiveRules,
 Tags,
 Type,
 AnalyzerConfiguration,
 region
)
SELECT 
 '{{ AnalyzerName }}',
 '{{ ArchiveRules }}',
 '{{ Tags }}',
 '{{ Type }}',
 '{{ AnalyzerConfiguration }}',
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
  - name: analyzer
    props:
      - name: AnalyzerName
        value: '{{ AnalyzerName }}'
      - name: ArchiveRules
        value:
          - Filter:
              - Contains:
                  - '{{ Contains[0] }}'
                Eq:
                  - '{{ Eq[0] }}'
                Exists: '{{ Exists }}'
                Property: '{{ Property }}'
                Neq:
                  - '{{ Neq[0] }}'
            RuleName: '{{ RuleName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'
      - name: AnalyzerConfiguration
        value:
          UnusedAccessConfiguration:
            UnusedAccessAge: '{{ UnusedAccessAge }}'
            AnalysisRule:
              Exclusions:
                - AccountIds:
                    - '{{ AccountIds[0] }}'
                  ResourceTags:
                    - - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
access-analyzer:ListAnalyzers,
access-analyzer:GetAnalyzer,
access-analyzer:ListArchiveRules
```

### Update
```json
access-analyzer:CreateArchiveRule,
access-analyzer:DeleteArchiveRule,
access-analyzer:ListAnalyzers,
access-analyzer:TagResource,
access-analyzer:UntagResource,
access-analyzer:UpdateAnalyzer,
access-analyzer:UpdateArchiveRule
```

### Delete
```json
access-analyzer:DeleteAnalyzer
```

### List
```json
access-analyzer:ListAnalyzers
```
