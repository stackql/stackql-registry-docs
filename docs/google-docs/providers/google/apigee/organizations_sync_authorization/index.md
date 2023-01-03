---
title: organizations_sync_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_sync_authorization
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_sync_authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.organizations_sync_authorization</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Entity tag (ETag) used for optimistic concurrency control as a way to help prevent simultaneous updates from overwriting each other. For example, when you call [getSyncAuthorization](organizations/getSyncAuthorization) an ETag is returned in the response. Pass that ETag when calling the [setSyncAuthorization](organizations/setSyncAuthorization) to ensure that you are updating the correct version. If you don't pass the ETag in the call to `setSyncAuthorization`, then the existing authorization is overwritten indiscriminately. **Note**: We strongly recommend that you use the ETag in the read-modify-write cycle to avoid race conditions. |
| `identities` | `array` | Required. Array of service accounts to grant access to control plane resources, each specified using the following format: `serviceAccount:` service-account-name. The service-account-name is formatted like an email address. For example: `my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com` You might specify multiple service accounts, for example, if you have multiple environments and wish to assign a unique service account to each one. The service accounts must have **Apigee Synchronizer Manager** role. See also [Create service accounts](https://cloud.google.com/apigee/docs/hybrid/latest/sa-about#create-the-service-accounts). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_getSyncAuthorization` | `SELECT` | `organizationsId` |
