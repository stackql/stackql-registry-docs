---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - logs_data_forwarding
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.logs_data_forwarding.destinations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the data forwarding destination. |
| `description` | `string` | Description of the S3 data forwarding destination. |
| `authenticationMode` | `string` | AWS IAM authentication method used for access. Possible values are: 1. `AccessKey` 2. `RoleBased` |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `bucketName` | `string` | The name of the Amazon S3 bucket. |
| `secretAccessKey` | `string` | The AWS Secret Key to access the S3 bucket. |
| `region` | `string` | The region where the S3 bucket is located. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `encrypted` | `boolean` | Enable S3 server-side encryption. |
| `accessKeyId` | `string` | The AWS Access ID to access the S3 bucket. |
| `enabled` | `boolean` | True if the destination is Active. |
| `roleArn` | `string` | The AWS Role ARN to access the S3 bucket. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `invalidatedBySystem` | `boolean` | True if invalidated by the system. |
| `destinationName` | `string` | Name of the S3 data forwarding destination. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDataForwardingBuckets` | `SELECT` | `region` | Get a list of all Amazon S3 data forwarding destinations. |
| `getDataForwardingDestination` | `SELECT` | `id, region` | Get an S3 data forwarding destination by the given identifier. |
| `createDataForwardingBucket` | `INSERT` | `region` | Create a new Amazon S3 data forwarding destination. |
| `deleteDataForwardingBucket` | `DELETE` | `id, region` | Delete an existing Amazon S3 data forwarding destination with the given identifier. |
| `UpdateDataForwardingBucket` | `EXEC` | `id, data__authenticationMode, region` | Update an S3 data forwarding destination by the given identifier. |
