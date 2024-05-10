---
title: document_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - document_classifiers
  - comprehend
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


Used to retrieve a list of <code>document_classifiers</code> in a region or to create or delete a <code>document_classifiers</code> resource, use <code>document_classifier</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Document Classifier enables training document classifier models.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.document_classifiers" /></td></tr>
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
FROM aws.comprehend.document_classifiers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>document_classifier</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- document_classifier.iql (required properties only)
INSERT INTO aws.comprehend.document_classifiers (
 DataAccessRoleArn,
 InputDataConfig,
 LanguageCode,
 DocumentClassifierName,
 region
)
SELECT 
'{{ DataAccessRoleArn }}',
 '{{ InputDataConfig }}',
 '{{ LanguageCode }}',
 '{{ DocumentClassifierName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- document_classifier.iql (all properties)
INSERT INTO aws.comprehend.document_classifiers (
 DataAccessRoleArn,
 InputDataConfig,
 OutputDataConfig,
 LanguageCode,
 ModelKmsKeyId,
 ModelPolicy,
 DocumentClassifierName,
 Mode,
 Tags,
 VersionName,
 VolumeKmsKeyId,
 VpcConfig,
 region
)
SELECT 
 '{{ DataAccessRoleArn }}',
 '{{ InputDataConfig }}',
 '{{ OutputDataConfig }}',
 '{{ LanguageCode }}',
 '{{ ModelKmsKeyId }}',
 '{{ ModelPolicy }}',
 '{{ DocumentClassifierName }}',
 '{{ Mode }}',
 '{{ Tags }}',
 '{{ VersionName }}',
 '{{ VolumeKmsKeyId }}',
 '{{ VpcConfig }}',
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
  - name: document_classifier
    props:
      - name: DataAccessRoleArn
        value: '{{ DataAccessRoleArn }}'
      - name: InputDataConfig
        value:
          AugmentedManifests:
            - AttributeNames:
                - '{{ AttributeNames[0] }}'
              S3Uri: '{{ S3Uri }}'
              Split: '{{ Split }}'
          DataFormat: '{{ DataFormat }}'
          LabelDelimiter: '{{ LabelDelimiter }}'
          DocumentType: '{{ DocumentType }}'
          Documents:
            S3Uri: null
            TestS3Uri: null
          DocumentReaderConfig:
            DocumentReadAction: '{{ DocumentReadAction }}'
            DocumentReadMode: '{{ DocumentReadMode }}'
            FeatureTypes:
              - '{{ FeatureTypes[0] }}'
          S3Uri: null
          TestS3Uri: null
      - name: OutputDataConfig
        value:
          KmsKeyId: '{{ KmsKeyId }}'
          S3Uri: null
      - name: LanguageCode
        value: '{{ LanguageCode }}'
      - name: ModelKmsKeyId
        value: null
      - name: ModelPolicy
        value: '{{ ModelPolicy }}'
      - name: DocumentClassifierName
        value: '{{ DocumentClassifierName }}'
      - name: Mode
        value: '{{ Mode }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VersionName
        value: '{{ VersionName }}'
      - name: VolumeKmsKeyId
        value: null
      - name: VpcConfig
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          Subnets:
            - '{{ Subnets[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.comprehend.document_classifiers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>document_classifiers</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
comprehend:CreateDocumentClassifier,
comprehend:DescribeDocumentClassifier,
comprehend:DescribeResourcePolicy,
comprehend:ListTagsForResource,
textract:DetectDocumentText
```

### Delete
```json
comprehend:DescribeDocumentClassifier,
comprehend:DeleteDocumentClassifier
```

### List
```json
comprehend:ListDocumentClassifiers
```

