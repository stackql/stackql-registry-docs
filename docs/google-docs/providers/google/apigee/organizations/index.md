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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.organizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the Apigee organization. |
| <CopyableCode code="description" /> | `string` | Description of the Apigee organization. |
| <CopyableCode code="addonsConfig" /> | `object` | Add-on configurations for the Apigee organization. |
| <CopyableCode code="analyticsRegion" /> | `string` | Required. DEPRECATED: This field will eventually be deprecated and replaced with a differently-named field. Primary Google Cloud region for analytics data storage. For valid values, see [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| <CopyableCode code="apiConsumerDataEncryptionKeyName" /> | `string` | Cloud KMS key name used for encrypting API consumer data. If not specified or [BillingType](#BillingType) is `EVALUATION`, a Google-Managed encryption key will be used. Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*` |
| <CopyableCode code="apiConsumerDataLocation" /> | `string` | This field is needed only for customers using non-default data residency regions. Apigee stores some control plane data only in single region. This field determines which single region Apigee should use. For example: "us-west1" when control plane is in US or "europe-west2" when control plane is in EU. |
| <CopyableCode code="apigeeProjectId" /> | `string` | Output only. Apigee Project ID associated with the organization. Use this project to allowlist Apigee in the Service Attachment when using private service connect with Apigee. |
| <CopyableCode code="attributes" /> | `array` | Not used by Apigee. |
| <CopyableCode code="authorizedNetwork" /> | `string` | Compute Engine network used for Service Networking to be peered with Apigee runtime instances. See [Getting started with the Service Networking API](https://cloud.google.com/service-infrastructure/docs/service-networking/getting-started). Valid only when [RuntimeType](#RuntimeType) is set to `CLOUD`. The value must be set before the creation of a runtime instance and can be updated only when there are no runtime instances. For example: `default`. Apigee also supports shared VPC (that is, the host network project is not the same as the one that is peering with Apigee). See [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc). To use a shared VPC network, use the following format: `projects/{host-project-id}/{region}/networks/{network-name}`. For example: `projects/my-sharedvpc-host/global/networks/mynetwork` **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="billingType" /> | `string` | Billing type of the Apigee organization. See [Apigee pricing](https://cloud.google.com/apigee/pricing). |
| <CopyableCode code="caCertificate" /> | `string` | Output only. Base64-encoded public certificate for the root CA of the Apigee organization. Valid only when [RuntimeType](#RuntimeType) is `CLOUD`. |
| <CopyableCode code="controlPlaneEncryptionKeyName" /> | `string` | Cloud KMS key name used for encrypting control plane data that is stored in a multi region. Only used for the data residency region "US" or "EU". If not specified or [BillingType](#BillingType) is `EVALUATION`, a Google-Managed encryption key will be used. Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*` |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time that the Apigee organization was created in milliseconds since epoch. |
| <CopyableCode code="customerName" /> | `string` | Not used by Apigee. |
| <CopyableCode code="disableVpcPeering" /> | `boolean` | Optional. Flag that specifies whether the VPC Peering through Private Google Access should be disabled between the consumer network and Apigee. Valid only when RuntimeType is set to CLOUD. Required if an authorizedNetwork on the consumer project is not provided, in which case the flag should be set to true. The value must be set before the creation of any Apigee runtime instance and can be updated only when there are no runtime instances. **Note:** Apigee will be deprecating the vpc peering model that requires you to provide 'authorizedNetwork', by making the non-peering model as the default way of provisioning Apigee organization in future. So, this will be a temporary flag to enable the transition. Not supported for Apigee hybrid. |
| <CopyableCode code="displayName" /> | `string` | Display name for the Apigee organization. Unused, but reserved for future use. |
| <CopyableCode code="environments" /> | `array` | Output only. List of environments in the Apigee organization. |
| <CopyableCode code="expiresAt" /> | `string` | Output only. Time that the Apigee organization is scheduled for deletion. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time that the Apigee organization was last modified in milliseconds since epoch. |
| <CopyableCode code="portalDisabled" /> | `boolean` | Configuration for the Portals settings. |
| <CopyableCode code="projectId" /> | `string` | Output only. Project ID associated with the Apigee organization. |
| <CopyableCode code="properties" /> | `object` | Message for compatibility with legacy Edge specification for Java Properties object in JSON. |
| <CopyableCode code="runtimeDatabaseEncryptionKeyName" /> | `string` | Cloud KMS key name used for encrypting the data that is stored and replicated across runtime instances. Update is not allowed after the organization is created. If not specified or [RuntimeType](#RuntimeType) is `TRIAL`, a Google-Managed encryption key will be used. For example: "projects/foo/locations/us/keyRings/bar/cryptoKeys/baz". **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="runtimeType" /> | `string` | Required. Runtime type of the Apigee organization based on the Apigee subscription purchased. |
| <CopyableCode code="state" /> | `string` | Output only. State of the organization. Values other than ACTIVE means the resource is not ready to use. |
| <CopyableCode code="subscriptionPlan" /> | `string` | Output only. Subscription plan that the customer has purchased. Output only. |
| <CopyableCode code="subscriptionType" /> | `string` | Output only. DEPRECATED: This will eventually be replaced by BillingType. Subscription type of the Apigee organization. Valid values include trial (free, limited, and for evaluation purposes only) or paid (full subscription has been purchased). See [Apigee pricing](https://cloud.google.com/apigee/pricing/). |
| <CopyableCode code="type" /> | `string` | Not used by Apigee. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_get" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Gets the profile for an Apigee organization. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| <CopyableCode code="organizations_list" /> | `SELECT` | <CopyableCode code="" /> | Lists the Apigee organizations and associated Google Cloud projects that you have permission to access. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). |
| <CopyableCode code="organizations_create" /> | `INSERT` | <CopyableCode code="" /> | Creates an Apigee organization. See [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). |
| <CopyableCode code="organizations_delete" /> | `DELETE` | <CopyableCode code="organizationsId" /> | Delete an Apigee organization. For organizations with BillingType EVALUATION, an immediate deletion is performed. For paid organizations (Subscription or Pay-as-you-go), a soft-deletion is performed. The organization can be restored within the soft-deletion period, which is specified using the `retention` field in the request or by filing a support ticket with Apigee. During the data retention period specified in the request, the Apigee organization cannot be recreated in the same Google Cloud project. **IMPORTANT: The default data retention setting for this operation is 7 days. To permanently delete the organization in 24 hours, set the retention parameter to `MINIMUM`.** |
| <CopyableCode code="organizations_update" /> | `REPLACE` | <CopyableCode code="organizationsId" /> | Updates the properties for an Apigee organization. No other fields in the organization profile will be updated. |
| <CopyableCode code="organizations_set_addons" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Configures the add-ons for the Apigee organization. The existing add-on configuration will be fully replaced. |
| <CopyableCode code="organizations_set_sync_authorization" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Sets the permissions required to allow the Synchronizer to download environment data from the control plane. You must call this API to enable proper functioning of hybrid. Pass the ETag when calling `setSyncAuthorization` to ensure that you are updating the correct version. To get an ETag, call [getSyncAuthorization](getSyncAuthorization). If you don't pass the ETag in the call to `setSyncAuthorization`, then the existing authorization is overwritten indiscriminately. For more information, see [Configure the Synchronizer](https://cloud.google.com/apigee/docs/hybrid/latest/synchronizer-access). **Note**: Available to Apigee hybrid only. |

## `SELECT` examples

Lists the Apigee organizations and associated Google Cloud projects that you have permission to access. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure).

```sql
SELECT
name,
description,
addonsConfig,
analyticsRegion,
apiConsumerDataEncryptionKeyName,
apiConsumerDataLocation,
apigeeProjectId,
attributes,
authorizedNetwork,
billingType,
caCertificate,
controlPlaneEncryptionKeyName,
createdAt,
customerName,
disableVpcPeering,
displayName,
environments,
expiresAt,
lastModifiedAt,
portalDisabled,
projectId,
properties,
runtimeDatabaseEncryptionKeyName,
runtimeType,
state,
subscriptionPlan,
subscriptionType,
type
FROM google.apigee.organizations
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organizations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.apigee.organizations (
,
lastModifiedAt,
subscriptionPlan,
portalDisabled,
caCertificate,
disableVpcPeering,
apiConsumerDataLocation,
analyticsRegion,
billingType,
authorizedNetwork,
controlPlaneEncryptionKeyName,
runtimeDatabaseEncryptionKeyName,
expiresAt,
runtimeType,
environments,
type,
displayName,
apiConsumerDataEncryptionKeyName,
name,
properties,
projectId,
description,
state,
customerName,
apigeeProjectId,
attributes,
subscriptionType,
addonsConfig,
createdAt
)
SELECT 
'{{  }}',
'{{ lastModifiedAt }}',
'{{ subscriptionPlan }}',
true|false,
'{{ caCertificate }}',
true|false,
'{{ apiConsumerDataLocation }}',
'{{ analyticsRegion }}',
'{{ billingType }}',
'{{ authorizedNetwork }}',
'{{ controlPlaneEncryptionKeyName }}',
'{{ runtimeDatabaseEncryptionKeyName }}',
'{{ expiresAt }}',
'{{ runtimeType }}',
'{{ environments }}',
'{{ type }}',
'{{ displayName }}',
'{{ apiConsumerDataEncryptionKeyName }}',
'{{ name }}',
'{{ properties }}',
'{{ projectId }}',
'{{ description }}',
'{{ state }}',
'{{ customerName }}',
'{{ apigeeProjectId }}',
'{{ attributes }}',
'{{ subscriptionType }}',
'{{ addonsConfig }}',
'{{ createdAt }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: lastModifiedAt
      value: '{{ lastModifiedAt }}'
    - name: subscriptionPlan
      value: '{{ subscriptionPlan }}'
    - name: portalDisabled
      value: '{{ portalDisabled }}'
    - name: caCertificate
      value: '{{ caCertificate }}'
    - name: disableVpcPeering
      value: '{{ disableVpcPeering }}'
    - name: apiConsumerDataLocation
      value: '{{ apiConsumerDataLocation }}'
    - name: analyticsRegion
      value: '{{ analyticsRegion }}'
    - name: billingType
      value: '{{ billingType }}'
    - name: authorizedNetwork
      value: '{{ authorizedNetwork }}'
    - name: controlPlaneEncryptionKeyName
      value: '{{ controlPlaneEncryptionKeyName }}'
    - name: runtimeDatabaseEncryptionKeyName
      value: '{{ runtimeDatabaseEncryptionKeyName }}'
    - name: expiresAt
      value: '{{ expiresAt }}'
    - name: runtimeType
      value: '{{ runtimeType }}'
    - name: environments
      value: '{{ environments }}'
    - name: type
      value: '{{ type }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: apiConsumerDataEncryptionKeyName
      value: '{{ apiConsumerDataEncryptionKeyName }}'
    - name: name
      value: '{{ name }}'
    - name: properties
      value: '{{ properties }}'
    - name: projectId
      value: '{{ projectId }}'
    - name: description
      value: '{{ description }}'
    - name: state
      value: '{{ state }}'
    - name: customerName
      value: '{{ customerName }}'
    - name: apigeeProjectId
      value: '{{ apigeeProjectId }}'
    - name: attributes
      value: '{{ attributes }}'
    - name: subscriptionType
      value: '{{ subscriptionType }}'
    - name: addonsConfig
      value: '{{ addonsConfig }}'
    - name: createdAt
      value: '{{ createdAt }}'

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>organizations</code> resource.

```sql
/*+ update */
REPLACE google.apigee.organizations
SET 
lastModifiedAt = '{{ lastModifiedAt }}',
subscriptionPlan = '{{ subscriptionPlan }}',
portalDisabled = true|false,
caCertificate = '{{ caCertificate }}',
disableVpcPeering = true|false,
apiConsumerDataLocation = '{{ apiConsumerDataLocation }}',
analyticsRegion = '{{ analyticsRegion }}',
billingType = '{{ billingType }}',
authorizedNetwork = '{{ authorizedNetwork }}',
controlPlaneEncryptionKeyName = '{{ controlPlaneEncryptionKeyName }}',
runtimeDatabaseEncryptionKeyName = '{{ runtimeDatabaseEncryptionKeyName }}',
expiresAt = '{{ expiresAt }}',
runtimeType = '{{ runtimeType }}',
environments = '{{ environments }}',
type = '{{ type }}',
displayName = '{{ displayName }}',
apiConsumerDataEncryptionKeyName = '{{ apiConsumerDataEncryptionKeyName }}',
name = '{{ name }}',
properties = '{{ properties }}',
projectId = '{{ projectId }}',
description = '{{ description }}',
state = '{{ state }}',
customerName = '{{ customerName }}',
apigeeProjectId = '{{ apigeeProjectId }}',
attributes = '{{ attributes }}',
subscriptionType = '{{ subscriptionType }}',
addonsConfig = '{{ addonsConfig }}',
createdAt = '{{ createdAt }}'
WHERE 
organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>organizations</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.organizations
WHERE organizationsId = '{{ organizationsId }}';
```
