---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - assuredworkloads
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
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.assuredworkloads.workloads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. The resource name of the workload. Format: organizations/&#123;organization&#125;/locations/&#123;location&#125;/workloads/&#123;workload&#125; Read-only. |
| `kajEnrollmentState` | `string` | Output only. Represents the KAJ enrollment state of the given workload. |
| `resourceSettings` | `array` | Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional. |
| `provisionedResourcesParent` | `string` | Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/&#123;folder_id&#125; |
| `compliantButDisallowedServices` | `array` | Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment." |
| `etag` | `string` | Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations. |
| `labels` | `object` | Optional. Labels applied to the workload. |
| `kmsSettings` | `object` | Settings specific to the Key Management Service. This message is deprecated. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field. |
| `complianceStatus` | `object` | Represents the Compliance Status of this workload |
| `createTime` | `string` | Output only. Immutable. The Workload creation timestamp. |
| `saaEnrollmentResponse` | `object` | Signed Access Approvals (SAA) enrollment response. |
| `billingAccount` | `string` | Optional. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/&#123;billing_account_id&#125;`. For example, `billingAccounts/012345-567890-ABCDEF`. |
| `partner` | `string` | Optional. Partner regime associated with this workload. |
| `complianceRegime` | `string` | Required. Immutable. Compliance Regime associated with this workload. |
| `resources` | `array` | Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only. |
| `displayName` | `string` | Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload |
| `enableSovereignControls` | `boolean` | Optional. Indicates the sovereignty status of the given workload. Currently meant to be used by Europe/Canada customers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_workloads_get` | `SELECT` | `locationsId, organizationsId, workloadsId` | Gets Assured Workload associated with a CRM Node |
| `organizations_locations_workloads_list` | `SELECT` | `locationsId, organizationsId` | Lists Assured Workloads under a CRM Node. |
| `organizations_locations_workloads_create` | `INSERT` | `locationsId, organizationsId` | Creates Assured Workload. |
| `organizations_locations_workloads_delete` | `DELETE` | `locationsId, organizationsId, workloadsId` | Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. |
| `organizations_locations_workloads_mutatePartnerPermissions` | `EXEC` | `locationsId, organizationsId, workloadsId` | Update the permissions settings for an existing partner workload. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| `organizations_locations_workloads_patch` | `EXEC` | `locationsId, organizationsId, workloadsId` | Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| `organizations_locations_workloads_restrictAllowedResources` | `EXEC` | `locationsId, organizationsId, workloadsId` | Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at https://cloud.google.com/assured-workloads/docs/supported-products In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality. |
