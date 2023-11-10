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
<tr><td><b>Description</b></td><td>studio_component</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.studio_component</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>configuration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;The description.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ec2_security_group_ids</code></td><td><code>array</code></td><td>&lt;p&gt;The EC2 security groups that control access to the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>initialization_scripts</code></td><td><code>array</code></td><td>&lt;p&gt;Initialization scripts for studio components.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>&lt;p&gt;The name for the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>runtime_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>script_parameters</code></td><td><code>array</code></td><td>&lt;p&gt;Parameters for the studio component scripts.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>secure_initialization_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>studio_component_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>subtype</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
configuration,
description,
ec2_security_group_ids,
initialization_scripts,
name,
runtime_role_arn,
script_parameters,
secure_initialization_role_arn,
studio_component_id,
studio_id,
subtype,
tags,
type
FROM aws.nimblestudio.studio_component
WHERE region = 'us-east-1'
AND data__Identifier = '<StudioComponentId>'
AND data__Identifier = '<StudioId>'
```
