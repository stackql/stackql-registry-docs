---
title: model_package_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - model_package_groups
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
Retrieves a list of <code>model_package_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_package_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>ModelPackageGroupArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelPackageGroupName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelPackageGroupDescription</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelPackageGroupPolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The time at which the model package group was created.</td></tr><tr><td><code>ModelPackageGroupStatus</code></td><td><code>string</code></td><td>The status of a modelpackage group job.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.model_package_groups
WHERE region = 'us-east-1'
</pre>
