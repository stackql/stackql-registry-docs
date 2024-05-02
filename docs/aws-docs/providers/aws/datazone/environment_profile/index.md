---
title: environment_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_profile
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
Gets or operates on an individual <code>environment_profile</code> resource, use <code>environment_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datazone.environment_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td>The AWS account in which the Amazon DataZone environment is created.</td></tr>
<tr><td><code>aws_account_region</code></td><td><code>string</code></td><td>The AWS region in which this environment profile is created.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when this environment profile was created.</td></tr>
<tr><td><code>created_by</code></td><td><code>string</code></td><td>The Amazon DataZone user who created this environment profile.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of this Amazon DataZone environment profile.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><code>environment_blueprint_id</code></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><code>environment_blueprint_identifier</code></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of this Amazon DataZone environment profile.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of this Amazon DataZone environment profile.</td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><code>project_identifier</code></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The timestamp of when this environment profile was updated.</td></tr>
<tr><td><code>user_parameters</code></td><td><code>array</code></td><td>The user parameters of this Amazon DataZone environment profile.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
environment_blueprint_identifier,
id,
name,
project_id,
project_identifier,
updated_at,
user_parameters
FROM aws.datazone.environment_profile
WHERE data__Identifier = '<DomainId>|<Id>';
```

## Permissions

To operate on the <code>environment_profile</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironmentProfile
```

### Update
```json
datazone:UpdateEnvironmentProfile,
datazone:GetEnvironmentProfile
```

### Delete
```json
datazone:DeleteEnvironmentProfile,
datazone:GetEnvironmentProfile
```

