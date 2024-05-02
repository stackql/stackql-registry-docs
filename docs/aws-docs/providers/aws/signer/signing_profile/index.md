---
title: signing_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - signing_profile
  - signer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>signing_profile</code> resource, use <code>signing_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signing_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A signing profile is a signing template that can be used to carry out a pre-defined signing job.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.signer.signing_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>profile_name</code></td><td><code>string</code></td><td>A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name. </td></tr>
<tr><td><code>profile_version</code></td><td><code>string</code></td><td>A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile.</td></tr>
<tr><td><code>profile_version_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile version.</td></tr>
<tr><td><code>signature_validity_period</code></td><td><code>object</code></td><td>Signature validity period of the profile.</td></tr>
<tr><td><code>platform_id</code></td><td><code>string</code></td><td>The ID of the target signing platform.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags associated with the signing profile.</td></tr>
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
profile_name,
profile_version,
arn,
profile_version_arn,
signature_validity_period,
platform_id,
tags
FROM aws.signer.signing_profile
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>signing_profile</code> resource, the following permissions are required:

### Read
```json
signer:GetSigningProfile
```

### Delete
```json
signer:CancelSigningProfile,
signer:GetSigningProfile
```

### Update
```json
signer:TagResource,
signer:UntagResource,
signer:GetSigningProfile
```

