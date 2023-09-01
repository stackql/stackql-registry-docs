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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the Apigee organization. |
| `description` | `string` | Description of the Apigee organization. |
| `state` | `string` | Output only. State of the organization. Values other than ACTIVE means the resource is not ready to use. |
| `displayName` | `string` | Display name for the Apigee organization. Unused, but reserved for future use. |
| `runtimeDatabaseEncryptionKeyName` | `string` | Cloud KMS key name used for encrypting the data that is stored and replicated across runtime instances. Update is not allowed after the organization is created. Required when [RuntimeType](#RuntimeType) is `CLOUD`. If not specified when [RuntimeType](#RuntimeType) is `TRIAL`, a Google-Managed encryption key will be used. For example: "projects/foo/locations/us/keyRings/bar/cryptoKeys/baz". **Note:** Not supported for Apigee hybrid. |
| `subscriptionType` | `string` | Output only. DEPRECATED: This will eventually be replaced by BillingType. Subscription type of the Apigee organization. Valid values include trial (free, limited, and for evaluation purposes only) or paid (full subscription has been purchased). See [Apigee pricing](https://cloud.google.com/apigee/pricing/). |
| `analyticsRegion` | `string` | Required. DEPRECATED: This field will eventually be deprecated and replaced with a differently-named field. Primary Google Cloud region for analytics data storage. For valid values, see [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| `environments` | `array` | Output only. List of environments in the Apigee organization. |
| `controlPlaneEncryptionKeyName` | `string` | Cloud KMS key name used for encrypting control plane data that is stored in a multi region. Required when [BillingType](#BillingType) is `SUBSCRIPTION`. When [BillingType](#BillingType) is `EVALUATION`, a Google-Managed encryption key will be used. Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*` |
| `disableVpcPeering` | `boolean` | Optional. Flag that specifies whether the VPC Peering through Private Google Access should be disabled between the consumer network and Apigee. Valid only when RuntimeType is set to CLOUD. Required if an authorizedNetwork on the consumer project is not provided, in which case the flag should be set to true. The value must be set before the creation of any Apigee runtime instance and can be updated only when there are no runtime instances. **Note:** Apigee will be deprecating the vpc peering model that requires you to provide 'authorizedNetwork', by making the non-peering model as the default way of provisioning Apigee organization in future. So, this will be a temporary flag to enable the transition. Not supported for Apigee hybrid. |
| `projectId` | `string` | Output only. Project ID associated with the Apigee organization. |
| `portalDisabled` | `boolean` | Configuration for the Portals settings. |
| `authorizedNetwork` | `string` | Compute Engine network used for Service Networking to be peered with Apigee runtime instances. See [Getting started with the Service Networking API](https://cloud.google.com/service-infrastructure/docs/service-networking/getting-started). Valid only when [RuntimeType](#RuntimeType) is set to `CLOUD`. The value must be set before the creation of a runtime instance and can be updated only when there are no runtime instances. For example: `default`. Apigee also supports shared VPC (that is, the host network project is not the same as the one that is peering with Apigee). See [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc). To use a shared VPC network, use the following format: `projects/&#123;host-project-id&#125;/&#123;region&#125;/networks/&#123;network-name&#125;`. For example: `projects/my-sharedvpc-host/global/networks/mynetwork` **Note:** Not supported for Apigee hybrid. |
| `runtimeType` | `string` | Required. Runtime type of the Apigee organization based on the Apigee subscription purchased. |
| `properties` | `object` | Message for compatibility with legacy Edge specification for Java Properties object in JSON. |
| `type` | `string` | Not used by Apigee. |
| `createdAt` | `string` | Output only. Time that the Apigee organization was created in milliseconds since epoch. |
| `lastModifiedAt` | `string` | Output only. Time that the Apigee organization was last modified in milliseconds since epoch. |
| `caCertificate` | `string` | Output only. Base64-encoded public certificate for the root CA of the Apigee organization. Valid only when [RuntimeType](#RuntimeType) is `CLOUD`. |
| `attributes` | `array` | Not used by Apigee. |
| `apigeeProjectId` | `string` | Output only. Apigee Project ID associated with the organization. Use this project to allowlist Apigee in the Service Attachment when using private service connect with Apigee. |
| `addonsConfig` | `object` | Add-on configurations for the Apigee organization. |
| `apiConsumerDataEncryptionKeyName` | `string` | Cloud KMS key name used for encrypting API consumer data. Required for US/EU regions when [BillingType](#BillingType) is `SUBSCRIPTION`. When [BillingType](#BillingType) is `EVALUATION` or the region is not US/EU, a Google-Managed encryption key will be used. Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*` |
| `expiresAt` | `string` | Output only. Time that the Apigee organization is scheduled for deletion. |
| `customerName` | `string` | Not used by Apigee. |
| `billingType` | `string` | Billing type of the Apigee organization. See [Apigee pricing](https://cloud.google.com/apigee/pricing). |
| `apiConsumerDataLocation` | `string` | This field is needed only for customers with control plane in US or EU. Apigee stores some control plane data only in single region. This field determines which single region Apigee should use. For example: "us-west1" when control plane is in US or "europe-west2" when control plane is in EU. |
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
