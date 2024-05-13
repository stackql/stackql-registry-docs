---
title: model_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - model_packages
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


Used to retrieve a list of <code>model_packages</code> in a region or to create or delete a <code>model_packages</code> resource, use <code>model_package</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackage</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_packages" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="model_package_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
model_package_arn
FROM aws.sagemaker.model_packages
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>model_package</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.model_packages (
 Tags,
 AdditionalInferenceSpecifications,
 CertifyForMarketplace,
 ClientToken,
 CustomerMetadataProperties,
 Domain,
 DriftCheckBaselines,
 InferenceSpecification,
 MetadataProperties,
 ModelApprovalStatus,
 ModelMetrics,
 ModelPackageDescription,
 ModelPackageGroupName,
 ModelPackageName,
 SamplePayloadUrl,
 SkipModelValidation,
 SourceAlgorithmSpecification,
 Task,
 ValidationSpecification,
 ApprovalDescription,
 LastModifiedTime,
 ModelPackageVersion,
 AdditionalInferenceSpecificationsToAdd,
 ModelPackageStatusDetails,
 region
)
SELECT 
'{{ Tags }}',
 '{{ AdditionalInferenceSpecifications }}',
 '{{ CertifyForMarketplace }}',
 '{{ ClientToken }}',
 '{{ CustomerMetadataProperties }}',
 '{{ Domain }}',
 '{{ DriftCheckBaselines }}',
 '{{ InferenceSpecification }}',
 '{{ MetadataProperties }}',
 '{{ ModelApprovalStatus }}',
 '{{ ModelMetrics }}',
 '{{ ModelPackageDescription }}',
 '{{ ModelPackageGroupName }}',
 '{{ ModelPackageName }}',
 '{{ SamplePayloadUrl }}',
 '{{ SkipModelValidation }}',
 '{{ SourceAlgorithmSpecification }}',
 '{{ Task }}',
 '{{ ValidationSpecification }}',
 '{{ ApprovalDescription }}',
 '{{ LastModifiedTime }}',
 '{{ ModelPackageVersion }}',
 '{{ AdditionalInferenceSpecificationsToAdd }}',
 '{{ ModelPackageStatusDetails }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.model_packages (
 Tags,
 AdditionalInferenceSpecifications,
 CertifyForMarketplace,
 ClientToken,
 CustomerMetadataProperties,
 Domain,
 DriftCheckBaselines,
 InferenceSpecification,
 MetadataProperties,
 ModelApprovalStatus,
 ModelMetrics,
 ModelPackageDescription,
 ModelPackageGroupName,
 ModelPackageName,
 SamplePayloadUrl,
 SkipModelValidation,
 SourceAlgorithmSpecification,
 Task,
 ValidationSpecification,
 ApprovalDescription,
 LastModifiedTime,
 ModelPackageVersion,
 AdditionalInferenceSpecificationsToAdd,
 ModelPackageStatusDetails,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ AdditionalInferenceSpecifications }}',
 '{{ CertifyForMarketplace }}',
 '{{ ClientToken }}',
 '{{ CustomerMetadataProperties }}',
 '{{ Domain }}',
 '{{ DriftCheckBaselines }}',
 '{{ InferenceSpecification }}',
 '{{ MetadataProperties }}',
 '{{ ModelApprovalStatus }}',
 '{{ ModelMetrics }}',
 '{{ ModelPackageDescription }}',
 '{{ ModelPackageGroupName }}',
 '{{ ModelPackageName }}',
 '{{ SamplePayloadUrl }}',
 '{{ SkipModelValidation }}',
 '{{ SourceAlgorithmSpecification }}',
 '{{ Task }}',
 '{{ ValidationSpecification }}',
 '{{ ApprovalDescription }}',
 '{{ LastModifiedTime }}',
 '{{ ModelPackageVersion }}',
 '{{ AdditionalInferenceSpecificationsToAdd }}',
 '{{ ModelPackageStatusDetails }}',
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
  - name: model_package
    props:
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: AdditionalInferenceSpecifications
        value:
          - Containers:
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
            Description: '{{ Description }}'
            Name: '{{ Name }}'
            SupportedContentTypes:
              - '{{ SupportedContentTypes[0] }}'
            SupportedRealtimeInferenceInstanceTypes:
              - '{{ SupportedRealtimeInferenceInstanceTypes[0] }}'
            SupportedResponseMIMETypes:
              - '{{ SupportedResponseMIMETypes[0] }}'
            SupportedTransformInstanceTypes:
              - '{{ SupportedTransformInstanceTypes[0] }}'
      - name: CertifyForMarketplace
        value: '{{ CertifyForMarketplace }}'
      - name: ClientToken
        value: '{{ ClientToken }}'
      - name: CustomerMetadataProperties
        value: {}
      - name: Domain
        value: '{{ Domain }}'
      - name: DriftCheckBaselines
        value:
          Bias:
            PostTrainingConstraints:
              ContentDigest: '{{ ContentDigest }}'
              ContentType: '{{ ContentType }}'
              S3Uri: '{{ S3Uri }}'
            PreTrainingConstraints: null
            ConfigFile:
              ContentDigest: '{{ ContentDigest }}'
              ContentType: '{{ ContentType }}'
              S3Uri: '{{ S3Uri }}'
          Explainability:
            Constraints: null
            ConfigFile: null
          ModelDataQuality:
            Constraints: null
            Statistics: null
          ModelQuality:
            Constraints: null
            Statistics: null
      - name: InferenceSpecification
        value:
          Containers:
            - null
          SupportedContentTypes:
            - null
          SupportedRealtimeInferenceInstanceTypes:
            - null
          SupportedResponseMIMETypes:
            - null
          SupportedTransformInstanceTypes:
            - null
      - name: MetadataProperties
        value:
          CommitId: '{{ CommitId }}'
          GeneratedBy: '{{ GeneratedBy }}'
          ProjectId: '{{ ProjectId }}'
          Repository: '{{ Repository }}'
      - name: ModelApprovalStatus
        value: '{{ ModelApprovalStatus }}'
      - name: ModelMetrics
        value:
          Bias:
            Report: null
            PreTrainingReport: null
            PostTrainingReport: null
          Explainability:
            Report: null
          ModelDataQuality:
            Constraints: null
            Statistics: null
          ModelQuality:
            Constraints: null
            Statistics: null
      - name: ModelPackageDescription
        value: '{{ ModelPackageDescription }}'
      - name: ModelPackageGroupName
        value: '{{ ModelPackageGroupName }}'
      - name: ModelPackageName
        value: '{{ ModelPackageName }}'
      - name: SamplePayloadUrl
        value: '{{ SamplePayloadUrl }}'
      - name: SkipModelValidation
        value: '{{ SkipModelValidation }}'
      - name: SourceAlgorithmSpecification
        value:
          SourceAlgorithms:
            - AlgorithmName: '{{ AlgorithmName }}'
              ModelDataUrl: '{{ ModelDataUrl }}'
      - name: Task
        value: '{{ Task }}'
      - name: ValidationSpecification
        value:
          ValidationProfiles:
            - TransformJobDefinition:
                Environment: null
                BatchStrategy: '{{ BatchStrategy }}'
                MaxConcurrentTransforms: '{{ MaxConcurrentTransforms }}'
                MaxPayloadInMB: '{{ MaxPayloadInMB }}'
                TransformInput:
                  CompressionType: '{{ CompressionType }}'
                  ContentType: '{{ ContentType }}'
                  DataSource:
                    S3DataSource:
                      S3DataType: '{{ S3DataType }}'
                      S3Uri: '{{ S3Uri }}'
                  SplitType: '{{ SplitType }}'
                TransformOutput:
                  Accept: '{{ Accept }}'
                  KmsKeyId: '{{ KmsKeyId }}'
                  S3OutputPath: '{{ S3OutputPath }}'
                  AssembleWith: '{{ AssembleWith }}'
                TransformResources:
                  InstanceCount: '{{ InstanceCount }}'
                  InstanceType: '{{ InstanceType }}'
                  VolumeKmsKeyId: '{{ VolumeKmsKeyId }}'
              ProfileName: '{{ ProfileName }}'
          ValidationRole: '{{ ValidationRole }}'
      - name: ApprovalDescription
        value: '{{ ApprovalDescription }}'
      - name: LastModifiedTime
        value: '{{ LastModifiedTime }}'
      - name: ModelPackageVersion
        value: '{{ ModelPackageVersion }}'
      - name: AdditionalInferenceSpecificationsToAdd
        value: null
      - name: ModelPackageStatusDetails
        value:
          ValidationStatuses:
            - FailureReason: '{{ FailureReason }}'
              Name: '{{ Name }}'
              Status: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.model_packages
WHERE data__Identifier = '<ModelPackageArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_packages</code> resource, the following permissions are required:

### Create
```json
ecr:BatchGetImage,
ecr:DescribeImages,
ecr:StartImageScan,
ecr:DescribeImageScanFindings,
sagemaker:AddTags,
sagemaker:CreateModel,
sagemaker:CreateModelPackage,
sagemaker:CreateTrainingJob,
sagemaker:CreateTransformJob,
sagemaker:DescribeTransformJob,
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
iam:PassRole,
s3:GetObject
```

### Delete
```json
sagemaker:DeleteModelPackage,
sagemaker:DescribeModelPackage
```

### List
```json
sagemaker:ListModelPackages
```

