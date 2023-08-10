---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.organizations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_get` | `SELECT` | `organizationsId` | Gets the profile for an Apigee organization. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| `organizations_list` | `SELECT` |  | Lists the Apigee organizations and associated Google Cloud projects that you have permission to access. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| `organizations_create` | `INSERT` |  | Creates an Apigee organization. See [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| `organizations_delete` | `DELETE` | `organizationsId` | Delete an Apigee organization. For organizations with BillingType EVALUATION, an immediate deletion is performed. For paid organizations, a soft-deletion is performed. The organization can be restored within the soft-deletion period which can be controlled using the retention field in the request. |
| `organizations_set_addons` | `EXEC` | `organizationsId` | Configures the add-ons for the Apigee organization. The existing add-on configuration will be fully replaced. |
| `organizations_set_sync_authorization` | `EXEC` | `organizationsId` | Sets the permissions required to allow the Synchronizer to download environment data from the control plane. You must call this API to enable proper functioning of hybrid. Pass the ETag when calling `setSyncAuthorization` to ensure that you are updating the correct version. To get an ETag, call [getSyncAuthorization](getSyncAuthorization). If you don't pass the ETag in the call to `setSyncAuthorization`, then the existing authorization is overwritten indiscriminately. For more information, see [Configure the Synchronizer](https://cloud.google.com/apigee/docs/hybrid/latest/synchronizer-access). **Note**: Available to Apigee hybrid only. |
| `organizations_update` | `EXEC` | `organizationsId` | Updates the properties for an Apigee organization. No other fields in the organization profile will be updated. |
