---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>studios</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.studios</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the EMR Studio.</td></tr><tr><td><code>AuthMode</code></td><td><code>string</code></td><td>Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.</td></tr><tr><td><code>DefaultS3Location</code></td><td><code>string</code></td><td>The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A detailed description of the Studio.</td></tr><tr><td><code>EngineSecurityGroupId</code></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>A descriptive name for the Amazon EMR Studio.</td></tr><tr><td><code>ServiceRole</code></td><td><code>undefined</code></td><td>The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.</td></tr><tr><td><code>StudioId</code></td><td><code>string</code></td><td>The ID of the EMR Studio.</td></tr><tr><td><code>SubnetIds</code></td><td><code>array</code></td><td>A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.</td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td>A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td>The unique Studio access URL.</td></tr><tr><td><code>UserRole</code></td><td><code>undefined</code></td><td>The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.</td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td>The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.</td></tr><tr><td><code>WorkspaceSecurityGroupId</code></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.</td></tr><tr><td><code>IdpAuthUrl</code></td><td><code>string</code></td><td>Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.</td></tr><tr><td><code>IdpRelayStateParameterName</code></td><td><code>string</code></td><td>The name of relay state parameter for external Identity Provider.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.emr.studios
WHERE region = 'us-east-1'
```
