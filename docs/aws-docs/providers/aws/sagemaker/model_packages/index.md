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
Retrieves a list of <code>model_packages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_packages</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_packages</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>AdditionalInferenceSpecifications</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AdditionalInferenceSpecificationDefinition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CertifyForMarketplace</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ClientToken</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomerMetadataProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Domain</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DriftCheckBaselines</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>InferenceSpecification</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MetadataProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelApprovalStatus</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelMetrics</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageDescription</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageGroupName</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageName</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SamplePayloadUrl</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SourceAlgorithmSpecification</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Task</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ValidationSpecification</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ApprovalDescription</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastModifiedBy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageStatus</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageVersion</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AdditionalInferenceSpecificationsToAdd</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageStatusDetails</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelPackageStatusItem</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CreatedBy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Environment</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.model_packages
WHERE region = 'us-east-1'
</pre>
