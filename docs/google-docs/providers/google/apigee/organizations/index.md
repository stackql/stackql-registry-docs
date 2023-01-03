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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.organizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the Apigee organization. |
| `description` | `string` | Description of the Apigee organization. |
| `lastModifiedAt` | `string` | Output only. Time that the Apigee organization was last modified in milliseconds since epoch. |
| `type` | `string` | Not used by Apigee. |
| `expiresAt` | `string` | Output only. Time that the Apigee organization is scheduled for deletion. |
| `portalDisabled` | `boolean` | Configuration for the Portals settings. |
| `runtimeType` | `string` | Required. Runtime type of the Apigee organization based on the Apigee subscription purchased. |
| `analyticsRegion` | `string` | Required. DEPRECATED: This field will be deprecated once Apigee supports DRZ. Primary GCP region for analytics data storage. For valid values, see [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| `properties` | `object` | Message for compatibility with legacy Edge specification for Java Properties object in JSON. |
| `attributes` | `array` | Not used by Apigee. |
| `customerName` | `string` | Not used by Apigee. |
| `environments` | `array` | Output only. List of environments in the Apigee organization. |
| `state` | `string` | Output only. State of the organization. Values other than ACTIVE means the resource is not ready to use. |
| `caCertificate` | `string` | Output only. Base64-encoded public certificate for the root CA of the Apigee organization. Valid only when [RuntimeType](#RuntimeType) is `CLOUD`. |
| `billingType` | `string` | Billing type of the Apigee organization. See [Apigee pricing](https://cloud.google.com/apigee/pricing). |
| `subscriptionType` | `string` | Output only. DEPRECATED: This will eventually be replaced by BillingType. Subscription type of the Apigee organization. Valid values include trial (free, limited, and for evaluation purposes only) or paid (full subscription has been purchased). See [Apigee pricing](https://cloud.google.com/apigee/pricing/). |
| `displayName` | `string` | Display name for the Apigee organization. Unused, but reserved for future use. |
| `projectId` | `string` | Output only. Project ID associated with the Apigee organization. |
| `addonsConfig` | `object` | Add-on configurations for the Apigee organization. |
| `createdAt` | `string` | Output only. Time that the Apigee organization was created in milliseconds since epoch. |
| `apigeeProjectId` | `string` | Output only. Apigee Project ID associated with the organization. Use this project to allowlist Apigee in the Service Attachment when using private service connect with Apigee. |
| `runtimeDatabaseEncryptionKeyName` | `string` | Cloud KMS key name used for encrypting the data that is stored and replicated across runtime instances. Update is not allowed after the organization is created. Required when [RuntimeType](#RuntimeType) is `CLOUD`. If not specified when [RuntimeType](#RuntimeType) is `TRIAL`, a Google-Managed encryption key will be used. For example: "projects/foo/locations/us/keyRings/bar/cryptoKeys/baz". **Note:** Not supported for Apigee hybrid. |
| `authorizedNetwork` | `string` | Compute Engine network used for Service Networking to be peered with Apigee runtime instances. See [Getting started with the Service Networking API](https://cloud.google.com/service-infrastructure/docs/service-networking/getting-started). Valid only when [RuntimeType](#RuntimeType) is set to `CLOUD`. The value must be set before the creation of a runtime instance and can be updated only when there are no runtime instances. For example: `default`. Apigee also supports shared VPC (that is, the host network project is not the same as the one that is peering with Apigee). See [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc). To use a shared VPC network, use the following format: `projects/{host-project-id}/{region}/networks/{network-name}`. For example: `projects/my-sharedvpc-host/global/networks/mynetwork` **Note:** Not supported for Apigee hybrid. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `organizationsId` | Gets the profile for an Apigee organization. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| `list` | `SELECT` |  | Lists the Apigee organizations and associated GCP projects that you have permission to access. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| `create` | `INSERT` |  | Creates an Apigee organization. See [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| `delete` | `DELETE` | `organizationsId` | Delete an Apigee organization. For organizations with BillingType EVALUATION, an immediate deletion is performed. For paid organizations, a soft-deletion is performed. The organization can be restored within the soft-deletion period - which can be controlled using the retention field in the request. |
| `setAddons` | `EXEC` | `organizationsId` | Configures the add-ons for the Apigee organization. The existing add-on configuration will be fully replaced. |
| `setSyncAuthorization` | `EXEC` | `organizationsId` | Sets the permissions required to allow the Synchronizer to download environment data from the control plane. You must call this API to enable proper functioning of hybrid. Pass the ETag when calling `setSyncAuthorization` to ensure that you are updating the correct version. To get an ETag, call [getSyncAuthorization](getSyncAuthorization). If you don't pass the ETag in the call to `setSyncAuthorization`, then the existing authorization is overwritten indiscriminately. For more information, see [Configure the Synchronizer](https://cloud.google.com/apigee/docs/hybrid/latest/synchronizer-access). **Note**: Available to Apigee hybrid only. |
| `update` | `EXEC` | `organizationsId` | Updates the properties for an Apigee organization. No other fields in the organization profile will be updated. |
