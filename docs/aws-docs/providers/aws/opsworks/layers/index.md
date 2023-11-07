---
title: layers
hide_title: false
hide_table_of_contents: false
keywords:
  - layers
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>layers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opsworks.layers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>AutoAssignElasticIps</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>AutoAssignPublicIps</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>CustomInstanceProfileArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomJson</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>CustomRecipes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomSecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EnableAutoHealing</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>InstallUpdatesOnBoot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>LifecycleEventConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LoadBasedAutoScaling</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Packages</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Shortname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StackId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UseEbsOptimizedInstances</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>VolumeConfigurations</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opsworks.layers
WHERE region = 'us-east-1'
</pre>
