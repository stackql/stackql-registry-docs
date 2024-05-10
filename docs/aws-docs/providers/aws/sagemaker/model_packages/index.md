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
model_package_arn
FROM aws.sagemaker.model_packages
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
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "AdditionalInferenceSpecifications": [
  {
   "Containers": [
    {
     "ContainerHostname": "{{ ContainerHostname }}",
     "Environment": {},
     "ModelInput": {
      "DataInputConfig": "{{ DataInputConfig }}"
     },
     "Image": "{{ Image }}",
     "ImageDigest": "{{ ImageDigest }}",
     "ModelDataUrl": "{{ ModelDataUrl }}",
     "Framework": "{{ Framework }}",
     "FrameworkVersion": "{{ FrameworkVersion }}",
     "NearestModelName": "{{ NearestModelName }}"
    }
   ],
   "Description": "{{ Description }}",
   "Name": "{{ Name }}",
   "SupportedContentTypes": [
    "{{ SupportedContentTypes[0] }}"
   ],
   "SupportedRealtimeInferenceInstanceTypes": [
    "{{ SupportedRealtimeInferenceInstanceTypes[0] }}"
   ],
   "SupportedResponseMIMETypes": [
    "{{ SupportedResponseMIMETypes[0] }}"
   ],
   "SupportedTransformInstanceTypes": [
    "{{ SupportedTransformInstanceTypes[0] }}"
   ]
  }
 ],
 "CertifyForMarketplace": "{{ CertifyForMarketplace }}",
 "ClientToken": "{{ ClientToken }}",
 "CustomerMetadataProperties": {},
 "Domain": "{{ Domain }}",
 "DriftCheckBaselines": {
  "Bias": {
   "PostTrainingConstraints": {
    "ContentDigest": "{{ ContentDigest }}",
    "ContentType": "{{ ContentType }}",
    "S3Uri": "{{ S3Uri }}"
   },
   "PreTrainingConstraints": null,
   "ConfigFile": {
    "ContentDigest": "{{ ContentDigest }}",
    "ContentType": "{{ ContentType }}",
    "S3Uri": "{{ S3Uri }}"
   }
  },
  "Explainability": {
   "Constraints": null,
   "ConfigFile": null
  },
  "ModelDataQuality": {
   "Constraints": null,
   "Statistics": null
  },
  "ModelQuality": {
   "Constraints": null,
   "Statistics": null
  }
 },
 "InferenceSpecification": {
  "Containers": [
   null
  ],
  "SupportedContentTypes": [
   null
  ],
  "SupportedRealtimeInferenceInstanceTypes": [
   null
  ],
  "SupportedResponseMIMETypes": [
   null
  ],
  "SupportedTransformInstanceTypes": [
   null
  ]
 },
 "MetadataProperties": {
  "CommitId": "{{ CommitId }}",
  "GeneratedBy": "{{ GeneratedBy }}",
  "ProjectId": "{{ ProjectId }}",
  "Repository": "{{ Repository }}"
 },
 "ModelApprovalStatus": "{{ ModelApprovalStatus }}",
 "ModelMetrics": {
  "Bias": {
   "Report": null,
   "PreTrainingReport": null,
   "PostTrainingReport": null
  },
  "Explainability": {
   "Report": null
  },
  "ModelDataQuality": {
   "Constraints": null,
   "Statistics": null
  },
  "ModelQuality": {
   "Constraints": null,
   "Statistics": null
  }
 },
 "ModelPackageDescription": "{{ ModelPackageDescription }}",
 "ModelPackageGroupName": "{{ ModelPackageGroupName }}",
 "ModelPackageName": "{{ ModelPackageName }}",
 "SamplePayloadUrl": "{{ SamplePayloadUrl }}",
 "SkipModelValidation": "{{ SkipModelValidation }}",
 "SourceAlgorithmSpecification": {
  "SourceAlgorithms": [
   {
    "AlgorithmName": "{{ AlgorithmName }}",
    "ModelDataUrl": "{{ ModelDataUrl }}"
   }
  ]
 },
 "Task": "{{ Task }}",
 "ValidationSpecification": {
  "ValidationProfiles": [
   {
    "TransformJobDefinition": {
     "Environment": null,
     "BatchStrategy": "{{ BatchStrategy }}",
     "MaxConcurrentTransforms": "{{ MaxConcurrentTransforms }}",
     "MaxPayloadInMB": "{{ MaxPayloadInMB }}",
     "TransformInput": {
      "CompressionType": "{{ CompressionType }}",
      "ContentType": "{{ ContentType }}",
      "DataSource": {
       "S3DataSource": {
        "S3DataType": "{{ S3DataType }}",
        "S3Uri": "{{ S3Uri }}"
       }
      },
      "SplitType": "{{ SplitType }}"
     },
     "TransformOutput": {
      "Accept": "{{ Accept }}",
      "KmsKeyId": "{{ KmsKeyId }}",
      "S3OutputPath": "{{ S3OutputPath }}",
      "AssembleWith": "{{ AssembleWith }}"
     },
     "TransformResources": {
      "InstanceCount": "{{ InstanceCount }}",
      "InstanceType": "{{ InstanceType }}",
      "VolumeKmsKeyId": "{{ VolumeKmsKeyId }}"
     }
    },
    "ProfileName": "{{ ProfileName }}"
   }
  ],
  "ValidationRole": "{{ ValidationRole }}"
 },
 "ApprovalDescription": "{{ ApprovalDescription }}",
 "LastModifiedTime": "{{ LastModifiedTime }}",
 "ModelPackageVersion": "{{ ModelPackageVersion }}",
 "AdditionalInferenceSpecificationsToAdd": null,
 "ModelPackageStatusDetails": {
  "ValidationStatuses": [
   {
    "FailureReason": "{{ FailureReason }}",
    "Name": "{{ Name }}",
    "Status": "{{ Status }}"
   }
  ]
 }
}
>>>
--required properties only
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
{{ Tags }},
 {{ AdditionalInferenceSpecifications }},
 {{ CertifyForMarketplace }},
 {{ ClientToken }},
 {{ CustomerMetadataProperties }},
 {{ Domain }},
 {{ DriftCheckBaselines }},
 {{ InferenceSpecification }},
 {{ MetadataProperties }},
 {{ ModelApprovalStatus }},
 {{ ModelMetrics }},
 {{ ModelPackageDescription }},
 {{ ModelPackageGroupName }},
 {{ ModelPackageName }},
 {{ SamplePayloadUrl }},
 {{ SkipModelValidation }},
 {{ SourceAlgorithmSpecification }},
 {{ Task }},
 {{ ValidationSpecification }},
 {{ ApprovalDescription }},
 {{ LastModifiedTime }},
 {{ ModelPackageVersion }},
 {{ AdditionalInferenceSpecificationsToAdd }},
 {{ ModelPackageStatusDetails }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "AdditionalInferenceSpecifications": [
  {
   "Containers": [
    {
     "ContainerHostname": "{{ ContainerHostname }}",
     "Environment": {},
     "ModelInput": {
      "DataInputConfig": "{{ DataInputConfig }}"
     },
     "Image": "{{ Image }}",
     "ImageDigest": "{{ ImageDigest }}",
     "ModelDataUrl": "{{ ModelDataUrl }}",
     "Framework": "{{ Framework }}",
     "FrameworkVersion": "{{ FrameworkVersion }}",
     "NearestModelName": "{{ NearestModelName }}"
    }
   ],
   "Description": "{{ Description }}",
   "Name": "{{ Name }}",
   "SupportedContentTypes": [
    "{{ SupportedContentTypes[0] }}"
   ],
   "SupportedRealtimeInferenceInstanceTypes": [
    "{{ SupportedRealtimeInferenceInstanceTypes[0] }}"
   ],
   "SupportedResponseMIMETypes": [
    "{{ SupportedResponseMIMETypes[0] }}"
   ],
   "SupportedTransformInstanceTypes": [
    "{{ SupportedTransformInstanceTypes[0] }}"
   ]
  }
 ],
 "CertifyForMarketplace": "{{ CertifyForMarketplace }}",
 "ClientToken": "{{ ClientToken }}",
 "CustomerMetadataProperties": {},
 "Domain": "{{ Domain }}",
 "DriftCheckBaselines": {
  "Bias": {
   "PostTrainingConstraints": {
    "ContentDigest": "{{ ContentDigest }}",
    "ContentType": "{{ ContentType }}",
    "S3Uri": "{{ S3Uri }}"
   },
   "PreTrainingConstraints": null,
   "ConfigFile": {
    "ContentDigest": "{{ ContentDigest }}",
    "ContentType": "{{ ContentType }}",
    "S3Uri": "{{ S3Uri }}"
   }
  },
  "Explainability": {
   "Constraints": null,
   "ConfigFile": null
  },
  "ModelDataQuality": {
   "Constraints": null,
   "Statistics": null
  },
  "ModelQuality": {
   "Constraints": null,
   "Statistics": null
  }
 },
 "InferenceSpecification": {
  "Containers": [
   null
  ],
  "SupportedContentTypes": [
   null
  ],
  "SupportedRealtimeInferenceInstanceTypes": [
   null
  ],
  "SupportedResponseMIMETypes": [
   null
  ],
  "SupportedTransformInstanceTypes": [
   null
  ]
 },
 "MetadataProperties": {
  "CommitId": "{{ CommitId }}",
  "GeneratedBy": "{{ GeneratedBy }}",
  "ProjectId": "{{ ProjectId }}",
  "Repository": "{{ Repository }}"
 },
 "ModelApprovalStatus": "{{ ModelApprovalStatus }}",
 "ModelMetrics": {
  "Bias": {
   "Report": null,
   "PreTrainingReport": null,
   "PostTrainingReport": null
  },
  "Explainability": {
   "Report": null
  },
  "ModelDataQuality": {
   "Constraints": null,
   "Statistics": null
  },
  "ModelQuality": {
   "Constraints": null,
   "Statistics": null
  }
 },
 "ModelPackageDescription": "{{ ModelPackageDescription }}",
 "ModelPackageGroupName": "{{ ModelPackageGroupName }}",
 "ModelPackageName": "{{ ModelPackageName }}",
 "SamplePayloadUrl": "{{ SamplePayloadUrl }}",
 "SkipModelValidation": "{{ SkipModelValidation }}",
 "SourceAlgorithmSpecification": {
  "SourceAlgorithms": [
   {
    "AlgorithmName": "{{ AlgorithmName }}",
    "ModelDataUrl": "{{ ModelDataUrl }}"
   }
  ]
 },
 "Task": "{{ Task }}",
 "ValidationSpecification": {
  "ValidationProfiles": [
   {
    "TransformJobDefinition": {
     "Environment": null,
     "BatchStrategy": "{{ BatchStrategy }}",
     "MaxConcurrentTransforms": "{{ MaxConcurrentTransforms }}",
     "MaxPayloadInMB": "{{ MaxPayloadInMB }}",
     "TransformInput": {
      "CompressionType": "{{ CompressionType }}",
      "ContentType": "{{ ContentType }}",
      "DataSource": {
       "S3DataSource": {
        "S3DataType": "{{ S3DataType }}",
        "S3Uri": "{{ S3Uri }}"
       }
      },
      "SplitType": "{{ SplitType }}"
     },
     "TransformOutput": {
      "Accept": "{{ Accept }}",
      "KmsKeyId": "{{ KmsKeyId }}",
      "S3OutputPath": "{{ S3OutputPath }}",
      "AssembleWith": "{{ AssembleWith }}"
     },
     "TransformResources": {
      "InstanceCount": "{{ InstanceCount }}",
      "InstanceType": "{{ InstanceType }}",
      "VolumeKmsKeyId": "{{ VolumeKmsKeyId }}"
     }
    },
    "ProfileName": "{{ ProfileName }}"
   }
  ],
  "ValidationRole": "{{ ValidationRole }}"
 },
 "ApprovalDescription": "{{ ApprovalDescription }}",
 "LastModifiedTime": "{{ LastModifiedTime }}",
 "ModelPackageVersion": "{{ ModelPackageVersion }}",
 "AdditionalInferenceSpecificationsToAdd": null,
 "ModelPackageStatusDetails": {
  "ValidationStatuses": [
   {
    "FailureReason": "{{ FailureReason }}",
    "Name": "{{ Name }}",
    "Status": "{{ Status }}"
   }
  ]
 }
}
>>>
--all properties
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
 {{ Tags }},
 {{ AdditionalInferenceSpecifications }},
 {{ CertifyForMarketplace }},
 {{ ClientToken }},
 {{ CustomerMetadataProperties }},
 {{ Domain }},
 {{ DriftCheckBaselines }},
 {{ InferenceSpecification }},
 {{ MetadataProperties }},
 {{ ModelApprovalStatus }},
 {{ ModelMetrics }},
 {{ ModelPackageDescription }},
 {{ ModelPackageGroupName }},
 {{ ModelPackageName }},
 {{ SamplePayloadUrl }},
 {{ SkipModelValidation }},
 {{ SourceAlgorithmSpecification }},
 {{ Task }},
 {{ ValidationSpecification }},
 {{ ApprovalDescription }},
 {{ LastModifiedTime }},
 {{ ModelPackageVersion }},
 {{ AdditionalInferenceSpecificationsToAdd }},
 {{ ModelPackageStatusDetails }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

