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


Used to retrieve a list of <code>model_cards</code> in a region or to create or delete a <code>model_cards</code> resource, use <code>model_card</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelCard.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_cards" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="model_card_name" /></td><td><code>string</code></td><td>The unique name of the model card.</td></tr>
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
model_card_name
FROM aws.sagemaker.model_cards
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>model_card</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- model_card.iql (required properties only)
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
-- model_card.iql (all properties)
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

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.model_cards
WHERE data__Identifier = '<ModelCardName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_cards</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelCard,
kms:DescribeKey,
kms:GenerateDataKey,
kms:CreateGrant,
sagemaker:DescribeModelPackageGroup,
sagemaker:DescribeModelPackage,
sagemaker:AddTags
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

