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

Creates, updates, deletes or gets a <code>model_package</code> resource or lists <code>model_packages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackage</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_packages" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="additional_inference_specifications" /></td><td><code>array</code></td><td>An array of additional Inference Specification objects.</td></tr>
<tr><td><CopyableCode code="certify_for_marketplace" /></td><td><code>boolean</code></td><td>Whether to certify the model package for listing on AWS Marketplace.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>A unique token that guarantees that the call to this API is idempotent.</td></tr>
<tr><td><CopyableCode code="customer_metadata_properties" /></td><td><code>object</code></td><td>The metadata properties associated with the model package versions.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The machine learning domain of the model package you specified.</td></tr>
<tr><td><CopyableCode code="drift_check_baselines" /></td><td><code>object</code></td><td>Represents the drift check baselines that can be used when the model monitor is set using the model package.</td></tr>
<tr><td><CopyableCode code="inference_specification" /></td><td><code>object</code></td><td>Details about inference jobs that can be run with models based on this model package.</td></tr>
<tr><td><CopyableCode code="metadata_properties" /></td><td><code>object</code></td><td>Metadata properties of the tracking entity, trial, or trial component.</td></tr>
<tr><td><CopyableCode code="model_approval_status" /></td><td><code>string</code></td><td>The approval status of the model package.</td></tr>
<tr><td><CopyableCode code="model_metrics" /></td><td><code>object</code></td><td>A structure that contains model metrics reports.</td></tr>
<tr><td><CopyableCode code="model_package_description" /></td><td><code>string</code></td><td>The description of the model package.</td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td>The name of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_name" /></td><td><code>string</code></td><td>The name or arn of the model package.</td></tr>
<tr><td><CopyableCode code="sample_payload_url" /></td><td><code>string</code></td><td>The Amazon Simple Storage Service (Amazon S3) path where the sample payload are stored pointing to single gzip compressed tar archive.</td></tr>
<tr><td><CopyableCode code="skip_model_validation" /></td><td><code>string</code></td><td>Indicates if you want to skip model validation.</td></tr>
<tr><td><CopyableCode code="source_algorithm_specification" /></td><td><code>object</code></td><td>Details about the algorithm that was used to create the model package.</td></tr>
<tr><td><CopyableCode code="task" /></td><td><code>string</code></td><td>The machine learning task your model package accomplishes.</td></tr>
<tr><td><CopyableCode code="validation_specification" /></td><td><code>object</code></td><td>Specifies configurations for one or more transform jobs that Amazon SageMaker runs to test the model package.</td></tr>
<tr><td><CopyableCode code="model_package_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the model package group.</td></tr>
<tr><td><CopyableCode code="approval_description" /></td><td><code>string</code></td><td>A description provided for the model approval.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the model package was created.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>The time at which the model package was last modified.</td></tr>
<tr><td><CopyableCode code="model_package_status" /></td><td><code>string</code></td><td>The current status of the model package.</td></tr>
<tr><td><CopyableCode code="model_package_version" /></td><td><code>integer</code></td><td>The version of the model package.</td></tr>
<tr><td><CopyableCode code="additional_inference_specifications_to_add" /></td><td><code>array</code></td><td>An array of additional Inference Specification objects.</td></tr>
<tr><td><CopyableCode code="model_package_status_details" /></td><td><code>object</code></td><td>Details about the current status of the model package.</td></tr>
<tr><td><CopyableCode code="source_uri" /></td><td><code>string</code></td><td>The URI of the source for the model package.</td></tr>
<tr><td><CopyableCode code="model_card" /></td><td><code>object</code></td><td>The model card associated with the model package.</td></tr>
<tr><td><CopyableCode code="security_config" /></td><td><code>object</code></td><td>An optional AWS Key Management Service key to encrypt, decrypt, and re-encrypt model package information for regulated workloads with highly sensitive data.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html"><code>AWS::SageMaker::ModelPackage</code></a>.

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
Gets all <code>model_packages</code> in a region.
```sql
SELECT
region,
tags,
additional_inference_specifications,
certify_for_marketplace,
client_token,
customer_metadata_properties,
domain,
drift_check_baselines,
inference_specification,
metadata_properties,
model_approval_status,
model_metrics,
model_package_description,
model_package_group_name,
model_package_name,
sample_payload_url,
skip_model_validation,
source_algorithm_specification,
task,
validation_specification,
model_package_arn,
approval_description,
creation_time,
last_modified_time,
model_package_status,
model_package_version,
additional_inference_specifications_to_add,
model_package_status_details,
source_uri,
model_card,
security_config
FROM aws.sagemaker.model_packages
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>model_package</code>.
```sql
SELECT
region,
tags,
additional_inference_specifications,
certify_for_marketplace,
client_token,
customer_metadata_properties,
domain,
drift_check_baselines,
inference_specification,
metadata_properties,
model_approval_status,
model_metrics,
model_package_description,
model_package_group_name,
model_package_name,
sample_payload_url,
skip_model_validation,
source_algorithm_specification,
task,
validation_specification,
model_package_arn,
approval_description,
creation_time,
last_modified_time,
model_package_status,
model_package_version,
additional_inference_specifications_to_add,
model_package_status_details,
source_uri,
model_card,
security_config
FROM aws.sagemaker.model_packages
WHERE region = 'us-east-1' AND data__Identifier = '<ModelPackageArn>';
```

## `INSERT` example

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
 SourceUri,
 ModelCard,
 SecurityConfig,
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
 '{{ SourceUri }}',
 '{{ ModelCard }}',
 '{{ SecurityConfig }}',
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
 SourceUri,
 ModelCard,
 SecurityConfig,
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
 '{{ SourceUri }}',
 '{{ ModelCard }}',
 '{{ SecurityConfig }}',
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
                ModelDataSource:
                  S3DataSource:
                    S3DataType: '{{ S3DataType }}'
                    S3Uri: '{{ S3Uri }}'
                    CompressionType: '{{ CompressionType }}'
                    ModelAccessConfig:
                      AcceptEula: '{{ AcceptEula }}'
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
      - name: SourceUri
        value: '{{ SourceUri }}'
      - name: ModelCard
        value:
          ModelCardContent: '{{ ModelCardContent }}'
          ModelCardStatus: '{{ ModelCardStatus }}'
      - name: SecurityConfig
        value:
          KmsKeyId: '{{ KmsKeyId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

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
sagemaker:UpdateModelPackage,
iam:PassRole,
s3:GetObject,
s3:ListBucket,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
kms:DescribeKey,
kms:Decrypt
```

### Update
```json
ecr:BatchGetImage,
sagemaker:UpdateModelPackage,
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags,
s3:GetObject,
s3:ListBucket,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
sagemaker:DeleteModelPackage,
sagemaker:DescribeModelPackage,
kms:DescribeKey,
kms:Decrypt
```

### List
```json
sagemaker:ListModelPackages
```
