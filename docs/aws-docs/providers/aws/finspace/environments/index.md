---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - finspace
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.finspace.environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EnvironmentId</code></td><td><code>string</code></td><td>Unique identifier for representing FinSpace Environment</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the Environment</td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td>AWS account ID associated with the Environment</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Description of the Environment</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>State of the Environment</td></tr>
<tr><td><code>EnvironmentUrl</code></td><td><code>string</code></td><td>URL used to login to the Environment</td></tr>
<tr><td><code>EnvironmentArn</code></td><td><code>string</code></td><td>ARN of the Environment</td></tr>
<tr><td><code>SageMakerStudioDomainUrl</code></td><td><code>string</code></td><td>SageMaker Studio Domain URL associated with the Environment</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>KMS key used to encrypt customer data within FinSpace Environment infrastructure</td></tr>
<tr><td><code>DedicatedServiceAccountId</code></td><td><code>string</code></td><td>ID for FinSpace created account used to store Environment artifacts</td></tr>
<tr><td><code>FederationMode</code></td><td><code>string</code></td><td>Federation mode used with the Environment</td></tr>
<tr><td><code>FederationParameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SuperuserParameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataBundles</code></td><td><code>array</code></td><td>ARNs of FinSpace Data Bundles to install</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.finspace.environments
WHERE region = 'us-east-1'
</pre>
