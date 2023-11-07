---
title: studio_component
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_component
  - nimblestudio
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>studio_component</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.studio_component</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Configuration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>&lt;p&gt;The description.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Ec2SecurityGroupIds</code></td><td><code>array</code></td><td>&lt;p&gt;The EC2 security groups that control access to the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>InitializationScripts</code></td><td><code>array</code></td><td>&lt;p&gt;Initialization scripts for studio components.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>&lt;p&gt;The name for the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>RuntimeRoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ScriptParameters</code></td><td><code>array</code></td><td>&lt;p&gt;Parameters for the studio component scripts.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>SecureInitializationRoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StudioComponentId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StudioId</code></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Subtype</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.nimblestudio.studio_component
WHERE region = 'us-east-1' AND data__Identifier = '&lt;StudioComponentId&gt;' AND data__Identifier = '&lt;StudioId&gt;'
</pre>
