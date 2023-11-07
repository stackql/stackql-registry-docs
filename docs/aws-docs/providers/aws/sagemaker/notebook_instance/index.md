---
title: notebook_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_instance
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
Gets an individual <code>notebook_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notebook_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.notebook_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VolumeSizeInGB</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>AdditionalCodeRepositories</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DefaultCodeRepository</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DirectInternetAccess</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PlatformIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AcceleratorTypes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SubnetId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceMetadataServiceConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RootAccess</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NotebookInstanceName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LifecycleConfigName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.notebook_instance
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
