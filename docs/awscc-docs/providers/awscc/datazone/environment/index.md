---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
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
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td>The AWS account in which the Amazon DataZone environment is created.</td></tr>
<tr><td><code>aws_account_region</code></td><td><code>string</code></td><td>The AWS region in which the Amazon DataZone environment is created.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the environment was created.</td></tr>
<tr><td><code>created_by</code></td><td><code>string</code></td><td>The Amazon DataZone user who created the environment.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the Amazon DataZone environment.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment is created.</td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment would be created.</td></tr>
<tr><td><code>environment_blueprint_id</code></td><td><code>string</code></td><td>The ID of the blueprint with which the Amazon DataZone environment was created.</td></tr>
<tr><td><code>environment_profile_id</code></td><td><code>string</code></td><td>The ID of the environment profile with which the Amazon DataZone environment was created.</td></tr>
<tr><td><code>environment_profile_identifier</code></td><td><code>string</code></td><td>The ID of the environment profile with which the Amazon DataZone environment would be created.</td></tr>
<tr><td><code>glossary_terms</code></td><td><code>array</code></td><td>The glossary terms that can be used in the Amazon DataZone environment.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone environment.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone project in which the environment is created.</td></tr>
<tr><td><code>project_identifier</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone project in which the environment would be created.</td></tr>
<tr><td><code>provider</code></td><td><code>string</code></td><td>The provider of the Amazon DataZone environment.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the Amazon DataZone environment.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The timestamp of when the environment was updated.</td></tr>
<tr><td><code>user_parameters</code></td><td><code>array</code></td><td>The user parameters of the Amazon DataZone environment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironment
```

### Update
```json
datazone:UpdateEnvironment,
datazone:GetEnvironment,
datazone:DeleteEnvironment
```

### Delete
```json
datazone:DeleteEnvironment,
datazone:GetEnvironment
```


## Example
```sql
SELECT
region,
aws_account_id,
aws_account_region,
created_at,
created_by,
description,
domain_id,
domain_identifier,
environment_blueprint_id,
environment_profile_id,
environment_profile_identifier,
glossary_terms,
id,
name,
project_id,
project_identifier,
provider,
status,
updated_at,
user_parameters
FROM awscc.datazone.environment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainId&gt;'
AND data__Identifier = '&lt;Id&gt;'
```
