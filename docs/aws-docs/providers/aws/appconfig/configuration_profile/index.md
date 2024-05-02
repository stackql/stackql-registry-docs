---
title: configuration_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>configuration_profile</code> resource, use <code>configuration_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.configuration_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>configuration_profile_id</code></td><td><code>string</code></td><td>The configuration profile ID</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>A URI to locate the configuration. You can specify the AWS AppConfig hosted configuration store, Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of configurations contained in the profile. When calling this API, enter one of the following values for Type: AWS.AppConfig.FeatureFlags, AWS.Freeform</td></tr>
<tr><td><code>kms_key_identifier</code></td><td><code>string</code></td><td>The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the configuration profile.</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for hosted configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.</td></tr>
<tr><td><code>validators</code></td><td><code>array</code></td><td>A list of methods for validating the configuration.</td></tr>
<tr><td><code>retrieval_role_arn</code></td><td><code>string</code></td><td>The ARN of an IAM role with permission to access the configuration at the specified LocationUri.</td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the configuration profile.</td></tr>
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
configuration_profile_id,
location_uri,
type,
kms_key_identifier,
description,
kms_key_arn,
validators,
retrieval_role_arn,
application_id,
tags,
name
FROM aws.appconfig.configuration_profile
WHERE data__Identifier = '<ApplicationId>|<ConfigurationProfileId>';
```

## Permissions

To operate on the <code>configuration_profile</code> resource, the following permissions are required:

### Read
```json
appconfig:GetConfigurationProfile,
appconfig:ListTagsForResource
```

### Update
```json
appconfig:UpdateConfigurationProfile,
appconfig:TagResource,
appconfig:UntagResource,
iam:PassRole
```

### Delete
```json
appconfig:DeleteConfigurationProfile
```

