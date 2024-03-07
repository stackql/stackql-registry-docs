---
title: environment_blueprint_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_blueprint_configurations
  - datazone
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>environment_blueprint_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment_blueprint_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.environment_blueprint_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_blueprint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environment_blueprint_configurations</code> resource, the following permissions are required:

### Create
<pre>
datazone:ListEnvironmentBlueprints,
iam:PassRole,
datazone:GetEnvironmentBlueprintConfiguration,
datazone:PutEnvironmentBlueprintConfiguration</pre>

### List
<pre>
datazone:ListEnvironmentBlueprintConfigurations</pre>


## Example
```sql
SELECT
region,
domain_id,
environment_blueprint_id
FROM awscc.datazone.environment_blueprint_configurations
WHERE region = 'us-east-1'
```
