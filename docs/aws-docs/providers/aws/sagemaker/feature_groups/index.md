---
title: feature_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups
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
Retrieves a list of <code>feature_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>feature_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.feature_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FeatureGroupName</code></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
<tr><td><code>RecordIdentifierFeatureName</code></td><td><code>string</code></td><td>The Record Identifier Feature Name.</td></tr>
<tr><td><code>EventTimeFeatureName</code></td><td><code>string</code></td><td>The Event Time Feature Name.</td></tr>
<tr><td><code>FeatureDefinitions</code></td><td><code>array</code></td><td>An Array of Feature Definition</td></tr>
<tr><td><code>OnlineStoreConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>OfflineStoreConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Description about the FeatureGroup.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pair to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.feature_groups<br/>WHERE region = 'us-east-1'
</pre>
