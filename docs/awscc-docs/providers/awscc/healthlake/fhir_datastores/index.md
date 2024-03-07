---
title: fhir_datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_datastores
  - healthlake
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>fhir_datastores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fhir_datastores</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.healthlake.fhir_datastores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>datastore_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>fhir_datastores</code> resource, the following permissions are required:

### Create
<pre>
healthlake:CreateFHIRDatastore,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt,
iam:GetRole,
iam:CreateServiceLinkedRole,
ram:GetResourceShareInvitations,
ram:AcceptResourceShareInvitation,
glue:CreateDatabase,
glue:DeleteDatabase,
lambda:InvokeFunction,
healthlake:TagResource,
healthlake:UntagResource,
healthlake:ListTagsForResource</pre>

### List
<pre>
healthlake:ListFHIRDatastores</pre>


## Example
```sql
SELECT
region,
datastore_id
FROM awscc.healthlake.fhir_datastores
WHERE region = 'us-east-1'
```
