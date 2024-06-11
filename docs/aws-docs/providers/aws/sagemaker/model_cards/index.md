---
title: model_cards
hide_title: false
hide_table_of_contents: false
keywords:
  - model_cards
  - sagemaker
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

Creates, updates, deletes or gets a <code>model_card</code> resource or lists <code>model_cards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelCard.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_cards" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="model_card_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the successfully created model card.</td></tr>
<tr><td><CopyableCode code="model_card_version" /></td><td><code>integer</code></td><td>A version of the model card.</td></tr>
<tr><td><CopyableCode code="model_card_name" /></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
<tr><td><CopyableCode code="security_config" /></td><td><code>An optional Key Management Service key to encrypt, decrypt, and re-encrypt model card content for regulated workloads with highly sensitive data.

</code></td><td></td></tr>
<tr><td><CopyableCode code="model_card_status" /></td><td><code>string</code></td><td>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>The content of the model card.</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the model card was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>The date and time the model card was last modified.</td></tr>
<tr><td><CopyableCode code="last_modified_by" /></td><td><code>object</code></td><td>Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.</td></tr>
<tr><td><CopyableCode code="model_card_processing_status" /></td><td><code>string</code></td><td>The processing status of model card deletion. The ModelCardProcessingStatus updates throughout the different deletion steps.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs used to manage metadata for model cards.</td></tr>
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
    <td><CopyableCode code="ModelCardName, Content, ModelCardStatus, region" /></td>
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
List all <code>model_cards</code> in a region.
```sql
SELECT
region,
model_card_name
FROM aws.sagemaker.model_cards
WHERE region = 'us-east-1';
```
Gets all properties from a <code>model_card</code>.
```sql
SELECT
region,
model_card_arn,
model_card_version,
model_card_name,
security_config,
model_card_status,
content,
creation_time,
created_by,
last_modified_time,
last_modified_by,
model_card_processing_status,
tags
FROM aws.sagemaker.model_cards
WHERE region = 'us-east-1' AND data__Identifier = '<ModelCardName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_card</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.model_cards (
 ModelCardName,
 ModelCardStatus,
 Content,
 region
)
SELECT 
'{{ ModelCardName }}',
 '{{ ModelCardStatus }}',
 '{{ Content }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.model_cards (
 ModelCardName,
 SecurityConfig,
 ModelCardStatus,
 Content,
 CreatedBy,
 LastModifiedBy,
 Tags,
 region
)
SELECT 
 '{{ ModelCardName }}',
 '{{ SecurityConfig }}',
 '{{ ModelCardStatus }}',
 '{{ Content }}',
 '{{ CreatedBy }}',
 '{{ LastModifiedBy }}',
 '{{ Tags }}',
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
  - name: model_card
    props:
      - name: ModelCardName
        value: '{{ ModelCardName }}'
      - name: SecurityConfig
        value:
          KmsKeyId: '{{ KmsKeyId }}'
      - name: ModelCardStatus
        value: '{{ ModelCardStatus }}'
      - name: Content
        value:
          ModelOverview:
            ModelDescription: '{{ ModelDescription }}'
            ModelOwner: '{{ ModelOwner }}'
            ModelCreator: '{{ ModelCreator }}'
            ProblemType: '{{ ProblemType }}'
            AlgorithmType: '{{ AlgorithmType }}'
            ModelId: '{{ ModelId }}'
            ModelArtifact:
              - '{{ ModelArtifact[0] }}'
            ModelName: '{{ ModelName }}'
            ModelVersion: null
            InferenceEnvironment:
              ContainerImage:
                - '{{ ContainerImage[0] }}'
          ModelPackageDetails:
            ModelPackageDescription: '{{ ModelPackageDescription }}'
            ModelPackageArn: '{{ ModelPackageArn }}'
            CreatedBy:
              UserProfileName: '{{ UserProfileName }}'
            ModelPackageStatus: '{{ ModelPackageStatus }}'
            ModelApprovalStatus: '{{ ModelApprovalStatus }}'
            ApprovalDescription: '{{ ApprovalDescription }}'
            ModelPackageGroupName: '{{ ModelPackageGroupName }}'
            ModelPackageName: '{{ ModelPackageName }}'
            ModelPackageVersion: null
            Domain: '{{ Domain }}'
            Task: '{{ Task }}'
            SourceAlgorithms:
              - AlgorithmName: '{{ AlgorithmName }}'
                ModelDataUrl: '{{ ModelDataUrl }}'
            InferenceSpecification:
              Containers:
                - ContainerHostname: '{{ ContainerHostname }}'
                  Environment: {}
                  ModelInput:
                    DataInputConfig: '{{ DataInputConfig }}'
                  Image: '{{ Image }}'
                  ImageDigest: '{{ ImageDigest }}'
                  ModelDataUrl: '{{ ModelDataUrl }}'
                  Framework: '{{ Framework }}'
                  FrameworkVersion: '{{ FrameworkVersion }}'
                  NearestModelName: '{{ NearestModelName }}'
              SupportedContentTypes:
                - '{{ SupportedContentTypes[0] }}'
              SupportedRealtimeInferenceInstanceTypes:
                - '{{ SupportedRealtimeInferenceInstanceTypes[0] }}'
              SupportedResponseMIMETypes:
                - '{{ SupportedResponseMIMETypes[0] }}'
              SupportedTransformInstanceTypes:
                - '{{ SupportedTransformInstanceTypes[0] }}'
          IntendedUses:
            PurposeOfModel: '{{ PurposeOfModel }}'
            IntendedUses: '{{ IntendedUses }}'
            FactorsAffectingModelEfficiency: '{{ FactorsAffectingModelEfficiency }}'
            RiskRating: '{{ RiskRating }}'
            ExplanationsForRiskRating: '{{ ExplanationsForRiskRating }}'
          BusinessDetails:
            BusinessProblem: '{{ BusinessProblem }}'
            BusinessStakeholders: '{{ BusinessStakeholders }}'
            LineOfBusiness: '{{ LineOfBusiness }}'
          TrainingDetails:
            ObjectiveFunction:
              Function:
                Function: '{{ Function }}'
                Facet: '{{ Facet }}'
                Condition: '{{ Condition }}'
              Notes: '{{ Notes }}'
            TrainingObservations: '{{ TrainingObservations }}'
            TrainingJobDetails:
              TrainingArn: '{{ TrainingArn }}'
              TrainingDatasets:
                - '{{ TrainingDatasets[0] }}'
              TrainingEnvironment:
                ContainerImage:
                  - '{{ ContainerImage[0] }}'
              TrainingMetrics:
                - Name: '{{ Name }}'
                  Notes: '{{ Notes }}'
                  Value: null
              UserProvidedTrainingMetrics:
                - null
              HyperParameters:
                - Name: '{{ Name }}'
                  Value: '{{ Value }}'
              UserProvidedHyperParameters:
                - null
          EvaluationDetails:
            - Name: '{{ Name }}'
              EvaluationObservation: '{{ EvaluationObservation }}'
              EvaluationJobArn: '{{ EvaluationJobArn }}'
              Datasets:
                - '{{ Datasets[0] }}'
              Metadata: {}
              MetricGroups:
                - Name: '{{ Name }}'
                  MetricData:
                    - null
          AdditionalInformation:
            EthicalConsiderations: '{{ EthicalConsiderations }}'
            CaveatsAndRecommendations: '{{ CaveatsAndRecommendations }}'
            CustomDetails: {}
      - name: CreatedBy
        value:
          UserProfileArn: '{{ UserProfileArn }}'
          UserProfileName: '{{ UserProfileName }}'
          DomainId: '{{ DomainId }}'
      - name: LastModifiedBy
        value: null
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.model_cards
WHERE data__Identifier = '<ModelCardName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_cards</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelCard,
sagemaker:DescribeModel,
kms:DescribeKey,
kms:GenerateDataKey,
kms:CreateGrant,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
sagemaker:AddTags
```

### Read
```json
sagemaker:DescribeModelCard,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
kms:Decrypt,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateModelCard,
sagemaker:DescribeModelCard,
sagemaker:DescribeModel,
kms:GenerateDataKey,
kms:Decrypt,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DescribeModelCard,
sagemaker:DeleteModelCard,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
kms:RetireGrant,
kms:Decrypt,
sagemaker:ListTags,
sagemaker:DeleteTags
```

### List
```json
sagemaker:ListModelCards,
sagemaker:ListModelCardVersions
```

