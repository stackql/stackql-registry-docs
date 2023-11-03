---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.organizations.accounts</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccountName</code></td><td><code>string</code></td><td>The friendly name of the member account.</td></tr><tr><td><code>Email</code></td><td><code>string</code></td><td>The email address of the owner to assign to the new member account.</td></tr><tr><td><code>RoleName</code></td><td><code>string</code></td><td>The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.</td></tr><tr><td><code>ParentIds</code></td><td><code>array</code></td><td>List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.</td></tr><tr><td><code>AccountId</code></td><td><code>string</code></td><td>If the account was created successfully, the unique identifier (ID) of the new account.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account.</td></tr><tr><td><code>JoinedMethod</code></td><td><code>string</code></td><td>The method by which the account joined the organization.</td></tr><tr><td><code>JoinedTimestamp</code></td><td><code>string</code></td><td>The date the account became a part of the organization.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the account in the organization.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.organizations.accounts
WHERE region = 'us-east-1'
</pre>
