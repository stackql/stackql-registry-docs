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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.assuredworkloads.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only. |
| <CopyableCode code="billingAccount" /> | `string` | Optional. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`. |
| <CopyableCode code="complianceRegime" /> | `string` | Required. Immutable. Compliance Regime associated with this workload. |
| <CopyableCode code="complianceStatus" /> | `object` | Represents the Compliance Status of this workload |
| <CopyableCode code="compliantButDisallowedServices" /> | `array` | Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment. |
| <CopyableCode code="createTime" /> | `string` | Output only. Immutable. The Workload creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload |
| <CopyableCode code="ekmProvisioningResponse" /> | `object` | External key management systems(EKM) Provisioning response |
| <CopyableCode code="enableSovereignControls" /> | `boolean` | Optional. Indicates the sovereignty status of the given workload. Currently meant to be used by Europe/Canada customers. |
| <CopyableCode code="etag" /> | `string` | Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations. |
| <CopyableCode code="kajEnrollmentState" /> | `string` | Output only. Represents the KAJ enrollment state of the given workload. |
| <CopyableCode code="kmsSettings" /> | `object` | Settings specific to the Key Management Service. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels applied to the workload. |
| <CopyableCode code="partner" /> | `string` | Optional. Partner regime associated with this workload. |
| <CopyableCode code="partnerPermissions" /> | `object` | Permissions granted to the AW Partner SA account for the customer workload |
| <CopyableCode code="partnerServicesBillingAccount" /> | `string` | Optional. Billing account necessary for purchasing services from Sovereign Partners. This field is required for creating SIA/PSN/CNTXT partner workloads. The caller should have 'billing.resourceAssociations.create' IAM permission on this billing-account. The format of this string is billingAccounts/AAAAAA-BBBBBB-CCCCCC |
| <CopyableCode code="provisionedResourcesParent" /> | `string` | Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/{folder_id} |
| <CopyableCode code="resourceMonitoringEnabled" /> | `boolean` | Output only. Indicates whether resource monitoring is enabled for workload or not. It is true when Resource feed is subscribed to AWM topic and AWM Service Agent Role is binded to AW Service Account for resource Assured workload. |
| <CopyableCode code="resourceSettings" /> | `array` | Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional. |
| <CopyableCode code="resources" /> | `array` | Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only. |
| <CopyableCode code="saaEnrollmentResponse" /> | `object` | Signed Access Approvals (SAA) enrollment response. |
| <CopyableCode code="violationNotificationsEnabled" /> | `boolean` | Optional. Indicates whether the e-mail notification for a violation is enabled for a workload. This value will be by default True, and if not present will be considered as true. This should only be updated via updateWorkload call. Any Changes to this field during the createWorkload call will not be honored. This will always be true while creating the workload. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Gets Assured Workload associated with a CRM Node |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists Assured Workloads under a CRM Node. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates Assured Workload. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. In addition to assuredworkloads.workload.delete permission, the user should also have orgpolicy.policy.set permission on the deleted folder to remove Assured Workloads OrgPolicies. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| <CopyableCode code="analyze_workload_move" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Analyzes a hypothetical move of a source resource to a target workload to surface compliance risks. The analysis is best effort and is not guaranteed to be exhaustive. |
| <CopyableCode code="enable_resource_monitoring" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Enable resource violation monitoring for a workload. |
| <CopyableCode code="mutate_partner_permissions" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Update the permissions settings for an existing partner workload. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| <CopyableCode code="restrict_allowed_resources" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at https://cloud.google.com/assured-workloads/docs/supported-products In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality. |

## `SELECT` examples

Lists Assured Workloads under a CRM Node.

```sql
SELECT
name,
billingAccount,
complianceRegime,
complianceStatus,
compliantButDisallowedServices,
createTime,
displayName,
ekmProvisioningResponse,
enableSovereignControls,
etag,
kajEnrollmentState,
kmsSettings,
labels,
partner,
partnerPermissions,
partnerServicesBillingAccount,
provisionedResourcesParent,
resourceMonitoringEnabled,
resourceSettings,
resources,
saaEnrollmentResponse,
violationNotificationsEnabled
FROM google.assuredworkloads.workloads
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workloads</code> resource.

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
INSERT INTO google.assuredworkloads.workloads (
locationsId,
organizationsId,
billingAccount,
partnerPermissions,
violationNotificationsEnabled,
partnerServicesBillingAccount,
kmsSettings,
complianceRegime,
etag,
provisionedResourcesParent,
displayName,
enableSovereignControls,
labels,
partner,
name,
resourceSettings
)
SELECT 
'{{ locationsId }}',
'{{ organizationsId }}',
'{{ billingAccount }}',
'{{ partnerPermissions }}',
{{ violationNotificationsEnabled }},
'{{ partnerServicesBillingAccount }}',
'{{ kmsSettings }}',
'{{ complianceRegime }}',
'{{ etag }}',
'{{ provisionedResourcesParent }}',
'{{ displayName }}',
{{ enableSovereignControls }},
'{{ labels }}',
'{{ partner }}',
'{{ name }}',
'{{ resourceSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: resources
      value:
        - - name: resourceId
            value: string
          - name: resourceType
            value: string
    - name: billingAccount
      value: string
    - name: partnerPermissions
      value:
        - name: accessTransparencyLogsSupportCaseViewer
          value: boolean
        - name: dataLogsViewer
          value: boolean
        - name: serviceAccessApprover
          value: boolean
        - name: assuredWorkloadsMonitoring
          value: boolean
    - name: violationNotificationsEnabled
      value: boolean
    - name: partnerServicesBillingAccount
      value: string
    - name: kajEnrollmentState
      value: string
    - name: saaEnrollmentResponse
      value:
        - name: setupStatus
          value: string
        - name: setupErrors
          value:
            - string
    - name: kmsSettings
      value:
        - name: rotationPeriod
          value: string
        - name: nextRotationTime
          value: string
    - name: complianceRegime
      value: string
    - name: etag
      value: string
    - name: ekmProvisioningResponse
      value:
        - name: ekmProvisioningErrorDomain
          value: string
        - name: ekmProvisioningState
          value: string
        - name: ekmProvisioningErrorMapping
          value: string
    - name: provisionedResourcesParent
      value: string
    - name: displayName
      value: string
    - name: enableSovereignControls
      value: boolean
    - name: labels
      value: object
    - name: complianceStatus
      value:
        - name: acknowledgedResourceViolationCount
          value: integer
        - name: acknowledgedViolationCount
          value: integer
        - name: activeViolationCount
          value: integer
        - name: activeResourceViolationCount
          value: integer
    - name: resourceMonitoringEnabled
      value: boolean
    - name: partner
      value: string
    - name: name
      value: string
    - name: resourceSettings
      value:
        - - name: displayName
            value: string
          - name: resourceId
            value: string
          - name: resourceType
            value: string
    - name: compliantButDisallowedServices
      value:
        - string
    - name: createTime
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workloads</code> resource.

```sql
/*+ update */
UPDATE google.assuredworkloads.workloads
SET 
billingAccount = '{{ billingAccount }}',
partnerPermissions = '{{ partnerPermissions }}',
violationNotificationsEnabled = true|false,
partnerServicesBillingAccount = '{{ partnerServicesBillingAccount }}',
kmsSettings = '{{ kmsSettings }}',
complianceRegime = '{{ complianceRegime }}',
etag = '{{ etag }}',
provisionedResourcesParent = '{{ provisionedResourcesParent }}',
displayName = '{{ displayName }}',
enableSovereignControls = true|false,
labels = '{{ labels }}',
partner = '{{ partner }}',
name = '{{ name }}',
resourceSettings = '{{ resourceSettings }}'
WHERE 
locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}';
```

## `DELETE` example

Deletes the specified <code>workloads</code> resource.

```sql
/*+ delete */
DELETE FROM google.assuredworkloads.workloads
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}';
```
