---
title: custom_action_type
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_action_type
  - codepipeline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>custom_action_type</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.codepipeline.custom_action_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Category</code></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr><tr><td><code>ConfigurationProperties</code></td><td><code>array</code></td><td>The configuration properties for the custom action.</td></tr><tr><td><code>InputArtifactDetails</code></td><td><code>undefined</code></td><td>The details of the input artifact for the action, such as its commit ID.</td></tr><tr><td><code>OutputArtifactDetails</code></td><td><code>undefined</code></td><td>The details of the output artifact of the action, such as its commit ID.</td></tr><tr><td><code>Provider</code></td><td><code>string</code></td><td>The provider of the service used in the custom action, such as AWS CodeDeploy.</td></tr><tr><td><code>Settings</code></td><td><code>undefined</code></td><td>URLs that provide users information about this custom action.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Any tags assigned to the custom action.</td></tr><tr><td><code>Version</code></td><td><code>string</code></td><td>The version identifier of the custom action.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codepipeline.custom_action_type
WHERE region = 'us-east-1' AND data__Identifier = '{Category}' AND data__Identifier = '{Provider}' AND data__Identifier = '{Version}'
</pre>
