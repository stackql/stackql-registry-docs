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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.logs_data_forwarding.destinations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the data forwarding destination. |
| <CopyableCode code="description" /> | `string` | Description of the S3 data forwarding destination. |
| <CopyableCode code="accessKeyId" /> | `string` | The AWS Access ID to access the S3 bucket. |
| <CopyableCode code="authenticationMode" /> | `string` | AWS IAM authentication method used for access. Possible values are: 1. `AccessKey` 2. `RoleBased` |
| <CopyableCode code="bucketName" /> | `string` | The name of the Amazon S3 bucket. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="destinationName" /> | `string` | Name of the S3 data forwarding destination. |
| <CopyableCode code="enabled" /> | `boolean` | True if the destination is Active. |
| <CopyableCode code="encrypted" /> | `boolean` | Enable S3 server-side encryption. |
| <CopyableCode code="invalidatedBySystem" /> | `boolean` | True if invalidated by the system. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="region" /> | `string` | The region where the S3 bucket is located. |
| <CopyableCode code="roleArn" /> | `string` | The AWS Role ARN to access the S3 bucket. |
| <CopyableCode code="secretAccessKey" /> | `string` | The AWS Secret Key to access the S3 bucket. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDataForwardingBuckets" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all Amazon S3 data forwarding destinations. |
| <CopyableCode code="getDataForwardingDestination" /> | `SELECT` | <CopyableCode code="id, region" /> | Get an S3 data forwarding destination by the given identifier. |
| <CopyableCode code="createDataForwardingBucket" /> | `INSERT` | <CopyableCode code="region" /> | Create a new Amazon S3 data forwarding destination. |
| <CopyableCode code="deleteDataForwardingBucket" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete an existing Amazon S3 data forwarding destination with the given identifier. |
| <CopyableCode code="UpdateDataForwardingBucket" /> | `EXEC` | <CopyableCode code="id, data__authenticationMode, region" /> | Update an S3 data forwarding destination by the given identifier. |
